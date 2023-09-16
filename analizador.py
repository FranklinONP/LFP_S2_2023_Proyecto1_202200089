entradaJson = '''{
    "operaciones": 
        { 
        !
            "operacion": "suma",
            "valor1": [
            "operacion":"potencia"
            "Valor1":2
            "Valor2":3],
            "valor2":[  {
            "operacion": "inverso",
            "valor1": 0.2
        }] 
        }$·$&·$&  
}
'''
from operaciones1valor import*
from operaciones2valores import*
from LexemaGeneral import*
import graphviz as gv
import os
from webbrowser import open_new as webbrowser

global num_col, num_fila,lexemas_captados,objetos_de_Operaciones,prueba,listaErrores
 
prueba=[]
listaErrores=[]

objetos_de_Operaciones=[]

num_fila=1
num_col=1

lexemas_captados=[]
lexema=""
lexemaNumero=""

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
            lex=LexemaGeneral(lexema.lower(),num_fila,num_col)
            lexemas_captados.append(lex)
            posicion+=1
            caracter=cadena[posicion]
            num_col+=len(lexema)+1  
            lexema=""
       
        elif esNumero(caracter):
            nuevaL=cadena[posicion-1:]
            numeroEncontrado=capturarNumero(nuevaL)
            #aca voy a armar mi lexemca como clase       
            numeroAgregar=LexemaGeneral(numeroEncontrado,num_fila,num_col)
            #aca agrego mi lexema a mi lista  
            prueba.append(numeroEncontrado)
            lexemas_captados.append(numeroAgregar)
            num_col+=len(str(numeroEncontrado))-1
            posicion+=len(str(numeroEncontrado))-1  
           
        elif ord(caracter)==91 or ord(caracter)==93:  #corchetes
            #aca voy a armar mi lexemca como clases
            caracterToken=LexemaGeneral(caracter,num_fila,num_col)
            #aca agrego mi lexema a mi lista  
            prueba.append(caracter)
            lexemas_captados.append(caracterToken)
            num_col+=1
            
        elif caracter=='\n':#salto de linea
            num_col=1
            num_fila+=1
        elif ord(caracter)==9:#tabulador
            num_col+=4
        #123,125 llaves, 58=Dos puntos  44=Coma  32=espacio
        elif ord(caracter)==123 or ord(caracter)==125 or ord(caracter)==58 or  ord(caracter)== 44 or ord(caracter)==32: 
            num_col+=1
        else:
            listaErrores.append(caracter)
            listaErrores.append("Lexico")
            listaErrores.append(num_col)
            listaErrores.append(num_fila)
            num_col+=1
            
            
            
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
    n1=""
    n2=""
    while lexemas_captados:
        lexema=lexemas_captados.pop(0)
        if lexema.operatoriaConRecursividad()=="operacion":
            
            operacionTemporal=lexemas_captados.pop(0)
        elif lexema.operatoriaConRecursividad()=="valor1":
            n1=lexemas_captados.pop(0)
            if n1.operatoriaConRecursividad() == '[':
                n1 = operarNodosConRecursividad()
        elif lexema.operatoriaConRecursividad()=="valor2":
            n2=lexemas_captados.pop(0)
            if n2.operatoriaConRecursividad() == '[':
                n2 = operarNodosConRecursividad()
            
        if operacionTemporal and n1 and n2:
            return operaciones2valor( n1, n2, operacionTemporal)
            
        if operacionTemporal and n1 and operacionTemporal.operatoriaConRecursividad()==(('seno') or ('coseno') or ('tangente')):
            return operaciones1valor(n1,operacionTemporal)
    #Tuve que poner el de inverson solito porque si lo ponia juntos con el seno conse y tangente como que no agarraba  
        if operacionTemporal and n1 and operacionTemporal.operatoriaConRecursividad()==( ('inverso') ):
            return operaciones1valor(n1,operacionTemporal)

    return None

def extraerResultados():
    global objetos_de_Operaciones
    while True:
        operacion=operarNodosConRecursividad()
        if operacion:
            objetos_de_Operaciones.append(operacion)
        else:
            break
    for intruc in objetos_de_Operaciones:  # cada iteracion lo que traer es un nodo u objeto 
        print(intruc.operatoriaConRecursividad())
        
global diccionarioFormas,diccionarioColores

