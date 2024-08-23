import re

text = "Hoy estamos a fecha 10/10/2023, mañana estaremos a 11/10/2023"
matches = re.findall("\d{2}\/\d{2}\/\d{4}", text)
print(matches)

# -----------------------------------------------------------------------------------

text = "Los usuarios pueden contactarnos a soporte@fav.supply o a info@fav.test"
matches = re.findall("(\w+)@(\w+\.\w{2,})", text)
print(matches)

# ----------------------------------------------------------------------------------

text = "Mi gato está en el tejado y mi perro está en el jardín"
matches = re.sub("gato", "perro", text)
print(matches)

# ---------------------------------------------------------------------------------

text = "Campo1,Campo2,Campo3,Campo4"
matches = re.split(",", text)
print(matches)
print(matches[2])

# ---------------------------------------------------------------------------------
# Validación de si la estructura del correo es correcta

def validar_correo(correo):
    patron = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b"
    
    if re.findall(patron, correo):
        return True
    else: return False
    
print(validar_correo("jorgetest@test.com"))

# ----------------------------------------------------------------------------------

text = "Hoy estamos a día 02/12/2023 y mañana estaremos a 11/10/2023"
patron = r"\b(\d{2}\/\d{2}\/\d{4})\b"

for match in re.finditer(patron, text):
    print(f" La fecha es: {match.group(0)}, la cual comienza en la posición {match.start()} y termina en {match.end()}")