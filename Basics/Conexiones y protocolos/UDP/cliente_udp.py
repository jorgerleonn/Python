import socket

def start_udp_client():
    
    host = 'localhost'
    port = 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = "Hola se tensó".encode("utf-8")
        s.sendto(message, (host, port))
        
start_udp_client()