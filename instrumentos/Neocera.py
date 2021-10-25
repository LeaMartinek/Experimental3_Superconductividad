# import visa
from instrumentos.GPIB import GPIB

"""
Clase con funcionalidades para el control del Neocera LTC21.

Comandos de comunicacion con el Neocera:
    - "QSAMP?1;" : Devuelve el valor medido para la temperatura como un string
                   con formato "  273K\n". 

Los comandos de comunicacion con el Neocera se pueden encontrar en su manual.
"""

class Neocera_LTC21(GPIB):
    
    def get_temperature(self):
        fetch = self.instrument.query('QSAMP?1;')
        return float(fetch[0:-3])
