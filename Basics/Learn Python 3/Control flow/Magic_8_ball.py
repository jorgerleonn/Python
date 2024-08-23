import random

name = "Jorge"
question = "I will be a succesfull person?"
answer = ""
random_number = random.randint(1,10)

if random_number == 1:
  answer = "Sí Sí, pero mira, ¿Leche y gofio?"
elif random_number == 2:
  answer = "Estás loco cabrón?, ni de fly"
elif random_number == 3:
  answer = "Ni aunque te paguen 4 duros"
elif random_number == 4:
  answer = "definitivamente Sí flaco"
elif random_number == 5:
  answer = "Preguntame luego porque llevo una encochinada... bof!!"
elif random_number == 6:
  answer = "Chacho mandate una papa"
elif random_number == 7:
  answer = "naah de locos, claro que sí"
elif random_number == 8:
  answer = "Lo veo tenso la verdad"
elif random_number == 9:
  answer = "Pues mira, puede que sí fijate"
elif random_number == 10:
  answer = "Ni de coña flaco"
else: answer = "Error"

if question == "":
  print("You forgot the question")
elif name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

