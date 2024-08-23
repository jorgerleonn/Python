#Definiendo una variable
nombre = True

#concatenar con +
bienvenida = "hola" + "nombre"

#concatenar con f-strings
bienvenida = f"hola {nombre}"

#la f es para convertir una variable tipo x, que al principio era un boolean, a texto directamente
print(bienvenida)

# del es una variable para borrar datos
del nombre

#operadores de pertenencia (in y not in)
print("True" not in bienvenida) #False
print("True" in bienvenida) #True