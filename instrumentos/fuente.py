import parallel

"""
Modos de la fuente segun el codigo que se envie por el puerto paralelo.

El modo "V" se refiere a la medicion del voltage que cae en los terminales
V+ y V-. El modo "T" se refiere a la medicion del voltage que corresponde
a los terminales T+ y T-. 

00 : Corriente negativa medicion en V+ y V-.
01 : Corriente positiva medicion en V+ y V-.
10 : Corriente negativa medicion en T+ y T-.
11 : Corriente positiva medicion en T+ y T-.

Para un ejemplo de uso ver test_fuente.py
"""

class Fuente():

    def __init__(self, current = 1, type_measure = 0):
        self.p = parallel.Parallel()  # open LPT1 or /dev/parport0

        ### Hay que probar que pasa si se usa esto ### 
        #envia el byte en hexa con los puestos 2-9
        # 0xff prende todos
        # 0x00 apaga todos
        # dan voltaje de 0.5 cuando estan apagados y 3.4 prendidos
        #self.p.setData(0x00)

        self.current = current # 0 -> corriente negativa; 1 -> corriente positiva; 
        self.type_measure = type_measure # 0 -> Bornes V; 1 -> Bornes T
        self.set_mode()

    def set_mode(self):
        """ Carga el modo fijado a la fuente """

        self.p.setData(2 * self.current + self.type_measure)

    def invert_current(self):
        """ Cambia le sentido de circulacion de la corriente """

        self.current = int(not self.current)

    def set_type_measure(self, type_measure):
        """ Cambia el modo de medicion de Voltage a Termocupla """

        if type_measure == 'T':
            self.type_measure = 1

        elif type_measure == 'V':
            self.type_measure = 0

        else:
            raise ValueError
