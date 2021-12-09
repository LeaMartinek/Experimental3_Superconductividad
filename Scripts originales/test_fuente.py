

import parallel
import time

class fuente():
	def __init__(self):
		self.p = parallel.Parallel()  # open LPT1 or /dev/parport0
		self.curr = 0 # 0-> corriente positiva; 1-> corriente negativa
		self.medir = 0 # 1-> tension; 2-> termocupla
		self.p.setData(2*self.curr+self.medir)
	def set(self):
		self.p.setData(2*self.curr+self.medir)
	def invertir(self):
		if(self.curr == 1):
			self.curr = 0
		else:
			self.curr =1
	def medirMucho(self,entrada):
		if entrada=='t':
			self.medir = 1
		elif entrada=='v':
			self.medir = 0

F = fuente()

F.medirMucho("v")
F.set()

print('finished')
