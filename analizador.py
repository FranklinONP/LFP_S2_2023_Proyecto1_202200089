from PIL import Image
from operaciones1valor import*
from operaciones2valores import*
from LexemaGeneral import*
import graphviz as gv
import os


global num_col, num_fila,lexemas_captados,objetos_de_Operaciones,prueba,listaErrores,lexemas_ParaGrafo
 
prueba=[]
listaErrores=[]

objetos_de_Operaciones=[]

num_fila=1
num_col=1

lexemas_captados=[]
lexemas_ParaGrafo=[]
lexema=""
lexemaNumero=""
global lexemasCaptadosParaMostrar
lexemasCaptadosParaMostrar=[]

def capturar_lexemas(cadena):
    posicion = 0
    global lexema
    global lexemaNumero
    global num_fila
    global num_col
    global listaErrores
    
    while posicion < len(cadena):
        caracter = cadena[posicion]
        posicion += 1
                
        if ord(caracter) == 34:#Si encuentra la comilla             #lexema abre con comillas
            caracter=cadena[posicion]
            num_col+=1
            while ord(caracter)!=34:
                lexema+=caracter
                posicion+=1
                caracter=cadena[posicion]
            #aca voy a armar mi lexemca como clases

            #aca agrego mi lexema a mi lista 
            prueba.append(lexema.lower())
            lex=LexemaGeneral(lexema.lower())
            agregar_a_lista(lexema)
            lexemas_ParaGrafo.append(lexema.lower())
            lexemas_captados.append(lex)
            posicion+=1
            caracter=cadena[posicion]
            num_col+=len(lexema)+1  
            lexema=""
       
        elif esNumero(caracter):
            nuevaL=cadena[posicion-1:]
            numeroEncontrado=capturarNumero(nuevaL)
            #aca voy a armar mi lexemca como clase       
            numeroAgregar=LexemaGeneral(numeroEncontrado)
            #aca agrego mi lexema a mi lista 
            agregar_a_lista(numeroEncontrado)
            prueba.append(numeroEncontrado)
            lexemas_captados.append(numeroAgregar)
            num_col+=len(str(numeroEncontrado))-1
            posicion+=len(str(numeroEncontrado))-1  
           
        elif ord(caracter)==91 or ord(caracter)==93:  #corchetes
            #aca voy a armar mi lexemca como clases
            caracterToken=LexemaGeneral(caracter)
            #aca agrego mi lexema a mi lista  
            agregar_a_lista(caracter)
            prueba.append(caracter)
            lexemas_captados.append(caracterToken)
            num_col+=1
            
        elif caracter=='\n':#salto de linea
            agregar_a_lista(caracter)
            num_col=1
            num_fila+=1
        elif ord(caracter)==9:#tabulador
            num_col+=4
            agregar_a_lista(caracter)
        #123,125 llaves, 58=Dos puntos  44=Coma  32=espacio
        elif ord(caracter)==123 or ord(caracter)==125 or ord(caracter)==58 or  ord(caracter)== 44 or ord(caracter)==32: 
            num_col+=1
            if ord(caracter)==123 or ord(caracter)==125 or ord(caracter)==44 or ord(caracter)==58 :
                agregar_a_lista(caracter)
        else:
            listaErrores.append(caracter)
            listaErrores.append("Lexico")
            listaErrores.append(num_col)
            listaErrores.append(num_fila)
            num_col+=1
 
def reiniciarFilaColumna():
    global num_col,num_fila
    num_fila=1
    num_col=1           
            
def agregar_a_lista(datos):
    if datos not in lexemasCaptadosParaMostrar:  # Verificar si el dato ya existe en la lista
        lexemasCaptadosParaMostrar.append(datos)             
            
            
