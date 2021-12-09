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
while True:
    fuente.set_type_measure("V")
    fuente.set_mode()
    time.sleep(0.2)

    V1 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    V2 = agilent.get_voltage()

    fuente.set_type_measure("T")
    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    T1 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    T2 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()

    print(
        "V = %s V ------ T = %s V ------ V - T = %s \n" % (
            abs(V1 - V2) / 2, abs(T1 - T2) / 2,
            abs(V1 - V2) / 2 - abs(T1 - T2) / 2
        )
    )
