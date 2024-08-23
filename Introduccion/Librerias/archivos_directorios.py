import os
import shutil

# Checkeando si existe un archivo.txt
if os.path.exists("mi_archivo.txt"):
    print(f"\n[+] El archivo existe\n")
else:
    print(f"\n[!] El archivo no existe")
    
# Creando directorios anidados
if not os.path.exists("mi_directorio/mi_subdirectorio"):
    os.makedirs("mi_directorio/mi_subdirectorio")
    
# Listando todos los recursos del directorio actual
print(f"\n[+] Listado todos los recursos del directorio actual de trabajo:\n")
recursos = os.listdir()
print(recursos)

# Eliminando un directorio
if os.path.exists("mi_directorio"):
    os.rmdir("mi_directorio")

if os.path.exists("mi_directorio"):
    os.rename("mi_directorio", "mi_directorio2")

    
if os.path.exists("mi_directorio2"):
    shutil.rmtree("mi_directorio2")
    
if not os.path.exists("mi_directorio"):
    os.mkdir("mi_directorio")
    
ruta = os.path.join("mi_directorio", "mi_archivo.txt")
print(ruta)