def es_error(caracter):
    # Obtener el valor ASCII del carácter
    ascii_valor = ord(caracter)
    
    # Verificar si el carácter no es una letra, número, comilla, llaves, espacio, salto de línea,
    # corchetes, dos puntos o coma (en términos de valores ASCII)
    if not ((65 <= ascii_valor <= 90) or  # Letras mayúsculas (A-Z)
            (97 <= ascii_valor <= 122) or  # Letras minúsculas (a-z)
            (48 <= ascii_valor <= 57) or  # Números (0-9)
            ascii_valor == 34 or  # Comilla doble (")
            ascii_valor == 123 or  # Llave abierta ({)
            ascii_valor == 125 or  # Llave cerrada (})
            ascii_valor == 32 or  # Espacio en blanco
            ascii_valor == 10 or  # Salto de línea (\n)
            ascii_valor == 9 or   # Tabulación (\t)
            ascii_valor == 13 or  # Retorno de carro (\r)
            ascii_valor == 91 or  # Corchete abierto ([)
            ascii_valor == 93 or  # Corchete cerrado (])
            ascii_valor == 58 or  # Dos puntos (:)
            ascii_valor == 44):  # Coma (,)
        return True  # Es un error
    else:
        return False  # No es un error
            
def capturarNumero(cadena):
    numero = ""
    decimal = False
    resultado = None
    for caracter in cadena:
        if caracter.isdigit():
            numero += caracter
        elif caracter == "." and not decimal:
            numero += caracter
            decimal = True
        else:
            break
    
    if decimal:
        resultado = float(numero)
    else:
        resultado = int(numero)
    return resultado

def esNumero(caracter):
    if (ord(caracter)>=48) & (ord(caracter)<=57):
        return True
          
          
 #................................................................

def operarNodosConRecursividad():
    global lexemas_captados
    global objetos_de_Operaciones
    operacionTemporal=""
    numeroIzquierda=""
    numeroDerecha=""
    while lexemas_captados:
        lexema=lexemas_captados.pop(0)
        if lexema.operatoriaConRecursividad()=="operacion":
            
            operacionTemporal=lexemas_captados.pop(0)
        elif lexema.operatoriaConRecursividad()=="valor1":
            numeroIzquierda=lexemas_captados.pop(0)
            if numeroIzquierda.operatoriaConRecursividad() == '[':
                numeroIzquierda = operarNodosConRecursividad()
        elif lexema.operatoriaConRecursividad()=="valor2":
            numeroDerecha=lexemas_captados.pop(0)
            if numeroDerecha.operatoriaConRecursividad() == '[':
                numeroDerecha = operarNodosConRecursividad()
            
        if operacionTemporal and numeroIzquierda and numeroDerecha:
            return operaciones2valor( numeroIzquierda, numeroDerecha, operacionTemporal)
            
        if operacionTemporal and numeroIzquierda and operacionTemporal.operatoriaConRecursividad()==(('seno') or ('coseno') or ('tangente')):
            return operaciones1valor(numeroIzquierda,operacionTemporal)
    #Tuve que poner el de inverson solito porque si lo ponia juntos con el seno conse y tangente no lo agarraba 
        if operacionTemporal and numeroIzquierda and operacionTemporal.operatoriaConRecursividad()==( ('inverso') ):
            return operaciones1valor(numeroIzquierda,operacionTemporal)

    return None


 #................................................................
 #................................................................
 
global atributosDeGrafo
atributosDeGrafo=[]
def atributos():
    global lexemas_ParaGrafo,atributosDeGrafo
    ultimas8=lexemas_ParaGrafo[-8:]
    atributos=[ultimas8[i] for i in range(len(ultimas8)) if i % 2 != 0]
    atributosDeGrafo.append(atributos[0])
    atributosDeGrafo.append(atributos[1])
    atributosDeGrafo.append(atributos[2])
    atributosDeGrafo.append(atributos[3])
    print("color de letra", atributosDeGrafo[2])

global diccionario_colores_graphviz,diccionario_formas_graphviz
diccionario_colores_graphviz = {
    "white": "white",
    "black": "black",
    "gray": "gray",
    "red": "red",
    "green": "green",
    "blue": "blue",
    "yellow": "yellow",
    "orange": "orange",
    "purple": "purple",
    "pink": "pink",
    "brown": "brown",
    "cyan": "cyan",
    "turquoise": "turquoise",
    "violet": "violet",
    "gold": "gold",
    "orchid": "orchid",
    "plum": "plum",
}

diccionario_formas_graphviz = {
    "rectángulo": "box",
    "elipse": "ellipse",
    "círculo": "circle",
    "rombo": "diamond",
    "hexágono": "hexagon",
    "trapezoide": "trapezium",
    "paralelogramo": "parallelogram",
    "triple_círculo": "tripleoctagon",
    "triángulo": "triangle",
    "octágono": "octagon",
}


