"""
Programa utilizado para la calibración del sensor de temperatura a partir
de la medición de la resistencia de un pt1000.
"""

import matplotlib.pyplot as plt
import time
from datetime import datetime

# Importamos los instrumentos
from instrumentos.fuente import Fuente
from instrumentos.Agilent import Agilent_34420A
from instrumentos.Neocera import Neocera_LTC11

# Los IDs de los equipos pueden varias si se cambian, para buscar los
# IDs de los equipos que estan conectados ver test_GPIB.py
ID_Neocera = "GPIB0::10::INSTR"
ID_Agilent = "GPIB0::22::INSTR"

# Inicializamos los instrumentos
fuente = Fuente()
neocera = Neocera_LTC11(ID_Neocera)
agilent = Agilent_34420A(ID_Agilent)

# Directorio donde se quiere guardar el archivo
file_path = "C:\\Users\\adminib\\Desktop\\Superconductividad Segovia y Martinek\\pt1000_26-11_primera"

# Creamos el archivo donde guardaremos los datos.
file = open(
    file_path + "\\"+ 
    "medicion_" + datetime.today().strftime('%Y%m%d_%H_%M_%S') + ".txt",
    'a'
)
file.write("Tiempo Temperatura V1 V2 \n")  # Cabecera del archivo

### Grafico de los datos obtenidos ###

fig = plt.figure()

# Grafico de temperatura
axTc = fig.add_subplot(311)
axTc.set_xlabel('Tiempo (s)')
axTc.set_ylabel('Temperatura (K)')
lineTc, = axTc.plot([],[])
axTc.ticklabel_format(useOffset=False)

# Grafico de tension en bornes V
axNv = fig.add_subplot(312)
axNv.set_xlabel('Tiempo (s)')
axNv.set_ylabel('Tension V (V)')
lineNv, = axNv.plot([],[])
axNv.ticklabel_format(useOffset=False)


fuente.set_type_measure("V")
fuente.set_mode()
t0 = time.time()
while True:
    T = neocera.get_temperature()
    t = time.time()

    V1 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    V2 = agilent.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    file.write(
        str(t - t0) + " " + str(T) + " " +
        str(V1) + " " + str(V2) + "\n"
    )

    axTc.plot(t - t0, T, "r*")  # Grafico de temperatura
    axNv.plot(t - t0, abs(V1 - V2) / 2, "b.")  # Grafico de tension en bornes V

    plt.pause(0.1)  # Muestra los datos y espera 0.1 segundos
