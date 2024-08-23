#!/usr/bin/env python3

# Convenio Lower Camel Case
def comprobacionEstadoApi():
    return
# Upper Camel Case
class TwitterApi:
    
    # SCREAMING_SNAKE_CASE
    VERSION_API = 1
    URL_API = "https://hack4u.io"
    
    _protegido = "Estoy protegido"
    __privada = "Soy privado"
    
# snake_case
def comprobar_estado_api():
    return


if __name__ == '__main__':
    # Si no es importado y es el codigo principal ejecutará esto
    print('Hola soy el módulo principal')
else:
    # Si lo importo o lo utilizo como módulo ejecutará esto
    print('Hola no soy el módulo principal')