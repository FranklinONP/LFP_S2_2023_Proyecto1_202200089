from logicaOperaciones import logicaOperacionesC
from operatoria2 import operatoria2
objeto=operatoria2()

class operaciones2valor(logicaOperacionesC):
    def __init__(self,valorIzquierdo,valorDerecho,tipoOperacion,fila,columna):
        super().__init__(fila,columna)
        self.valorIzquierdo=valorIzquierdo
        self.valorDerecho=valorDerecho
        self.tipoOperacion=tipoOperacion
        
    def operar(self, arbol):
        derechoTemporal=""
        izquierdoTemporal=""
        numeroTrabajado=None
        if self.valorIzquierdo!=None:
            #izquierdoTemporalTemporal=self.valorIzquierdo.operar(arbol)
            izquierdoTemporal=self.valorIzquierdo.operar(arbol)
            
        if self.valorDerecho!=None:
            #derechoTemporalTemporal=self.valorDerecho.operar(arbol)
            derechoTemporal=self.valorDerecho.operar(arbol)
            
        if self.tipoOperacion.operar(arbol)=="suma":
            return izquierdoTemporal+derechoTemporal
        elif self.tipoOperacion.operar(arbol)=="resta":
            return izquierdoTemporal-derechoTemporal
        elif self.tipoOperacion.operar(arbol)=="multiplicacion":
            return izquierdoTemporal*derechoTemporal
        elif self.tipoOperacion.operar(arbol)=="division":
            return izquierdoTemporal/derechoTemporal
        elif self.tipoOperacion.operar(arbol)=="potencia":
            return izquierdoTemporal**derechoTemporal
        elif self.tipoOperacion.operar(arbol)=="raiz":
            return izquierdoTemporal**(1/derechoTemporal)
        elif self.tipoOperacion.operar(arbol)=="inverso":
            return 1/izquierdoTemporal
        elif self.tipoOperacion.operar(arbol)=="mod":
            return izquierdoTemporal%derechoTemporal  
            
            
        #if numeroTrabajado==objeto.operar(self.tipoOperacion.operar(arbol).OperarNumeros,izquierdoTemporal,derechoTemporal):
            #return numeroTrabajado
        else:
            return None

    def getFila(self):
        return super().getFila
    
    def getColumna(self):
        return super().getColumna
        