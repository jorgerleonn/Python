# EJEMPLO 1 DE SETTER Y GETTER ( PROPIEDADES Y VARIABLES PROTEGIDAS )
class Persona:
    
    def __init__(self, nombre, edad):
        self._nombre = nombre # Atributo protegido
        self._edad = edad
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter # Setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("[!] La edad no puede ser 0 o un número negativo")
        
       
manolo = Persona("Manolo", 23)
manolo.edad = 14 # Setter
print(manolo.edad) # Getter

# EJEMPLO 2
import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        funcion()
        final = time.time()
        
        print(f"Tiempo total transcurrido en la funcion {funcion.__name__} : {final - inicio}")
        if args:
            print(args)
            
        if 'nombre' in kwargs and kwargs:
            print(kwargs['nombre'])
    return envoltura

@cronometro
def pausa_corta(*args, **kwargs):
    time.sleep(1)
    
@cronometro
def pausa_larga(*args, **kwargs):
    time.sleep(3)
    
pausa_corta(2,3,4,5, nombre="Jorge", edad=21)
pausa_larga()
    