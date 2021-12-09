# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:41:59 2019

@author: MAATI
"""

import matplotlib.pyplot as plt
import numpy as np
import visa
import time

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

## Visa##

"""
rm = visa.ResourceManager()
rm.list_resources()
tc = rm.open_resource('GPIB::10::INSTR')

print(tc.query('*IDN?;'))

tc.write('SMON;')

tc.write('SETP1,8;')

tc.write('SCONT;')

print(tc.query('QSETP?1;'))
"""
##Archivo##

file = open('grafico.txt','a')



# PLOT #
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

H = handler(line)

t0 = time.time()
t = t0

T_aux = tc.query('QSAMP?1;')
T = float(T_aux[0:-3])

tiempos = [t-t0]
temperaturas = [T]

phase = 0
while not H.STOP:
    phase += float(input('..'))
    line.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()

file.close()