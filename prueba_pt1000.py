"""
Programa utilizado para observar las mediciones de voltajes directamente
en la terminal. Esto nos permitia hacer cambios sobre la muestra o la corriente
y observar directamente el cambio en los voltajes medidos.
"""

import time

# Importamos instrumentos
from instrumentos.fuente import Fuente
from instrumentos.Agilent import Agilent_34420A

# Los IDs de los equipos pueden varias si se cambian, para buscar los
# IDs de los equipos que estan conectados ver test_GPIB.py
ID_Agilent = "GPIB0::22::INSTR"

# Inicializamos los instrumentos
fuente = Fuente()
agilent = Agilent_34420A(ID_Agilent)
fuente.set_type_measure("V")
fuente.set_mode()

while True:
    V1 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    V2 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    print("V = %s V \n" % (abs(V1 - V2) / 2))
