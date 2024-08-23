coded_message = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"""
first_message = """jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."""
second_message = """bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"""
third_message = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."""

abcd = 'abcdefghijklmnopqrstuvwxyz'
letras = abcd*3

lista_letras = []
for letra in letras:
    lista_letras.append(letra)
    
letras_index = []
for letra in abcd:
    letras_index.append(letra)

def decode(string,offset):
    mensaje = ''
    numerito = 0 
    for letter in string:
        index = 0
        if letter in abcd:
            index = letras_index.index(letter)
        numerito = index + offset
        
        if letter not in abcd:
            mensaje += str(letter)
        else: mensaje += str(letras[numerito])   
    return mensaje

def encode(string,offset):
    code_mensaje = ''
    for letter in string:
        index = 0
        if letter in abcd:
            index = letras_index.index(letter)
        
        if letter not in abcd:
            code_mensaje += str(letter)
        else: code_mensaje += str(letras[index + offset])
    return code_mensaje

def try_offsets(string):
    i = 0
    while i <= 26:
        print(decode(string,i))
        i += 1

print(decode(coded_message,10))
print()
print(decode(first_message,10))
print()
print(encode(second_message,14))
print()
print(try_offsets(third_message))

