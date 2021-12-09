Resumen
========

Este módulo contiene el código necesario para el control de los instrumentos 
a utilizar en la práctica de superconductividad de Laboratorio 3 en el
Instituto Balseiro. También contiene los códigos de las rutinas usadas para
realizar las mediciones, las cuales pueden servir de ejemplo para quienes
quieran hacer las suyas propias.

En la carpeta 'Scripts originales' se encuentran los scripts originales creados
por Matias Mantiñan. Estos se utilizaron de base para crear los scripts que
se encuentran en este repositorio. 

Si en su experiencia realiza cambios al código que cree que pueden ser 
útiles para las próximas personas que lo vayan a utilizar por favor realice 
un commit a este repositorio y eventualmente será agregado a la rama principal.

Colaboradores:

- Matias Mantiñan: mantinanmatias@gmail.com 

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
este problema por favor documéntelo acá y si no le sucede borre este 
comentario.

Si encuentra algún requerimiento que no fue especificado en el archivo 
`requirements.txt` o algún requerimiento externo,
por favor déjelo documentado aquí.

Ejecución
============

Para correr uno de estos archivos .py debe iniciar una terminal de comandos
e ubicarse dentro de este espacio de trabajo. Luego con el comando que se muestra abajo se ejecutara el archivo que se indique.

    $ python file.py

Lista TODO
============

En el archivo `TODO.txt` se encuentran ideas para mejorar los programas
realizados. Si se le ocurre alguna, déjela registrada ahí, sino, intente
hacerlas para mejorar el programa.