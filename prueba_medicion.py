"""
Programa para medir la caida de tension en los bornes V y T a medida
que varia la temperatura de la muestra.

Requerimientos:
- Es necesario setear la rampa de temperaturas a mano en el Neocera.
- Es necesario setear la escala de medicion a mano en el Nanovolt.
- Es necesario tener prendida la fuente y seteada con la corriente deseada.

La rutina a seguida es:

- Medicion en bornes V:
    Se mide la caida de tension con corriente positiva y luego se invierte
    el sentido de la corriente y se repite la medicion del voltage
    para eliminar efectos termicos en la medicion.

- Medicion en bornes T:
    Se mide la caida de tension con corriente positiva y luego se invierte
    el sentido de la corriente y se repite la medicion del voltage
    para eliminar efectos termicos en la medicion.

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

print("V = %s V ------ T = %s V ------ V - T = %s \n" % (abs(V1 - V2) / 2, abs(T1 - T2) / 2, abs(V1 - V2) / 2 - abs(T1 - T2) / 2))
