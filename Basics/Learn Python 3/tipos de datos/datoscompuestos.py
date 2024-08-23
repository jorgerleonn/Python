#las cosas que están dentro de la lista se van a poder modificar
lista = ["hola",143,True,1.85]
print(lista[0],lista[1])

#las cosas que están dentro de la tupla no se van a poder modificar
tupla = ["hola",143,True,1.85]
print(tupla[0])

#los conjuntos se pueden redefinir pero no puedo cambiarle los elementos 
# de dentro, tampoco acceder por índices y no almacena datos duplicados
conjunto = {"hola"}
conjunto = {"pene"}

#creando un diccionario (dict)
diccionario = {
    'nombre' : 'Jorge',
    'pene' : 18,
    'dato_duplicado' : 'Jorge',
}

print(diccionario['pene'] - 20)