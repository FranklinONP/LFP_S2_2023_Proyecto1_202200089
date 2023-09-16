from math import*
class operaciones1valor():

  OPERACIONES = {
    "seno": sin, 
    "coseno": cos,
    "tangente": tan,
    "inverso": lambda x: 1/x
  }

  def __init__(self, valor_izquierdo, tipo_operacion):
    self.valor_izquierdo = valor_izquierdo
    self.tipo_operacion = tipo_operacion


  def operatoriaConRecursividad(self):
    valor = self.valor_izquierdo.operatoriaConRecursividad() if self.valor_izquierdo else None
    
    operacion = self.OPERACIONES.get(self.tipo_operacion.operatoriaConRecursividad())
    if operacion:
      return operacion(valor)
