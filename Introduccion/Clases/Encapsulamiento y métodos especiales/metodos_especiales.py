#!/usr/bin/env pyhon3
class Libro:
    
    def __init__(self, autor, titulo):
        
        self.autor = autor
        self.titulo = titulo
        
    def __str__(self):
        return f"El libro {self.titulo}, ha sido escrito por {self.autor}"
    
    def __eq__(self, otro):
        return self.autor == otro.autor and self.titulo == otro.titulo
        
        
mi_libro = Libro("Jorge", "Como ser un Lammer")
libro_2 = Libro("Jorge", "Como ser un Lammer")
print(mi_libro)
print(f"¿Son iguales ambos libros? -> {mi_libro == libro_2}")


# ----------------------------------------------------------------------------

class Caja:
    
    def __init__(self, *frutas):
        self.frutas = frutas
    
    def mostrar_frutas(self):
        for fruta in self.frutas:
            print(fruta)
        
        # print(type(self.frutas))
    
    def __len__(self):
        return len(self.frutas)
    
caja = Caja("Manzana", "Plátano", "Kiwi", "Pera", "Melocotón")
caja.mostrar_frutas()

print(len(caja))


# -------------------------------------------------------------------------

class MiLista:
    
    def __init__(self):
        self.data =  [1,2,3,4,5]
          
    def __getitem__(self, index):
        return self.data[index]
        
        
lista = MiLista()
print(lista[2])


# -------------------------------------------------------------------------

class Saludo:
    
    def __init__(self, saludo):
        self.saludo = saludo
        
    def __call__(self, nombre):
        return f"{self.saludo} {nombre}"


hola = Saludo("¡Hola!")
print(hola("Luis"))
print(hola("Alberto el del culo abierto"))

# --------------------------------------------------------------------------

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    
p1 = Punto(2, 8)
p2 = Punto(4, 9)

print(p1 + p2)

# --------------------------------------------------------------------------

class Contador:
    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):
        self.contador = 0
        return self
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else: 
            raise StopIteration
        
    
c = Contador(50)

for i in c:
    print(i)