from flask import jsonify, request
from flask_pymongo import pymongo
from app import create_app
from bson.json_util import dumps
import db_config as db


app = create_app()


@app.route('/api/all_locations/', methods=['GET'])
def show_locations():
    all_locations=list(db.db.chihuahua.find())
    for location in all_locations:
        del location ["_id"]   

    return jsonify({"all_locations":all_locations})    


@app.route('/api/location/<int:location_id>/', methods=['GET'])
def show_a_location(location_id):
    location=db.db.chihuahua.find_one({"location_id":location_id})
    del location ["_id"]

    if location != "null":
        return jsonify({
            "location":location
        })
    else:
        return jsonify({
                "status":404,
                "message":"La ubicación no existe",
            })
    

@app.route('/api/add_location/', methods=['POST'])
def add_new_location():    
    if len(request.json) == 6:
            db.db.chihuahua.insert_one({
                "location_id":request.json["location_id"],
                "nombre":request.json["nombre"],
            })
    else:
        return jsonify({
            "ERROR":"ERROR",
            "message":"Te faltan datos",
        })

    return jsonify({
        "message":f"La ubicación {request.json['nombre']} se ha añadido satisfactoriamente",
        "status":200,
    })

@app.route('/api/location/update/<int:location_id>/', methods=['PUT'])
def update_location(location_id):
    if db.db.chihuahua.find_one({'location_id' : request.json["location_id"]}):
            db.db.chihuahua.update_one({'location_id' : request.json["location_id"]},
            {'$set':{
                "location_id":request.json["location_id"],
                "nombre":request.json["nombre"],
            }})
    else:
        return jsonify({'status':400, "message": f"El lugar {request.json['nombre']} no existe"})
    return jsonify({'status':200, "message": f"El lugar de tipo {request.json['nombre']} fue actualizado"})

@app.route('/api/location/delete/<int:location_id>/', methods=['DELETE'])
def delete_song(location_id):
    if db.db.chihuahua.find_one({'location_id' : request.json["location_id"]}):
            db.db.chihuahua.delete_one({'location_id' : request.json["location_id"]})
    else:
        return jsonify({'status':400, "message": f"El lugar {request.json['nombre']} no existe"})
    return jsonify({"status":200, "message": f"El lugar {request.json['nombre']} fue eliminado"})


if __name__ == "__main__":
    app.run(load_dotenv=True, port=8080)

