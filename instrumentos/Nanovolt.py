# import visa
from instrumentos.GPIB import GPIB

"""
Clase con funcionalidades para el control del Nanovolt.
Hereda de GPIB.
"""

class Nanovolt(GPIB):
    
    def get_voltage(self):
        return float(self.instrument.query('READ?;'))
