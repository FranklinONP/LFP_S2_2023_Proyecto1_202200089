from operatoria2 import operatoria2
objeto=operatoria2()


#boore la fila y columna juto con sus get
class operaciones2valor():
    def __init__(self,valorIzquierdo,valorDerecho,tipoOperacion):
        self.valorIzquierdo=valorIzquierdo
        self.valorDerecho=valorDerecho
        self.tipoOperacion=tipoOperacion

        
    def operar(self):
        derechoTemporal=""
        izquierdoTemporal=""
        numeroTrabajado=None
        if self.valorIzquierdo!=None:
            #izquierdoTemporalTemporal=self.valorIzquierdo.operar(arbol)
            izquierdoTemporal=self.valorIzquierdo.operar()
            
        if self.valorDerecho!=None:
            #derechoTemporalTemporal=self.valorDerecho.operar(arbol)
            derechoTemporal=self.valorDerecho.operar()
            
        
        if self.tipoOperacion.operar()=="suma":
            return izquierdoTemporal+derechoTemporal
        elif self.tipoOperacion.operar()=="resta":
            return izquierdoTemporal-derechoTemporal
        elif self.tipoOperacion.operar()=="multiplicacion":
            return izquierdoTemporal*derechoTemporal
        elif self.tipoOperacion.operar()=="division":
            return izquierdoTemporal/derechoTemporal
        elif self.tipoOperacion.operar()=="potencia":
            return izquierdoTemporal**derechoTemporal
        elif self.tipoOperacion.operar()=="raiz":
            return izquierdoTemporal**(1/derechoTemporal)
        elif self.tipoOperacion.operar()=="mod":
            return izquierdoTemporal%derechoTemporal  

        else:
            return None
