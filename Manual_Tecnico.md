# Lenguajes Formales y de Programación
## Práctica 
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Franklin Orlando Noj Pérez
Carne: 202200089
Correo: master11frank@gmail.com/3110022770701@ingenieria.usac.edu.gt
```
---
## Desarrollo de un programa en python que permita gestionar un inventario y movimientos del mismo a partir de archivos de texto.


## Objetivos
* Objetivo General
    * Desarrollo de un programa capaz de cargar, leeer y escribir en archivos de texto
* Objetivos Específicos
    * El programa sea amigable con el usuario.
    * Sea liviano para no requerir muchos recursos del ordenador.

## Caracteristicas del programa
* Desarrollado en el edito de código fuente Visual Studio version 1.81.1

* Desarrollado en Python version 3.11.4
---
## Modulos usados en la práctica
* import tkinter as tk
* from tkinter import filedialog
* from tkinter import messagebox
---
## Capturas de algunas funciones imortantes en el codigo del programa
<br>

##### Funcion cargar Inventario
![cargarInventario](https://i.ibb.co/2FYDH8s/cargar-Inventario.jpg)

Esta funcion es la cual se utiliza para subir los archivos de inventario. Examina la lógica que maneja los nombres de productos, cantidades, precios y ubicaciones, y los agrega a la lista si asi corresponde.
<br>
<br>

##### Funcion Cargar Movimientos
![cargarMovimientos](https://i.ibb.co/s3pDsrG/cargar-Movimientos.jpg)

Esta función maneja varios tipos de movimientos en el inventario, entre ellos agregar stock y vender productos. Para cada movimiento, verifica si el producto existe en la lista del inventario, si la ubicación es correcta y si la cantidad disponible es suficiente para la operación. Si alguna de estas condiciones no se cumple, muestra un mensaje utilizando messagebox.showinfo (Una función para mostrar ventanas de información en consola).
<br>
<br>

##### Funcion Escribir Inventario
![archivoSalida](https://i.ibb.co/nMMGdmY/archivo-Salida.jpg)
###### Funcion ---matriz_para_txt()---
Toma una lista de información de productos. Realiza cálculos con los valores de los productos. Guarda los cálculos y la información en una nueva estructura de datos. Actualiza la lista original con la nueva información.
<br>

######  Función ---Imprimir_en_txt(lista, ruta)---
Toma una lista con información de productos y luego escribe esta información en un archivo de texto en la ruta que se proporcionó.





