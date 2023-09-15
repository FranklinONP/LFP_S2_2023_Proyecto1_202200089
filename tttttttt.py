import graphviz as gv

# Clase nodo del árbol
class TreeNode:
  def __init__(self, value, left=None, right=None, operation=None):
    self.value = value
    self.left = left 
    self.right = right
    self.operation = operation

# Definir los nodos  
root = TreeNode(None, 
               left=TreeNode(1),
               right=TreeNode(2,
                             left=TreeNode(3), 
                             right=TreeNode(4, operation="+")),
               operation="*")
nodes = [root] 

# Grafo
graph = gv.Digraph()

# Función recursiva para agregar nodos y aristas
def add_nodes(node):
  graph.node(str(id(node)))
  
  if node.left:  
    graph.edge(str(id(node)), str(id(node.left)))
    add_nodes(node.left)
  
  if node.right:
    graph.edge(str(id(node)), str(id(node.right))) 
    add_nodes(node.right)

# Llamar función para cada nodo  
for node in nodes:
  add_nodes(node)

# Agregar etiquetas con valores y operaciones
for node in nodes:
  graph.node(str(id(node)), label=f"{node.value} {node.operation}")

graph.render("tree", view=True)