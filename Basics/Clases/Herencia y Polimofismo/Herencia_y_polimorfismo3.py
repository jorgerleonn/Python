
class Dispositivo():
    
    def __init__(self, modelo):
        self.modelo = modelo
        
    def escanear_vulnerabilidades(self):
        raise NotImplementedError("Este método debe de ser definido para el resto de subclases existentes")
    
    
class Ordenador(Dispositivo):
    
    def escanear_vulnerabilidades(self):
        return F"[+] Análisis de vulnerabilidades concluido: Actualización de software necesaria, múltiples desactualizaciones de software detectadas"
    
    
class Router(Dispositivo):
    
    def escanear_vulnerabilidades(self):
        return F"[+] Análisis de vulnerabilidades concluido: Múltiples puertos críticos detectados como abiertos, es recomendable cerrar estos puertos"
    

class TelefonoMovil(Dispositivo):

    def escanear_vulnerabilidades(self):
        return f"[+] Análisis de vulnerabilidades concluido: Múltiples Apps detectadas con permisos excesivos"
    

def realizar_escaneo(dispotivo):
    print(dispotivo.escanear_vulnerabilidades())
    

pc = Ordenador("Dell XPS")
router = Router("Tp-Link Archer C50")
movil = TelefonoMovil("Samsung Galazy S21")

realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)

# ----------------------------------------------------------------------------------------------

class A:
    
    def __init__(self, x):
        self.x = x
        print(f"Valor en x: {self.x}")
        
class B(A):
    
    def __init__(self, x, y):
        print("Inicializando B")
        super().__init__(x)
        self.y = y
        print(f"Valor en y: {self.y}")
        
b = B(2, 10)

# Valor en x: 2
# Valor en y: 10

# ---------------------------------------------------------------------

class A:
    
    def saludo(self):
        return "Saludo desde A"
        
class B(A):
    
    def saludo(self):
        original = super().saludo()
        print(f"{original}, pero tambien Saludo desde B")
        
        
saludo = B()
saludo.saludo()


# --------------------------------------------------------------------

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludo(self):
        
        return f"Hola, soy {self.nombre} y tengo {self.edad}"
        
        
class Empleado(Persona):
    
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
        
    def saludo(self):
        
        return f"{super().saludo()}, y cobro {self.salario} euros brutos anuales"



persona = Empleado(nombre="Alicia", edad=23, salario=35000)
print(persona.saludo())

persona = Persona(nombre="Jorge", edad=21)
print(persona.saludo())