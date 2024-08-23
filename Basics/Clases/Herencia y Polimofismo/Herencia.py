# Ejemplo de Herencia de clases
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
        
    
gato = Gato("Firulais")
perro = Perro("Alfredo")

print(gato.hablar())
print(perro.hablar())