diccionarioFormas={
        "circulo": "circle",
    "cuadrado": "square",
    "rectangulo": "rectangle",
    "elipse": "ellipse",
    "diamante": "diamond",
    "triangulo": "triangle",
    "paralelogramo": "parallelogram",
    "trapecio": "trapezium",
    "hexagono": "hexagon",
    "octagono": "octagon",
    "pentaedro": "pentagon"
}

diccionarioColores={
    "rojo": "red",
    "verde": "green",
    "azul": "blue",
    "amarillo": "yellow",
    "naranja": "orange",
    "purpura": "purple",
    "rosa": "pink",
    "marron": "brown",
    "gris": "gray",
    "negro": "black",
    "blanco": "white"
}

global fondoGrafo,fuenteLetra,formaGrafo

def definirParametrosParaGrafo(colorG, colorL, forma):
    global diccionarioFormas, diccionarioColores

    formaTemp = diccionarioFormas.get(forma)
    colorGTemp = diccionarioColores.get(colorG)
    colorLTemp = diccionarioColores.get(colorL)

    if formaTemp:
        if colorGTemp and colorLTemp:
            return colorG, colorL, forma
        elif colorGTemp:
            return "Palabra no encontrada en el diccionario de colores", colorLTemp
        elif colorLTemp:
            return colorGTemp, "Palabra no encontrada en el diccionario de formas"
        else:
            return "Palabra no encontrada en los diccionarios de colores y formas", "Palabra no encontrada en los diccionarios"
    else:
        return "Palabra no encontrada en el diccionario de formas", colorGTemp, colorLTemp

global atributosDeGrafo
atributosDeGrafo=[]
def atributos():
    global lexemas_captados
    ultimas8=lexemas_captados[-8:]
    atributos=[ultimas8[i] for i in range(len(ultimas8)) if i % 2 != 0]
    v2,v3,v4=definirParametrosParaGrafo(atributos[1],atributos[2],atributos[3])
    atributosDeGrafo.append(atributos[0])
    atributosDeGrafo.append(v2)
    atributosDeGrafo.append(v3)
    atributosDeGrafo.append(v4)
    print(v3)
    
def graficar():
        atributos()
        print()
        global objetos_de_Operaciones,atributosDeGrafo

        text = """digraph G {
                    label=" """+atributosDeGrafo[0]+""""
                    rankdir="LR"
                    node[style=filled, color=" """+atributosDeGrafo[1]+"""", fontcolor=" """+atributosDeGrafo[2]+"""", shape="""+atributosDeGrafo[3]+"""]"""

        for i in range(len(objetos_de_Operaciones)):
            
            text += unir_nodos_de_graficar(objetos_de_Operaciones[i], i, 0,'')
            

        text += "\n}"
        f = open('bb.dot', 'w')

        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o Arbol_de_Operaciones.png')

def unir_nodos_de_graficar(self, tipo, numero, codigo, barra):
        valor = ""
        if tipo:
            if tipo.isdigit():
                valor += f'nodo{numero}{codigo}{barra}[label="{tipo.operacion(None)}"];\n'
            if type(tipo) == operaciones2valor:
                valor += f'nodo{numero}{codigo}{barra}[label="{tipo.tipo.lexema}\\n{tipo.operacion(None)}"];\n'
                valor += self.unir_nodos_de_graficar(tipo.left ,numero, codigo+1, barra+"_left")
                valor += f'nodo{numero}{codigo}{barra} -> nodo{numero}{codigo+1}{barra}_left;\n'
                valor += self.unir_nodos_de_graficar(tipo.right,numero, codigo+1, barra+"_right")
                valor += f'nodo{numero}{codigo}{barra} -> nodo{numero}{codigo+1}{barra}_right;\n'
            
            if type(tipo) == operaciones1valor:
                valor += f'nodo{numero}{codigo}{barra}[label="{tipo.tipo.lexema}\\n{tipo.operacion(None)}"];\n'
                valor += self.unir_nodos_de_graficar(tipo.left,numero, codigo+1, barra+"_tri")
                valor += f'nodo{numero}{codigo}{barra} -> nodo{numero}{codigo+1}{barra}_tri;\n'
        return valor


        
  
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
    
      
capturar_lexemas(entradaJson)
extraerResultados()
crearJsonErrores()

print("----")
graficar()
print("----")

