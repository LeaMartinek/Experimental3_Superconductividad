"""
Este programa controla el eqipo neocera ltc-11
Nos vamos a conectar con pyvisa y a 
setear un setpoint de temperatura para que el equipo 
vaya a ese valor
"""

import visa
import time

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
while (t-t0)<2400:
	T = tc.query('QSAMP?1;')
	print(T+str(t-t0))
	file.write(T+str(t-t0))
	time.sleep(1)
	t = time.time()

file.close()