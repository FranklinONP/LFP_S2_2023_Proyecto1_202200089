# Lenguajes Formales y de Programación
# B-
## Proyecto 1
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Franklin Orlando Noj Pérez
Carne: 202200089
Correo: master11frank@gmail.com/3110022770701@ingenieria.usac.edu.gt
```
---
## Desarrollo de un analizador lexico, capaz de analizar operaciones aritmeticas y trigonometricas, simples o anidadas.


## Objetivos
* Objetivo General
    * Desarrollo de un analizador lexico, el cual tenga una entrada de texto editable para modificar y subir archivos con instrucciones de operaciones matemáticas que pueden ser analizadas y graficadas en forma de árbol binario. 
* Objetivos Específicos
    * El programa sea amigable con el usuario.
    * Sea liviano para no requerir muchos recursos del ordenador.
    * Los archivos analizados sean mostrados lo mas simple y entendible posible

## Caracteristicas del programa
* Desarrollado en el edito de código fuente Visual Studio version 1.81.1

* Desarrollado en Python version 3.11.4
---
## Modulos usados en la práctica
* import tkinter as tk
* from tkinter import scrolledtext 
* from tkinter import filedialog
* from tkinter import simpledialog
* import tkinter as tk
* import sys
* from tkinter import messagebox
---
## Capturas de algunas funciones imortantes en el codigo del programa
<br>


##### Funcion capturar_lexemas
![cargarMovimientos](https://i.ibb.co/SvbNGys/lexemas1.jpg)
![cargarMovimientos2](https://i.ibb.co/b36rwSz/lexemas2.jpg)


Esta función analiza caracter por caracter, de una cadena de tesxto que se le pasa como parametro, la cadena de texto que esta pensada que recibirá, será todo el texto de un text área, pasa por un proceso de selección, dependiendo del caracter que sea, se ira agregando a la clase de lexema general, la cual servirá para la logica de las operaciones que se deberán hacer, tambien la funcion sirve para recolectar datos para darle formato al grafo, el árbol binario, y para captar todos los caracteres, fuera de los parametros establecidos, es decir los errores lexicos.
<br>
<br>

##### Funcion capturarNumeros
![archivoSalida](https://i.ibb.co/kJpQwpF/numero.jpg)

La logica de está funcion se centra en poder extraer el numero completo de una cadena de texto, ya sea un numero entero o decimal, y retorna el mismo casteado al tipo de numero que haya encontrado.
<br>

##### Funcion crearJsonErroes
![archivoSalida](https://i.ibb.co/DRBx7Pr/erroes.jpg)

La logica de está funcion esta basada en construir un Json, el cuál llevará los errores LEXICOS encontrados en la cadena de testo, esto están guardados en una lista nativa de python, cada json_string tiene tabulaciones y saltos de linea, para que cuando creé el archivo Json este ya este identado para una mejor comprensión y lectura de los errores.
<br>


##### AFD
![archivoSalida](https://i.ibb.co/pWhwkrj/AFD.jpg)

AFD
GRAMATICA {E,N,Inicio,Producciones}
A={+,-,*,^,/,sqrt(N )}
T={seno,coseno,tangente,1/n}
"#={1,2,3,4,5,6,7,8,9}
E={A,T,#,operaciones}
N={q0}
Inicio=q0

Producciones
q0-->operacionesq1
q1-->Aq2|Tq3
q2-->#q2|Aq2|Tq3|e
q3-->#q3|Tq3|Aq2|e


<br>






