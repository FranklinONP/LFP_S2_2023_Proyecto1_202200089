# Supongamos que tienes una lista de datos
datos = ["?", "error lexico", 2, 9, "1", "error lexico", 4, 5]

# Inicializa una cadena JSON vacía
json_string = "{\n\"errores\":[\n"

# Iterar sobre los datos en grupos de 4 (lexema, tipo, columna, fila)
for i in range(0, len(datos), 4):
    lexema = datos[i]
    tipo = datos[i + 1]
    columna = datos[i + 2]
    fila = datos[i + 3]
    
    # Agregar un objeto de error al JSON
    json_string += "{\n"
    json_string += f"\"No\": {i // 4 + 1},\n"
    json_string += "\"descripcion\": {\n"
    json_string += f"\"lexema\": \"{lexema}\",\n"
    json_string += f"\"tipo\": \"{tipo}\",\n"
    json_string += f"\"columna\": {columna},\n"
    json_string += f"\"fila\": {fila}\n"
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

print(f"JSON guardado en {archivo_json}")
