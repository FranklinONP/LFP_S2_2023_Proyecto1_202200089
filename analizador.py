entradaJson = '''{ ?
  {
        "Operacion":"Resta"
        "Valor1":6.5
        "Valor2":3.5
    }, *
    {
        "Operacion":"Multiplicacion"
        "Valor1":[
            "Operacion":"Potencia"
            "Valor1":2
            "Valor2":[
        "Operacion":"Raiz"
        "Valor1":9
        "Valor2":2
                ]
        ]
        "Valor2": [
            "Operacion":"Potencia"
            "Valor1":2
            "Valor2":[
                "Operacion":"Raiz"
                "Valor1":9
                "Valor2":2
                ]
        ] +
    },
    {
        "Operacion":"Suma"
        "Valor1":[
        "Operacion":"Seno"
        "Valor1":90
        ]
        "Valor2":5.32
    }
    "Texto":"Realizacion de Operaciones"
    "Color-Fondo-Nodo":"Amarillo"
    "Color-Fuente-Nodo":"Rojo"
    "Forma-Nodo":"Circulo"
    @
}'''

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
    
    while posicion < len(cadena):
        caracter = cadena[posicion]
        posicion += 1
                
        if ord(caracter) == 34:#Si encuentra la comilla
            caracter=cadena[posicion]
            num_col+=1
            while ord(caracter)!=34:
                lexema+=caracter
                posicion+=1
                caracter=cadena[posicion]
            #aca voy a armar mi lexemca como clases
            
            #aca agrego mi lexema a mi lista    
            lexemas_captados.append(lexema)
            posicion+=1
            caracter=cadena[posicion]
            num_col+=len(lexema)+1  
            lexema=""
       
        elif esNumero(caracter):
            nuevaL=cadena[posicion-1:]
            numeroEncontrado=capturarNumero(nuevaL)
            #aca voy a armar mi lexemca como clases
            
            #aca agrego mi lexema a mi lista  
            lexemas_captados.append(numeroEncontrado)
            num_col+=len(str(numeroEncontrado))-1
            posicion+=len(str(numeroEncontrado))-1
            
           
        elif ord(caracter)==91 or ord(caracter)==93:  #corchetes
            #aca voy a armar mi lexemca como clases
            
            #aca agrego mi lexema a mi lista  
            lexemas_captados.append(caracter)
            num_col+=1
            
        elif caracter=='\n':#salto de linea
            num_col=1
            num_fila+=1
        elif ord(caracter)==9:#tabulador
            num_col+=4
        #123,125 llaves, 48=Dos puntos  44=Coma  32=espacio
        elif ord(caracter)==123 or ord(caracter)==125 or ord(caracter)==58 or ord(caracter)== 44 or ord(caracter)==32:
            num_col+=1
        else:
            #Aca agrego los caracteres que no esten dentro de mis caracteres permitidos, necesito sus fila y columna
            num_col+=1
            
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
           
capturar_lexemas(entradaJson)

for l in lexemas_captados:
    print(l)