#!/usr/bin/env python3
import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def send_message(client_socket, username, textWidget, entryWidget):
    message = entryWidget.get()
    client_socket.sendall(f"{username} > {message}".encode())
    
    entryWidget.delete(0, END)
    textWidget.configure(state="normal")
    textWidget.insert(END,f"{username} > {message}\n")
    textWidget.configure(state="disabled")
    
def receive_message(client_socket, textWidget):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            
            if not message:
                break
                
            textWidget.configure(state="normal")
            textWidget.insert(END,message)
            textWidget.configure(state="disabled")
            
        except:
            break
        
def list_users_request(client_socket):
    client_socket.sendall("!usuarios".encode())

def exit_request(client_socket, username, window):
    client_socket.sendall(f"\n[!] El usuario {username} ha abandonado el chat\n".encode())
    client_socket.close()
    
    window.quit()
    window.destroy()
    
def client_program():
    
    host = 'localhost'
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))
    
    username = input(f"\n[+] Introduce tu usuario: ")
    client_socket.sendall(username.encode())
    
    window = Tk()
    window.title("Chat")
    
    textWidget = ScrolledText(window, state='disabled')
    textWidget.pack(padx=5, pady=5)
    
    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=5, fill=BOTH)
    
    entryWidget = Entry(frame_widget, font=("Arial", 14))
    entryWidget.bind("<Return>", lambda _: send_message(client_socket, username, textWidget, entryWidget))
    entryWidget.pack(side=LEFT, fill=X, expand=1, padx=5)
    
    entryButton = Button(frame_widget, text="Enviar", command=lambda: send_message(client_socket, username, textWidget, entryWidget))
    entryButton.pack(side=RIGHT)
    
    usersWidget = Button(window, text="Listar usuarios", command=lambda: list_users_request(client_socket))
    usersWidget.pack(padx=5, pady=5)
    
    exitWidget = Button(window, text="Salir", command=lambda: exit_request(client_socket, username, window))
    exitWidget.pack(padx=5, pady=5)
    
    thread = threading.Thread(target=receive_message, args=(client_socket, textWidget))
    thread.daemon = True
    thread.start()
    
    window.mainloop()
    client_socket.close()
    

if __name__ == '__main__':
    client_program()