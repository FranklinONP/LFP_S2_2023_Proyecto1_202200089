class operaciones2valor:
    OPERACIONES = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multiplicacion": lambda x, y: x * y,
        "division": lambda x, y: x / y,
        "potencia": lambda x, y: x ** y,
        "raiz": lambda x, y: x ** (1 / y),
        "mod": lambda x, y: x % y,
    }

    def __init__(self, valorIzquierdo, valorDerecho,tipoOperacion):
        self.valorIzquierdo = valorIzquierdo
        self.valorDerecho = valorDerecho
        self.tipoOperacion = tipoOperacion

    def operatoriaConRecursividad(self):
        izquierdo_temporal = self.valorIzquierdo.operatoriaConRecursividad() if self.valorIzquierdo else None
        derecho_temporal = self.valorDerecho.operatoriaConRecursividad() if self.valorDerecho else None

        operacion = self.tipoOperacion.operatoriaConRecursividad()
        funcion_operacion = self.OPERACIONES.get(operacion)

        if funcion_operacion and izquierdo_temporal is not None and derecho_temporal is not None:
            resultado = funcion_operacion(izquierdo_temporal, derecho_temporal)
            return round(resultado, 3)  # Redondear a 3 decimales
        else:
            return None
