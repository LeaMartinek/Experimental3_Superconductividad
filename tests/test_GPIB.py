# Ejecutar desde el directorio general con 'python /test/test_GPIB.py'

# Agregamos el directorio general a los paths para poder importar GPIB
import sys
sys.path.append(".")  

try:
    import visa
except:
    import pyvisa as visa


from instrumentos.GPIB import GPIB

rm = visa.ResourceManager()
print("Lista de equipos conectados:\n ")
print(rm.list_resources())

ID = input("Escriba el ID del equipo a utilizar: ")

instrument = None
while not instrument:
    try:
        instrument = GPIB(ID)
    except:
        ID = input("No se encontro el equipo, ingrese otro ID: ")

instrument.test_connectivity()
