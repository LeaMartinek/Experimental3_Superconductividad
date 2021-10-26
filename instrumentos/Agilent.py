# import visa
from instrumentos.GPIB import GPIB

"""
Clase con funcionalidades para el control del Agilent 34420A.

Comandos de comunicacion con el Agilent:
    - "READ?;" : Devuelve el valor medido. 

Los comandos de comunicacion con el Agilent se pueden encontrar en su manual.
"""

class Agilent_34420A(GPIB):

    def get_voltage(self):
        return float(self.instrument.query('READ?;'))
