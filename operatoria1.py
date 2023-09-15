from math import*

class operatorina1():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ejecutar(self, valor):
        if self.nombre == "seno":
            return sin(valor)
        elif self.nombre == "coseno": 
            return cos(valor) 
        elif self.nombre == "tangente":
            return tan(valor)
        elif self.nombre == "inverso":
            return 1/valor