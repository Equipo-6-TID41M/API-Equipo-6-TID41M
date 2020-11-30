# Phasmophobia API
--------------

#### Para poder obtener todos los tipos de fantasma se usa esta liga:
```
https://phasmophobiaapi.herokuapp.com/api/all_ghosts/
```
--------------
#### Para poder obtener un tipo de fantasma dependiendo de su ID:
```
https://phasmophobiaapi.herokuapp.com/api/ghost/num/
```
Donde "num" es el ID del tipo de fantasma.

--------------
#### Para poder insertar un nuevo fantasma se requiere de un token:
El uso es:

```
https://phasmophobiaapi.herokuapp.com/<token>/api/add_ghost/
```
Donde "token" es reemplazado por la contraseña que es "phasmophobia"

--------------
#### Para poder modificar datos un fantasma existente se requiere de un token y el ID del fantasma:
El uso es:
```
https://phasmophobiaapi.herokuapp.com/<token>/api/ghost/update/<num>/
```
Donde "token" es reemplazado por la contraseña que es "phasmophobia". Y num es el ID del fantasma a modificar datos.

--------------
#### Para poder eliminar un fantasma existente se requiere de un token y el ID del fantasma:
El uso es:
```
https://phasmophobiaapi.herokuapp.com/<token>/api/ghost/delete/<num>/
```
Donde "token" es reemplazado por la contraseña que es "phasmophobia". Y num es el ID del fantasma a eliminar.