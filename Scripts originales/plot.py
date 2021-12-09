import numpy as np
import matplotlib.pyplot as plt
import sys

file = sys.argv[1]
dat = np.transpose(np.loadtxt(file,skiprows=1))

t = dat[0]
T = dat[1]
V1 = (dat[2]-dat[3])/2
#V2 = (dat[4]-dat[5])/2

plt.plot(T,V1,'.',label='v1')
#plt.plot(T,V2, label= 'v2')
plt.xlabel('Temperatura (K)')

plt.ylabel('Tension (V)')
plt.legend()

plt.show()