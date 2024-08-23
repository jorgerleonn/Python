cadena1 = "Buenos días jefe"
cadena2 = "Que tenga buen día entonces"

#lo que tiene dentro te lo convierte a mayusculas
mayusc = cadena1.upper()

#lo que tiene dentro te lo convierte a minisculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no encuentra nada devuelve -1
busqueda_find = cadena1.find("a") #dará 9 ya que en la cadena 1 la letra a se encuentra en la posición 9

#buscamos una cadena en otra cadena, si no encuentra nada devuelve un error
busqueda_index = cadena1.index("B")

#si es numerico devolvemos true, si no devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, si no devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencia = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith("Buenos")

#verificamos si una cadena termina con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith("jefe")

#remplaza un pedazo de la cadena dada con otra dada
cadena_nueva = cadena1.replace("jefe", "capo")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada)