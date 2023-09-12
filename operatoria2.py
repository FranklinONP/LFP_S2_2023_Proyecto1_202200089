class operatoria2:
    def operar(self,simbolo,izquierdo,derecho):
        if simbolo=="suma":
            return izquierdo+derecho
        if simbolo=="resta":
            return izquierdo-derecho
        if simbolo=="multiplicacion":
            return izquierdo*derecho
        if simbolo=="division":
            return izquierdo/derecho
        if simbolo=="potencia":
            return izquierdo**derecho
        if simbolo=="raiz":
            return izquierdo**(1/derecho)
        if simbolo=="inverso":
            return 1/izquierdo
        if simbolo=="mod":
            return izquierdo%derecho
        else:
            return None
        