from math import*

class operatoria1:
    def operar(self,simbolo,izquierdo):
        if simbolo=="seno":
            return sin(izquierdo)
        if simbolo=="coseno":
            return cos(izquierdo)
        if simbolo=="tangente":
            return tan(izquierdo)
        else:
            return None
        