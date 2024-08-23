#!/usr/bin/env python3

# *args
def suma(*args):
    return print(sum(args))
    
    
suma(2,3,4,423,4)

# **kwargs

def presentacion(**kwargs):
    for clave, valor in kwargs.items():
        print(clave,':', valor)
    
    
presentacion(nombre="Jorge", edad=21, profesion="estudiante")