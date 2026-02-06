#!/bin/bash
# Configuración de la Máquina ATACANTE
# IP: 10.21.23.2/24
# Gateway: 192.168.100.1

echo "[*] Configurando máquina ATACANTE..."

# Configurar interfaz de red
sudo ip addr flush dev eth0
sudo ip addr add 10.21.23.2/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.100.1

# Verificar configuración
echo "[+] Configuración aplicada:"
ip addr show eth0
ip route show

# Instalar dependencias
echo "[*] Instalando dependencias..."
sudo apt update
sudo apt install -y python3 python3-pip tcpdump
pip3 install scapy colorama

echo "[] Máquina ATACANTE configurada correctamente"
echo "IP: 10.21.23.2/24"
echo "Gateway: 192.168.100.1"
