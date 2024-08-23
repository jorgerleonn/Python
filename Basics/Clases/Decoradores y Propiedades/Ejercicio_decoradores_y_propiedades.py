# Sin emplear Setters
class Circunferencia:
    def __init__(self, radio):
        self._radio = radio
        
    @property
    def radio(self):
        return self._radio
    
    @property
    def diametro(self):
        return 2 * self._radio
    
    @property
    def area(self):
        return 3.1415 * (self._radio)**2

c = Circunferencia(5)
print(c.radio)
print(c.diametro)
print(c.area)


# Empleando setters
class Circunferencia:
    def __init__(self, radio):
        self._radio = radio
        
    @property
    def radio(self):
        return self._radio
    
    @property
    def diametro(self):
        return 2 * self._radio
    
    @property
    def area(self):
        return 3.1415 * (self._radio)**2
    
    @radio.setter
    def radio(self, valor):
        if self._radio >= 0:
            self._radio = valor
        else: 
            raise ValueError("[!] El radio no puede ser 0 o un número negativo")
         
    
c = Circunferencia(5)

c.radio = 10
print(c.radio)
print(c.area)
print(c.diametro)