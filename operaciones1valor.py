from math import*
class operaciones1valor():

  OPERACIONES = {
    "seno": sin, 
    "coseno": cos,
    "tangente": tan,
    "inverso": lambda x: 1/x
  }

  def __init__(self, valor_izquierdo, tipo_operacion, fila, columna):
    self.valor_izquierdo = valor_izquierdo
    self.tipo_operacion = tipo_operacion
    self.fila = fila
    self.columna = columna

  def operar(self):
    valor = self.valor_izquierdo.operar() if self.valor_izquierdo else None
    
    operacion = self.OPERACIONES.get(self.tipo_operacion.operar())
    if operacion:
      return operacion(valor)

  def get_fila(self):
    return self.fila

  def get_columna(self):   
    return self.columna