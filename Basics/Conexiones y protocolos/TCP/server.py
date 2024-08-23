#!/usr/bin/env python3
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket.sock_stream para indicarle que vamos a trabajar con conexiones TCP
server_address = ('localhost', 1234)
server_socket.bind(server_address) # Así nos ponemos en escucha por el puerto 1234

# Limitar el límite de conexiones a 1
server_socket.listen(1)

while True:
    
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024) 
    
    print(f"\n[+] Mensaje recibido del cliente: {data.decode()}")
    print(f"[+] Información del cliente que se ha comunicado con nosotros: {client_address}")
    
    client_socket.sendall(f"Un saludo crack\n".encode())
    client_socket.close()
    