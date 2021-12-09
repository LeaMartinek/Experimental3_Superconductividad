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
    """
		Maneja los eventos de matplotlib y el control de temperatura
    """
    def __init__(self,line,puerto):
        self.line = line
        self.puerto = puerto
        self.setP = 0 #set point
        self.setPex = 0 #punto decimal del set point
        self.new = True # habilita la entrada de un nuevo dato
        self.xs = line.get_xdata()
        self.ys = line.get_ydata()
        self.STOP = False # frena la iteracion
        self.cid = line.figure.canvas.mpl_connect('close_event',self.stop)
        self.cidkey = line.figure.canvas.mpl_connect('key_press_event',self.setPoint)
    
    def stop(self,event):
        self.STOP = True

    def cambiarSetP(self):
        print('nuevo set point: ', self.setP)
        self.puerto.write('SMON;')
        self.puerto.write('SETP1,'+str(self.setP)+';')# setea el setPoint a 80
        self.puerto.write('SCONT;')
		#self.puerto.write('SCONT;')# modo control

    def setPoint(self, event):
        try:
            n = int(event.key)
            if self.new:
                self.setP = n
                self.setPex = 0
                self.new = False
            elif self.setPex==0 :
                self.setP = self.setP*10 + n
            else:
                self.setP = self.setP + n*(10**self.setPex)
                self.setPex -= 1
        except:
            if event.key == '.':
                self.setPex = -1
            if event.key == 'enter':
                self.new = True
                self.cambiarSetP()
            if event.key == 'backspace':
                self.new = True
            if event.key == 'p':
            	plt.cla()
            	print ('reset grafico')

#H = handler(line)




rm = visa.ResourceManager()
rm.list_resources()
tc = rm.open_resource('GPIB::10::INSTR')

print(tc.query('*IDN?;'))



file = open('nadagrafico40-30-11.txt','a')
control = 1
t0 = time.time()
t = t0


fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([],[])

H = handler(line,tc)
H.setPoint(290.0)
#tiempos = []
#temperaturas = []

while not H.STOP:
	T_aux = tc.query('QSAMP?1;')
	T = float(T_aux[0:len(T_aux)-3])
	t = time.time()
#	print(T_aux+str(t-t0))
	file.write(T_aux+str(t-t0))
	
	#tiempos.append(t)
	#temperaturas.append(T)

	#plt.plot(t-t0,T,"r*")
	#plt.pause(0.5) # muestra los datos y espera 0.5 segundos
	ax.plot(t-t0,T,"r*")
	plt.pause(0.5) # muestra los datos y espera 0.5 segundos
#	time.sleep(1)

file.close()

