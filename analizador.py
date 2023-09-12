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
}'''
from operaciones1valor import*
from operaciones2valores import*
from Lexema import*
from Numero import*



global num_col
global num_fila
global lexemas_captados
global instrucciones 

global pruba   
prueba=[]

instrucciones=[]

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
            lex=Lexema(lexema.lower(),num_fila,num_col)
            lexemas_captados.append(lex)
            posicion+=1
            caracter=cadena[posicion]
            num_col+=len(lexema)+1  
            lexema=""
       
        elif esNumero(caracter):
            nuevaL=cadena[posicion-1:]
            numeroEncontrado=capturarNumero(nuevaL)
            #aca voy a armar mi lexemca como clase       
            numeroAgregar=Numero(numeroEncontrado,num_fila,num_col)
            #aca agrego mi lexema a mi lista  
            prueba.append(numeroEncontrado)
            lexemas_captados.append(numeroAgregar)
            num_col+=len(str(numeroEncontrado))-1
            posicion+=len(str(numeroEncontrado))-1  
           
        elif ord(caracter)==91 or ord(caracter)==93:  #corchetes
            #aca voy a armar mi lexemca como clases
            caracterToken=Lexema(caracter,num_fila,num_col)
            #aca agrego mi lexema a mi lista  
            prueba.append(caracter)
            prueba.append(num_fila)
            prueba.append(num_col)
            lexemas_captados.append(caracterToken)
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
           
for l in lexemas_captados:
    print(l)
    
    
def imprimirReporte():
    global lexemas_captados
    global instrucciones
    operacionTemporal=""
    n1=""
    n2=""
    while lexemas_captados:
        lexema=lexemas_captados.pop(0)
        if lexema.operar(None)=="operacion":
            operacionTemporal=lexemas_captados.pop(0)
        elif lexema.operar(None)=="valor1":
            n1=lexemas_captados.pop(0)
            if n1.operar(None) == '[':
                n1 = imprimirReporte()
        elif lexema.operar(None)=="valor2":
            n2=lexemas_captados.pop(0)
            if n2.operar(None) == '[':
                n2 = imprimirReporte()
            
        if operacionTemporal and n1 and n2:
            return operaciones2valor( n1, n2, operacionTemporal, f'Inicio: {operacionTemporal.getFila()}:{operacionTemporal.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')
            
        if operacionTemporal and n1 and operacionTemporal.operar(None)==('seno'):
            return operaciones1valor(n1,operacionTemporal,
                    f'Inicia en: {operacionTemporal.getFila()}:{operacionTemporal.getColumna()}',
                    f'Termina en:{n1.getFila()}:{n1.getColumna}')
            
        if operacionTemporal and n1 and operacionTemporal.operar(None)==('coseno'):
            return operaciones1valor(n1,operacionTemporal,
                    f'Inicia en: {operacionTemporal.getFila()}:{operacionTemporal.getColumna()}',
                    f'Termina en:{n1.getFila()}:{n1.getColumna}')
            
        if operacionTemporal and n1 and operacionTemporal.operar(None)==('tangente'):
            return operaciones1valor(n1,operacionTemporal,
                    f'Inicia en: {operacionTemporal.getFila()}:{operacionTemporal.getColumna()}',
                    f'Termina en:{n1.getFila()}:{n1.getColumna}')
            
    return None

def ejecutable():
    global instrucciones
    while True:
        operacion=imprimirReporte()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    for intruc in instrucciones:
        print(intruc.operar(None))
        
capturar_lexemas(entradaJson)
ejecutable()
