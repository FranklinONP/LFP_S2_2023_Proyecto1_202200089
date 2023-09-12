from logicaOperaciones import logicaOperacionesC

class Lexema(logicaOperacionesC):

    def __init__(self, lexemaG, fila, columna):
        self.lexemaG = lexemaG
        super().__init__(fila, columna)
    
    def operar(self,arbol):
        return self.lexemaG
 

    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()

