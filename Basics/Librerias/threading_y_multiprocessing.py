import threading
import time

def tarea(num_tarea):
    print(f"\n[+] Hilo {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Hilo {num_tarea} finalizando")
    
thread1 = threading.Thread(target=tarea, args=(1,)) 
thread2 = threading.Thread(target=tarea, args=(2,))
    
thread1.start()
thread2.start()

thread1.join()
thread2.join()
    
print(f"\n[+] Los hilos han finalizado exitosamente")

#------------------------------------------------------------

import multiprocessing

def tarea(num_tarea):
    print(f"\n[+] Hilo {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Hilo {num_tarea} finalizando")
    
proceso1 = multiprocessing.Process(target=tarea, args=(1,))
proceso2 = multiprocessing.Process(target=tarea, args=(2,))
    
proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()
    
print(f"\n[+] Los procesos han finalizado exitosamente")

# ---------------------------------------------------------