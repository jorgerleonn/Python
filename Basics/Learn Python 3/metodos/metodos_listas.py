lista = list(["hola","jorge",34])
cadena = "hola"

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(cadena)

#agregando con append
lista.append("CUCA")

#agregando un elemento a la lista en un índice específico
lista.insert(2,"PENE")

#agregando varios elementos a la lista
lista.extend([False,69])

print(len(lista))
#eliminando un elemento de la lista (por su indice)
lista.pop(2)
print(len(lista))

#para eliminar el último elemento de la lista
lista.pop(-2) #-1 para eliminar el último, -2 para eliminar el penúltimo...

#removiendo un elemento de la lista por su valor, si no está en la lista, nos tira un error
lista.remove("CUCA")

#eliminando todos los elementos de la lista
#lista.clear()

#ordena los elementos de la lista, pero solo si en la lista hay números
#lista.sort()
#si usamos el parámetro = True ordena la lista del menor al mayor
#si usamos el parámetro = False ordena la lista del mayor al menor
#lista.sort(reverse=True)

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index("jorge")

print(lista)
print(elemento_encontrado)
