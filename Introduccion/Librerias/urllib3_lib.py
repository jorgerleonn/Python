import urllib3

http = urllib3.PoolManager() # Controlador de conexiones

response = http.request('GET', 'https://httpbin.org/get')
print(response.data.decode())