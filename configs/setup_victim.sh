#!/bin/bash
# Configuración de la Máquina VÍCTIMA
# IP: 10.21.24.2/24
# Gateway: 192.168.100.1

echo "[*] Configurando máquina VÍCTIMA..."

# Configurar interfaz de red
sudo ip addr flush dev e0
sudo ip addr add 10.21.24.2/24 dev e0
sudo ip link set e0 up
sudo ip route add default via 192.168.100.1

# Verificar configuración
echo "[+] Configuración aplicada:"
ip addr show e0
ip route show

# Instalar herramientas de monitoreo
echo "[*] Instalando herramientas de monitoreo..."
sudo apt update
sudo apt install -y tcpdump wireshark iftop

echo "[] Máquina VÍCTIMA configurada correctamente"
echo "IP: 10.21.24.2/24"
echo "Gateway: 192.168.100.1"
