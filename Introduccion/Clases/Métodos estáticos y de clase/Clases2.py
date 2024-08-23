#!/usr/bin/nnv python3

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
      
    @property
    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f"\n[+] Propiedades del rectángulo: [Ancho: {self.ancho}][Alto: {self.alto}]"

    def __eq__(self, otro):
        return self.ancho == otro.ancho and self.alto == otro.alto
        
         
rect1 = Rectangulo(20,80)
rect2 = Rectangulo(10,60)

print(rect1)
print(f"\n[+] El área es {rect1.area}")
print(f"\n[+] ¿Son iguales? -> {rect1 == rect2}")

# ----------------Método estático y Método de clase--------------------------- #

class Libro:
    
    IVA = 0.21
    
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    
    @staticmethod # Decoradores
    def es_bestseller(total_de_ventas):
        return total_de_ventas > 5000
    
    @classmethod # Decoradores
    def precio_con_iva(cls, precio):
        return precio + precio*cls.IVA
    

class LibroDigital(Libro):
    
    IVA = 0.1

mi_libro = Libro("¿Como ser un Lammer de los verdad?", "Jorge Rodríguez", 17.5)
mi_libro_digital = LibroDigital("¿Iniciación al Lammer?", "Jorge Rodríguez", 17.5)

print(Libro.es_bestseller(7000))

print(f"\n[+] El precio del libro con IVA incluido es de {round(Libro.precio_con_iva(mi_libro.precio),2)}")
print(f"[+] El precio del libro digital con IVA incluido es de {round(LibroDigital.precio_con_iva(mi_libro_digital.precio),2)}")