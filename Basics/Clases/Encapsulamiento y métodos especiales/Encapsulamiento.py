#!/usr/bin/env python3

class Ejemplo:
    
    def __init__(self):
        
        # Atributo protegido
        self._atributo_protegido = "Soy un atributo protegido y no deberías poder verme"
        # Atributo privado
        self.__atributo_privado = "Soy un atributo privado y no deberías poder verme"
        
        
        
ejemplo = Ejemplo()
print(ejemplo._atributo_protegido)
print(ejemplo._Ejemplo__atributo_privado) # existir existe solo que python lo hace menos accesible


# ------------------------------------------------------------------------------------------------

class Coche:
    
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 # Atributo privado
        
    def conducir(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else: 
            print("\n[!] Los kilometros deben ser mayores a 0\n")
            
    def mostrar_kilometros(self):
        return self.__kilometraje
    

coche = Coche("Toyota", "Corolla")
coche.conducir(150)
print(coche.mostrar_kilometros())

# -----------------------------------------------------------------

class CuentaBancaria:
    
    def __init__(self, num_cuenta, titular, saldo_inicial=0):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial
        
    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"\n[+] Saldo actual en la cuenta: {self.__saldo}\n")
        else:
            print("El monto a depositar es erróneo")
        
    def retirar_dinero(self, cantidad):
        if cantidad < self.__saldo and cantidad > 0:
            self.__saldo -= cantidad
            print(f"\n[+] Saldo actual en la cuenta {self.__saldo}\n")
        else:
            print("No puedes retirar tanta cantidad de dinero puto pobre")
        
    def mostrar_dinero(self):
        print(self.__saldo)
      
manolo = CuentaBancaria("123523", "Manolo Vieria")
manolo.depositar_dinero(500)
manolo.mostrar_dinero()
manolo.retirar_dinero(400)
manolo.mostrar_dinero()
