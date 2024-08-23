#!/usr/bin/env python3

def mi_decorador(funcion): # Función de orden superior
    def envoltura():
        print("Estoy saludando en la envoltura del decorador antes de llamar a la función")
        funcion()
        print("Estoy saludando en la envoltrura del decorador después de llamar a la función")
    return envoltura

@mi_decorador
def saludo():
    
    print("Hola, estoy saludando dentro de la función")
    

saludo()
