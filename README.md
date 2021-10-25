Resumen
========

Este módulo contiene el código necesario para el control de los instrumentos 
a utilizar en la práctica de superconductividad de Laboratorio 3 en el
Instituto Balseiro. Tambien contiene los códigos de las rutinas usadas para
realizar las mediciones, las cuales pueden servir de ejemplo para quienes
quieran hacer las suyas propias.

Si en su experiencia realiza cambios al código que cree que pueden ser 
utiles para las proximas personas que lo vayan a utilizar por favor realice 
un commit a este repositorio y eventualmente sera agregado a la rama principal.

Colaboradores:

- Matias Martiñan: 

- Leandro Martinek: leandro.martinek@gmail.com


Requerimientos
============

Para instalar los paquetes necesarios utilizar el siguiente comando en la 
terminal en la carpeta donde se encuentre el repositorio 
(La computadora del laboratorio que se utilizó hasta la fecha 25/10/2021 ya los 
tiene instalados, por lo que no hace falta realizar esto)

    $ python -m pip install -r requirements.txt

En particular el paquete pyparallel (https://github.com/pyserial/pyparallel)
no pude lograr instalarlo en Windows 10. Si se encuentra una solución a
este problema por favor documentelo aca y si no le sucede borre este 
comentario.

Si encuentra algun requerimiento que no fue especificado en el archivo 
`requirements.txt` o algun requerimiento externo,
por favor dejelo documentado aqui. 