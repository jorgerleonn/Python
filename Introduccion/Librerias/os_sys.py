import os

directorio_actual = os.getcwd()
print(directorio_actual)

files = os.listdir(directorio_actual)

print(f"\n[+] Listando los archivos existentes en el directorio {directorio_actual}")

for file in files:
    print(file)
    
if os.path.exists("mi_directorio_creado"):
    print(f"\n[+] El directorio ya ha sido creado")
else:
    os.mkdir("mi_directorio_creado")

files = os.listdir(directorio_actual)

print(f"\n[+] Listando los archivos existentes en el directorio {directorio_actual}\n")

for file in files:
    print(file)
    
# ------------------------------------------------------------------------------------------

import sys

print(f"\n[+] El nombre del script: {sys.argv[0]}")
print(f"\n[+] Total de argumentos que se están pasando al programa: {len(sys.argv)}")
print(f"\n[+] Mostrando todos los argumentos: {','.join(argument for argument in sys.argv)}")
print(f"\n[+] Mostrando las rutas de python:")

for element in sys.path:
    print(element)
    
print(f"\n[+] Saliendo con un código de estado o (exitoso)")
sys.exit(0)