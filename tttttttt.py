def translate_to_english(word, shape_translation, color_translation):
    shape_translation_result = shape_translation.get(word)
    color_translation_result = color_translation.get(word)

    if shape_translation_result and color_translation_result:
        return shape_translation_result, color_translation_result
    elif shape_translation_result:
        return shape_translation_result, "Palabra no encontrada en el diccionario de colores"
    elif color_translation_result:
        return "Palabra no encontrada en el diccionario de formas", color_translation_result
    else:
        return "Palabra no encontrada en ninguno de los diccionarios", "Palabra no encontrada en ninguno de los diccionarios"

# Diccionario de traducción de formas en Graphviz
shapes_translation = {
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

# Diccionario de traducción de colores en Graphviz
colors_translation = {
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

# Ejemplo de uso
palabra_en_espanol = "circulo"

forma_en_ingles, color_en_ingles = translate_to_english(palabra_en_espanol, shapes_translation, colors_translation)

print(f"{palabra_en_espanol} en inglés (forma) es: {forma_en_ingles}")
print(f"{palabra_en_espanol} en inglés (color) es: {color_en_ingles}")