def extraerResultados():
    global objetos_de_Operaciones
    while True:
        operacion=operarNodosConRecursividad()
        if operacion:
            objetos_de_Operaciones.append(operacion)
        else:
            break
    for objetosOperados in objetos_de_Operaciones:  # cada iteracion lo que traer es un nodo u objeto 
        print(objetosOperados.operatoriaConRecursividad())
        



 
def graficar(objetos_de_Operaciones, atributosDeGrafo):
    atributos()

    def unir_nodos_recursivamente(objeto, indice, codigo, espacio):
        valor = ""
        if objeto:
            if isinstance(objeto, operaciones2valor):
                valor += f'nodo{indice}{codigo}{espacio}[label="{objeto.tipoOperacion.lexemaG}\\n{objeto.operatoriaConRecursividad()}"];\n'
                valor += unir_nodos_recursivamente(objeto.valorIzquierdo, indice, codigo + 1, espacio + "_left")
                valor += f'nodo{indice}{codigo}{espacio} -> nodo{indice}{codigo+1}{espacio}_left;\n'
                valor += unir_nodos_recursivamente(objeto.valorDerecho, indice, codigo + 1, espacio + "_right")
                valor += f'nodo{indice}{codigo}{espacio} -> nodo{indice}{codigo+1}{espacio}_right;\n'
            elif isinstance(objeto, operaciones1valor):
                valor += f'nodo{indice}{codigo}{espacio}[label="{objeto.tipo_operacion.lexemaG}\\n{objeto.operatoriaConRecursividad()}"];\n'
                valor += unir_nodos_recursivamente(objeto.valor_izquierdo, indice, codigo + 1, espacio + "_tri")
                valor += f'nodo{indice}{codigo}{espacio} -> nodo{indice}{codigo+1}{espacio}_tri;\n'
            else:
                valor += f'nodo{indice}{codigo}{espacio}[label="{objeto.operatoriaConRecursividad()}"];\n'
        return valor

    datosArbol = """digraph G {
                    label=" """ + "Arbol de operaciones Franklin Orlando Noj Perez" + """"
                    rankdir="LR"
                    node[style=filled, color=" """ + atributosDeGrafo[1] + """", fontcolor=" """ + atributosDeGrafo[2] + """", shape=""" + atributosDeGrafo[3] + """, fontsize=30,fontweight="bold"]"""

    for i in range(len(objetos_de_Operaciones)):
        datosArbol += unir_nodos_recursivamente(objetos_de_Operaciones[i], i, 0, '')

    datosArbol += "\n}"
    f = open('bb.dot', 'w')
    f.write(datosArbol)
    f.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    os.system(f'dot -Tpng bb.dot -o Grafo_Franklin.png')
    imagen = Image.open('Grafo_Franklin.png')
    imagen.show()

 #........................................................................................................................................
 #........................................................................................................................................
 
  
global json_string 
def crearJsonErrores():
        global json_string
        global listaErrores
        json_string = "{\n\"errores\":[\n"
    # Iterar sobre los datos en grupos de 4 (lexema, tipo, columna, fila)
        for i in range(0, len(listaErrores), 4):
            lexema = listaErrores[i]
            tipo = listaErrores[i + 1]
            columna = listaErrores[i + 2]
            fila = listaErrores[i + 3]
            
            # Agregar un objeto de error al JSON
            json_string += "{\n"
            json_string += f"     \"No\": {i // 4 + 1},\n"
            json_string += "      \"descripcion\": {\n"
            json_string += f"            \"lexema\": \"{lexema}\",\n"
            json_string += f"            \"tipo\": \"{tipo}\",\n"
            json_string += f"            \"columna\": {columna},\n"
            json_string += f"            \"fila\": {fila}\n"
            json_string += "}\n"
            json_string += "},\n"

        # Elimina la coma adicional y cierra los corchetes
        json_string = json_string[:-2]  # Elimina la última coma y el espacio
        json_string += "\n]\n}\n"

        # Especifica la ruta del archivo donde deseas guardar el JSON
        archivo_json = "RESULTADOS_202200089.json"

        # Guarda la cadena JSON en el archivo
        with open(archivo_json, "w") as archivo:
            archivo.write(json_string)
          

 #................................................................
 #................................................................



#-----------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

    
#---------------------------------------------------------------------------------------------------------
