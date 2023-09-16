mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener las últimas 8 posiciones de la lista
ultimas_ocho = mi_lista[-8:]

# Obtener las posiciones impares (7, 5, 3, 1)
posiciones_impares = [ultimas_ocho[i] for i in range(len(ultimas_ocho)) if i % 2 != 0]

print(ultimas_ocho)
print(posiciones_impares)

print(posiciones_impares[0])