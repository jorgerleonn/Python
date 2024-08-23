#!/usr/bin/env python3
import argparse
from scapy.all import arping

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-i", "--ip", required=True, dest="ip", help="Host / IP range to Scan")
        
    args = parser.parse_args()
        
    return args.ip

def scan(ip_range):
    
    print("\n[+] Escaneando la red.")
    
    arping(ip_range)
    
    print("\n[+] Escaneo Completo.")

def main():
    ip_range = get_arguments()
    scan(ip_range)

if __name__ == '__main__':
    main()