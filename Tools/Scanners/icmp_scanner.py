#!/usr/bin/env python3
import argparse
from termcolor import colored
import subprocess
from concurrent.futures import ThreadPoolExecutor
import signal
import sys

def def_handler(sig, frame):
      print(colored(f"\n[!] Saliendo del programa...\n", "red"))
      sys.exit(1)
  
signal.signal(signal.SIGINT, def_handler)
  
def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para descubrir hosts activos en una red ICMP")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")
      
    args = parser.parse_args()
      
    return args.target
  
def parse_target(target_str): # verifica si la ip está bien puesta y devuelve todo el rango de ips
    
    # 192.168.1.1-100
    target_str_splitted = target_str.split('.') # ["192","168","1","1","1-100"]
    first_three_octets = '.'.join(target_str_splitted[:3]) # 192.168.1
    
    if len(target_str_splitted) == 4:
        if "-" in target_str_splitted[3]:
            start, end = target_str_splitted[3].split('-') # ["1", "100"]
            return [f"{first_three_octets}.{i}" for i in range(int(start), int(end)+1)]
        else:
            return [target_str]
    else:
        print(colored(f"\n[!] El formato de ip o rango de ip no es válido", "red"))
        
def host_discovery(targets): # verifica con un ping si el código de estado es exitoso o no
    for target in targets:
        try:
            ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
            
            if ping.returncode == 0:
                print(colored(f"\n[i] La IP {target} está activa\n", "green"))
                
        except subprocess.TimeoutExpired:
            pass
            
def main():
    target_str = get_arguments()    
    targets = parse_target(target_str)
    
    print(f"\n[+] Hosts activos en la red:\n")
    
    max_threads = 100
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discovery, targets)
    
    
if __name__ == '__main__':
    main()