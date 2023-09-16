from operatoria2 import operatoria2
objeto=operatoria2()


#boore la fila y columna juto con sus get
class operaciones2valor():
    def __init__(self,valorIzquierdo,valorDerecho,tipoOperacion):
        self.valorIzquierdo=valorIzquierdo
        self.valorDerecho=valorDerecho
        self.tipoOperacion=tipoOperacion

        
    def operatoriaConRecursividad(self):
        derechoTemporal=""
        izquierdoTemporal=""
        numeroTrabajado=None
        if self.valorIzquierdo!=None:
            #izquierdoTemporalTemporal=self.valorIzquierdo.operar(arbol)
            izquierdoTemporal=self.valorIzquierdo.operatoriaConRecursividad()
            
        if self.valorDerecho!=None:
            #derechoTemporalTemporal=self.valorDerecho.operatoriaConRecursividad(arbol)
            derechoTemporal=self.valorDerecho.operatoriaConRecursividad()
            
        
        if self.tipoOperacion.operatoriaConRecursividad()=="suma":
            return izquierdoTemporal+derechoTemporal
        elif self.tipoOperacion.operatoriaConRecursividad()=="resta":
            return izquierdoTemporal-derechoTemporal
        elif self.tipoOperacion.operatoriaConRecursividad()=="multiplicacion":
            return izquierdoTemporal*derechoTemporal
        elif self.tipoOperacion.operatoriaConRecursividad()=="division":
            return izquierdoTemporal/derechoTemporal
        elif self.tipoOperacion.operatoriaConRecursividad()=="potencia":
            return izquierdoTemporal**derechoTemporal
        elif self.tipoOperacion.operatoriaConRecursividad()=="raiz":
            return izquierdoTemporal**(1/derechoTemporal)
        elif self.tipoOperacion.operatoriaConRecursividad()=="mod":
            return izquierdoTemporal%derechoTemporal  

        else:
            return None
