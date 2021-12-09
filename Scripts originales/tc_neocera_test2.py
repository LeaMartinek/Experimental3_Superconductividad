"""
Este programa controla el eqipo neocera ltc-11
Nos vamos a conectar con pyvisa y a 
setear un setpoint de temperatura para que el equipo 
vaya a ese valor
"""

import visa
import time
import matplotlib.pyplot as plt
import numpy as np

class handler():
    
    def __init__(self,line):
        self.line = line
        self.xs = line.get_xdata()
        self.ys = line.get_ydata()
        self.STOP = False
        self.cid = line.figure.canvas.mpl_connect('button_press_event',self.stop)
    
    def stop(self,event):
        self.STOP = True

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

H = handler(line)

phase = 0



rm = visa.ResourceManager()
rm.list_resources()
tc = rm.open_resource('GPIB::10::INSTR')

print(tc.query('*IDN?;'))

tc.write('SMON;')

tc.write('SETP1,8;')

tc.write('SCONT;')

print(tc.query('QSETP?1;'))

file = open('grafico.txt','a')
control = 1
t0 = time.time()
t = t0

tiempos = []
temperaturas = []

while not H.STOP:

	T_aux = tc.query('QSAMP?1;')
	T = float(T_aux[0:-3])
	t = time.time()
	print(T,str(t))
	file.write(T_aux+str(t-t0))
	
	tiempos.append(t)
	temperaturas.append(T)
	line.set_xdata(tiempos)
	line.set_ydata(temperaturas)
	fig.canvas.draw()
	fig.canvas.flush_events()
	
	time.sleep(1)

file.close()