class Automovil():
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def describir(self):
        
        return f"Vehículo: {self.marca} {self.modelo}"
    
    
class Coche(Automovil):
    
    def  describir(self):
        return f"Coche: {self.marca} {self.modelo}"
    
    
class Moto(Automovil): 
    
    def  describir(self):
        return f"Moto: {self.marca} {self.modelo}"
    
    
coche = Coche("Toyota", "Corolla")
moto = Moto("Honda", "CBR")
print(coche.describir())
print(moto.describir())