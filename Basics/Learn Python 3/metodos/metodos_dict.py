diccionario = {
    0 : 'Jorge',
    "apellido" : 'Rodríguez',
    2 : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un objeto con get
valor_de_apellido = diccionario.get("apellido") #si no está dentro del dicionario el programa se traba
valor_de_2 = diccionario.get(2)

#eliminando un elemento del diccionario
diccionario.pop(2)

#eliminando todo del diccionario
#diccionario.clear()

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(valor_de_apellido)
print(valor_de_2)
print(diccionario)
print(diccionario_iterable)

