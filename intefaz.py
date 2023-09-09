import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog


#________________________________Funciones_________________________________
def mostrar_opciones(opciones):
    cuadro_texto.delete(1.0, tk.END)  # Limpiar el cuadro de texto
    for opcion in opciones:
        cuadro_texto.insert(tk.END, f"- {opcion}\n")

def salir():
    ventana.quit()  # Cierra el programa

def boton_presionado(boton_num):
    if boton_num == 1:
        opciones = ["Abrir", "Guardar", "Guardar como", "Salir"]
        mostrar_opciones(opciones)
        
def abrir():
    # Add your code for the "Abrir" function here
    file_path = filedialog.askopenfilename()
    print(file_path)      
 
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
            if opcion == "Salir":
                boton_menu.add_command(label=opcion, command=salir)
            elif opcion=="Abrir":
                boton_menu.add_command(label=opcion, command=abrir)
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
