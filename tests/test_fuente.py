# Ejecutar desde el directorio general con 'python /test/test_fuente.py'

# Agregamos el directorio general a los paths para poder importar GPIB
import sys
sys.path.append(".")

import time
from instrumentos.fuente import Fuente

# Inicializo con corriente positiva y medicion en bornes "V"
fuente = Fuente(current=1, type_measure=0)
print("Tension y Corriente positiva (01)")

time.sleep(2)

fuente.invert_current()
fuente.set_mode()

print("Tension y Corriente negativa  (00)")

time.sleep(2)

fuente.set_type_measure("T")
fuente.set_mode()

print("Termocupla y Corriente negativa  (10)")

time.sleep(2)

fuente.invert_current()
fuente.set_mode()

print("Termocupla y Corriente positiva  (11)")

time.sleep(2)

print('Fin de la Prueba')
