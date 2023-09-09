import tkinter as tk
from tkinter import scrolledtext 
from tkinter import filedialog
from tkinter import simpledialog

def button1_hover_in(event):
    button1.config(bg="gray", fg="black")  # Cambia el color del botón 1 a gris
    button1.config(cursor="hand2")

def button1_hover_out(event):
    button1.config(bg="burlywood1", fg="black")  # Restaura el color del botón 1 a su color original
    button1.config(cursor="arrow")




#########
def button2_hover_in(event):
    button2.config(bg="yellow", fg="black")  # Cambia el color del botón 2 a amarillo
    button2.config(cursor="hand2")

def button2_hover_out(event):
    button2.config(bg="burlywood1", fg="black")  # Restaura el color del botón 2 a su color original
    button2.config(cursor="arrow")

def button3_hover_in(event):
    button3.config(bg="lightblue", fg="black")  # Cambia el color del botón 3 a celeste
    button3.config(cursor="hand2")

def button3_hover_out(event):
    button3.config(bg="burlywood1", fg="black")  # Restaura el color del botón 3 a su color original
    button3.config(cursor="arrow")

def button4_hover_in(event):
    button4.config(bg="orange", fg="black")  # Cambia el color del botón 4 a naranja
    button4.config(cursor="hand2")

def button4_hover_out(event):
    button4.config(bg="burlywood1", fg="black")  # Restaura el color del botón 4 a su color original
    button4.config(cursor="arrow")

#########


def button2_click():#Cuando presiono el boton
    print("B2")

def button3_click():#Cuando presiono el boton
    print("B3")

def button4_click():
    print("B4")







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
        print("cargar archivo")
    
def guardar_archivo():
    global rutaEntrada
    contenido = cuadro_texto.get('1.0', tk.END)
    
    if contenido.strip():  # Verificar que haya contenido antes de guardar
        with open(rutaEntrada, 'w') as file:
            file.write(contenido)
            print("guardar archivo")

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
                    print("guardar archivo como")

window = tk.Tk()
window.title("Proyecto 1_Franklin Orlando Noj Pérez_202200089")
window.config(bg="burlywood")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

button_frame = tk.Frame(window)
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

button1 = tk.Menubutton(button_frame, text="Archivo", bg="burlywood1", fg="black", width=10, height=2)
button1.menu = tk.Menu(button1, tearoff=0)
button1["menu"] = button1.menu

button2 = tk.Button(button_frame, text="Analizar", command=button2_click, bg="burlywood1", fg="black", width=10, height=2)
button3 = tk.Button(button_frame, text="Errores", command=button3_click, bg="burlywood1", fg="black", width=10, height=2)
button4 = tk.Button(button_frame, text="Reporte", command=button4_click, bg="burlywood1", fg="black", width=10, height=2)


button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)
button4.grid(row=0, column=3, padx=10, pady=10)

button2.bind("<Enter>", button2_hover_in)
button2.bind("<Leave>", button2_hover_out)

button3.bind("<Enter>", button3_hover_in)
button3.bind("<Leave>", button3_hover_out)

button4.bind("<Enter>", button4_hover_in)
button4.bind("<Leave>", button4_hover_out)

button1.menu.add_command(label="Cargar Archivo", command=cargar_archivo)
button1.menu.add_command(label="Guardar Archivo", command=guardar_archivo)
button1.menu.add_command(label="Guardar Archivo Como...", command=guardar_archivo_como)

button1.bind("<Enter>", button1_hover_in)
button1.bind("<Leave>", button1_hover_out)

button1.grid(row=0, column=0, padx=10, pady=10)

# Crea el área de texto y configura para que se ajuste horizontalmente
cuadro_texto = scrolledtext.ScrolledText(button_frame, wrap=tk.WORD, width=120, height=30)
cuadro_texto.grid(row=1, column=0, columnspan=15, padx=10, pady=10, sticky="nsew")

window.mainloop()
