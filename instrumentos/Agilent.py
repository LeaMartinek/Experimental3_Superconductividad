# import visa
from instrumentos.GPIB import GPIB

"""
Clase con funcionalidades para el control del Agilent 34420A.
Hereda de GPIB.
"""

class Agilent_34420A(GPIB):
    
    def get_voltage(self):
        return float(self.instrument.query('READ?;'))
