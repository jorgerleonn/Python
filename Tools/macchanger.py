#!/usr/bin/env python3
import argparse
import re
import subprocess
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la dirección MAC de una interfaz de red")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="MAC Address para la interfaz de red")
      
    return parser.parse_args()
  
def is_valid_input(interface, mac_address):
    
    is_valid_interface = re.match(r'^[a-zA-Z]+[0-9]+$', interface)
    is_valid_mac_address = re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address)
    print(is_valid_interface)
    print(is_valid_mac_address)
    
    return is_valid_interface and is_valid_mac_address

def change_mac_address(interface, mac_address):
    
    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])
        
        print(colored(f"\n[+] La MAC ha sido cambiado exitosamente", "green"))
    else:
        print(colored('Los datos introducidos son incorrectos', 'red'))

def main():
    args = get_arguments()
    change_mac_address(args.interface, args.mac_address)
    
if __name__ == '__main__':
    main()