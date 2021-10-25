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

import matplotlib.pyplot as plt
import time
from datetime import datetime

# Importamos instrumentos
from instrumentos.fuente import Fuente
from instrumentos.Nanovolt import Nanovolt
from instrumentos.Neocera import TC_Neocera_TCL111

# Los IDs de los equipos pueden varias si se cambian, para buscar los
# IDs de los equipos que estan conectados ver test_GPIB.py
ID_Neocera = "GPIB::10::INSTR"
ID_Nanovolt = "GPIB::22::INSTR"

# Inicializamos los instrumentos
fuente = Fuente()
neocera = TC_Neocera_TCL111(ID_Neocera)
nanovolt = Nanovolt(ID_Nanovolt)

# Creamos el archivo donde guardaremos los datos.
file = open(
    "rutina1_" + datetime.today().strftime('%Y%m%d_%H_%M_%S') + ".txt",
    'a'
)
file.write("Tiempo Temperatura V1 V2 T1 T2\n")  # Cabecera del archivo

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

# Grafico de tension en bornes T
axNt = fig.add_subplot(313)
axNt.set_xlabel('Tiempo (s)')
axNt.set_ylabel('Tension T (V)')
lineNt, = axNt.plot([],[])
axNv.ticklabel_format(useOffset=False)

t0 = time.time()
while True:
    T = neocera.get_temperature()
    t = time.time()

    fuente.set_type_measure("V")
    fuente.set_mode()
    
    V1 = nanovolt.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    V2 = nanovolt.get_voltage()

    fuente.set_type_measure("T")
    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    T1 = nanovolt.get_voltage()

    fuente.invert_current()
    fuente.set_mode()
    time.sleep(0.2)

    T2 = nanovolt.get_voltage()

    file.write(
        str(t - t0) + " " + str(T) + " " + str(V1) + " " + str(V2) +
        str(T1) + str(T2) + "\n"
    )
		
    axTc.plot(t - t0, T, "r*")  # Grafico de temperatura
    axNv.plot(t - t0, (V1 - V2) / 2, "b.")  # Grafico de tension en bornes V
    axNv.plot(t - t0, (T1 - T2) / 2, "go")  # Grafico de tension en bornes T
    
    plt.pause(0.1)  # Muestra los datos y espera 0.1 segundos
