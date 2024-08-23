import requests

response = requests.get('https://google.es')

print(f"\n[+] Status code: {response.status_code}")
print(f"\n[+] Mostrando código fuente de la respuesta: \n")

with open("index.html", 'w') as file:
    file.write(response.text)
    
# -------------------------------------------------------

try: 
    response = requests.get('https://google.es', timeout=1)
    response.raise_for_status()

except requests.Timeout:
    print(f"\n[!] La petición ha excedido el límite de tiempo de espera")
except requests.HTTPError as http_err:
    print(f"\n[!] Error HTTP: {http_err}")
except requests.RequestException as err:
    print(f"\n[!] Error: {err}")
    
else: print(f"\n[!] No ha habido ningún error en la solicitud")

# -----------------------------------------------------
from requests.auth import HTTPBasicAuth

# Para autenticarnos
response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=HTTPBasicAuth('foo', 'bar'))

print(response.text)

# -------------------------------------------------------
url = 'https://httpbin.org/cookies/set/my_cookie/123123'

s = requests.Session() # Para arrastrar las cookies

response = s.get(url)

print(response.text)

# --------------------------------------------------------

from requests import Request, Session

url = 'https://httpbin.org/get'

s = Session() # Para arrastrar las cookies
headers = {'Custom-Header': 'my_custom_header'}

req = Request('GET', url, headers=headers)

prepped = req.prepare()
prepped.headers['Custom_Header'] = 'my_header_changed'
prepped.headers['Another-Header'] = 'another-header'
response = s.send(prepped)

print(response.text)

# ------------------------------------------------------

url = 'http://github.com'

r = requests.get(url)
print(r.url)

r = requests.get(url, allow_redirects=False)
print(r.url)
for request in r.history:
    print(f"\n[+] Hemos pasado por el dominio {request.url} con un código de estado {request.status_code}")

# ------------------------------------------------------
# Así arrastramos la sesión
with Session() as session:
    session.auth = ('foo', 'bar')
    response1 = session.get('https://httpbin.org/basic-auth/foo/bar')
    print(response1.text)
    
    response2 = session.get('https://httpbin.org/basic-auth/foo/bar')
    print(response2.text)
