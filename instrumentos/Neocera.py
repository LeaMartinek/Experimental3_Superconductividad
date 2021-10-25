# import visa
from instrumentos.GPIB import GPIB

"""
Clase con funcionalidades para el control del Neocera.
Hereda de GPIB.
"""

class TC_Neocera_TCL111(GPIB):
    
    def get_temperature(self):
        fetch = self.instrument.query('QSAMP?1;')
        return float(fetch[0:-3])
