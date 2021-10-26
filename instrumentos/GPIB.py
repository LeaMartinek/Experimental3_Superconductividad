try:
    import visa
except:
    import pyvisa as visa

""" 
GPIB es un protocolo de comunicacion entre los equipos. 
Se hace una clase general para agregar funcionalidades que son generales
a todos los equipos con este protocolo como el Neocera y el Agilent.

Para un ejemplo de uso ver test_GPIB.py
"""

class GPIB():

    def __init__(self, ID):
        self.id = ID
        self.__connect_instrument(ID)

    def __connect_instrument(self, ID):
        rm = visa.ResourceManager()
        if ID not in rm.list_resources():
            raise Exception("No se encontro el ID del equipo")

        self.instrument = rm.open_resource(ID)
        if not self.id:
            self.id = ID

    def test_connectivity(self):
        ID = self.instrument.query("*IDN?;")
        print("Conectado a " + ID)

    def print_ID(self, connect=True):
        if connect:
            print(self.instrument.query("*IDN?;"))
        else:
            print(self.id)
