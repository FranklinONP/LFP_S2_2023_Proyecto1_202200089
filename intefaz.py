import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import filedialog, simpledialog

#Variables globales
rutaEntrada=""


#________________________________Funciones del Menu_________________________
def abrir():
    # Add your code for the "Abrir" function here
    cargar_archivo()
 
def guardar():
    guardar_archivo()

def guardar_como():
    guardar_archivo_como()
    
def salir():
    ventana.quit()  # Cierra el programa

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def mostrar_opciones(opciones):
    cuadro_texto.delete(1.0, tk.END)  # Limpiar el cuadro de texto
    for opcion in opciones:
        cuadro_texto.insert(tk.END, f"- {opcion}\n")

def boton_presionado(boton_num):
    if boton_num == 1:
        opciones = ["Abrir", "Guardar", "Guardar como", "Salir"]
        mostrar_opciones(opciones)
        
def cargar_archivo():
    # Abre un cuadro de diálogo para que el usuario elija un archivo
    archivo = filedialog.askopenfilename()
    global rutaEntrada
    rutaEntrada=archivo

    if archivo:
        # Abre el archivo y lee su contenido
        with open(archivo, 'r') as file:
            contenido = file.read()
        
        # Inserta el contenido en el widget de Text
        cuadro_texto.delete('1.0', tk.END)  # Borra cualquier texto existente en el widget
        cuadro_texto.insert('1.0', contenido)  # Inserta el contenido en la posición 1.0
    
def guardar_archivo():
    global rutaEntrada
    contenido = cuadro_texto.get('1.0', tk.END)
    
    if contenido.strip():  # Verificar que haya contenido antes de guardar
        with open(rutaEntrada, 'w') as file:
            file.write(contenido)


def guardar_archivo_como():
    contenido = cuadro_texto.get('1.0', tk.END)
    
    if contenido.strip():  # Verificar que haya contenido antes de guardar
        # Pedir al usuario el nombre del archivo
        nombre_archivo = simpledialog.askstring("Guardar Archivo", "Ingrese el nombre del archivo:")
        if nombre_archivo:
            archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos json", "*.json")], initialfile=nombre_archivo)
            
            if archivo:
                with open(archivo, 'w') as file:
                    file.write(contenido)


#________________________________Funciones_________________________________       
        
        
        
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto 1_LFP_Franklin Orlando Noj Pérez_202200089")

# Personalización de estilos
estilo = ttk.Style()
estilo.configure("TButton", font=("Helvetica", 12, "bold"), background="gray")

# Crear los botones como submenús en la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

nombres_botones = ["Archivo", "Analizar", "Errores", "Reporte"]
opciones_submenus = [
    ["Abrir", "Guardar", "Guardar como", "Salir"],
    ["Analizar"],
    ["Errores"],
    ["Reporte"]
]

for i in range(4):
    boton_menu = tk.Menu(barra_menu, tearoff=0)
    if i == 0:  # Botón "Archivo"
        for opcion in opciones_submenus[i]:
            if  opcion=="Abrir":
                boton_menu.add_command(label=opcion, command=abrir)
                
            elif opcion=="Guardar":
                boton_menu.add_command(label=opcion, command=guardar)
                
            elif opcion=="Guardar como":
                boton_menu.add_command(label=opcion, command=guardar_como)
                
            elif opcion == "Salir":
                boton_menu.add_command(label=opcion, command=salir)
                
            else:
                boton_menu.add_command(label=opcion, command=lambda i=i: boton_presionado(i+1))
    else:
        for opcion in opciones_submenus[i]:
            boton_menu.add_command(label=opcion, command=lambda i=i: boton_presionado(i+1))
    barra_menu.add_cascade(label=nombres_botones[i], menu=boton_menu)

# Crear el cuadro de texto grande con color de fondo
cuadro_texto = scrolledtext.ScrolledText(ventana, width=120, height=40, bg="lightgray")

# Ubicar el cuadro de texto en la ventana y hacerlo redimensionable
cuadro_texto.pack(expand=True, fill=tk.BOTH, padx=1, pady=10)

# Iniciar el bucle de eventos de la interfaz
ventana.mainloop()
