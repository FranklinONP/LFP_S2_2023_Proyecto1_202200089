from logicaOperaciones import logicaOperacionesC
from operatoria1 import operatoria1
from math import*
objeto=operatoria1()

class operaciones1valor(logicaOperacionesC):
    def __init__(self,valorIzquierdo,tipoOperacion,fila,columna):
        super().__init__(fila,columna)
        self.valorIzquierdo=valorIzquierdo
        self.tipoOperacion=tipoOperacion
    
    def operar(self,arbol):
        izquierdoTemporal=""
        numeroTrabajado=None
        if self.valorIzquierdo!=None:
           izquierdoTemporal=self.valorIzquierdo.operar(arbol) 

        if self.tipoOperacion.operar(arbol)=="seno":
            return sin(izquierdoTemporal)
        elif self.tipoOperacion.operar(arbol)=="coseno":
            return cos(izquierdoTemporal)
        elif self.tipoOperacion.operar(arbol)=="tangente":
            return tan(izquierdoTemporal)  
            
        
            #izquierdoTemporal=self.valorIzquierdo.OperarNumeros(arbol)
        #if numeroTrabajado==objeto.operar(self.tipoOperacion.OperarNumeros(arbol),izquierdoTemporal):
        #    return numeroTrabajado
        else: 
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()