# Ejemplo de Polimorfismo de clases
# El polimorfismo es como un mismo método puede comportarse de forma distinta para diferentes clases
# En el caso de hacer_hablar, le estamos pasando un objeto pero no sabe cual es, sin embargo luego de forma dinámica lo redirigue en función del objeto pasado
class Animal:
    
    def __init__(self, nombre):
        
        self.nombre = nombre
        
    def hablar(self):
        
        raise NotImplementedError("Las subclases definidas deben implementar este método")
    
class Gato(Animal):
    
    def hablar(self):
        
        return f"{self.nombre} dice ¡Miau!"
    
class Perro(Animal):
    
    def hablar(self):
        return f"{self.nombre} dice Guau!" 
        

def hacer_hablar(objeto):
    print(objeto.hablar())
        
        
gato = Gato("Firulais")
perro = Perro("Alfredo")

hacer_hablar(gato)
hacer_hablar(perro)