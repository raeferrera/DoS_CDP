# CDP DoS Attack 

**Estudiante:** Raelina  
**Matrícula:** 20212371
**Institución:** Instituto Tecnológico de las Américas (ITLA)    
**Fecha:** Febrero 2026

---

##  Objetivo del Script

Implementar un ataque de **Denegación de Servicio (DoS)** explotando el protocolo **CDP (Cisco Discovery Protocol)** mediante el envío masivo de paquetes CDP falsos para:

1. **Saturar la tabla CDP** del switch objetivo con dispositivos falsos
2. **Consumir recursos críticos** (CPU y memoria) del dispositivo de red
3. **Degradar el rendimiento** de la infraestructura de red
4. **Demostrar vulnerabilidades** de protocolos propietarios de capa 2
5. **Documentar contramedidas** efectivas para mitigar el ataque

---

##  Topología de Red

<img width="705" height="467" alt="image" src="https://github.com/user-attachments/assets/943e8391-ba39-4ced-ba93-599565e4233b" />


---

##  Tabla de Direccionamiento IP

| Dispositivo | Interfaz | Dirección IP | Máscara | VLAN | Gateway | Descripción |
|------------|----------|--------------|---------|------|---------|-------------|
| **ATTACKER** | eth0 | 10.21.23.2 | /24 (255.255.255.0) | 23 | 192.168.100.1 | Máquina atacante (VPC) |
| **VICTIM** | e0 | 10.21.24.2 | /24 (255.255.255.0) | 71 | 192.168.100.1 | Máquina víctima (VPC) |
| **ROUTER** | e0/0 | DHCP | - | - | 192.168.100.1 | Interfaz WAN |
| **ROUTER** | e0/1.23 | 10.21.23.1 | /24 (255.255.255.0) | 23 | - | Gateway VLAN 23 |
| **ROUTER** | e0/2.71 | 10.21.24.1 | /24 (255.255.255.0) | 71 | - | Gateway VLAN 71 |
| **SW1** | - | - | - | - | - | Switch capa 2 (VLAN 23) |
| **SW2** | - | - | - | - | - | Switch capa 2 (VLAN 71) |

### Configuración de VLANs

| VLAN ID | Nombre | Red | Dispositivos |
|---------|--------|-----|--------------|
| 23 | VLAN_ATTACKER | 10.21.23.0/24 | ATTACKER, SW1 |
| 71 | VLAN_VICTIM | 10.21.24.0/24 | VICTIM, SW2 |

### Interfaces y Conexiones

**ROUTER CORE:**
- **e0/0:** Conexión a Internet (NAT outside) - 192.168.100.1
- **e0/1:** Trunk 802.1Q  e0/1.23 (VLAN 23 - Red atacante)
- **e0/2:** Trunk 802.1Q  e0/2.71 (VLAN 71 - Red víctima)

**SW1 (Switch VLAN 23):**
- **e0/0:** Trunk hacia Router CORE
- **e0/1:** Access VLAN 23  Conecta a ATTACKER
- **e0/2:** Access VLAN 23

**SW2 (Switch VLAN 71):**
- **e0/0:** Trunk hacia Router CORE
- **e0/1:** Access VLAN 71  Conecta a VICTIM
- **e0/2:** Access VLAN 71

---

##  Parámetros del Script

### Sintaxis Completa
\\\ash
sudo python3 scripts/cdp_dos.py -i <INTERFACE> [-c COUNT] [-d DELAY] [-m MAC]
\\\

### Tabla de Parámetros

| Parámetro | Nombre Largo | Tipo | Requerido | Valor Default | Descripción |
|-----------|--------------|------|-----------|---------------|-------------|
| \-i\ | \--interface\ | string |  SÍ | - | Interfaz de red a utilizar (ej: eth0) |
| \-c\ | \--count\ | int |  NO | 1000 | Cantidad total de paquetes CDP a enviar |
| \-d\ | \--delay\ | float |  NO | 0.001 | Retardo en segundos entre cada paquete |
| \-m\ | \--mac\ | string |  NO | 01:00:0c:cc:cc:cc | Dirección MAC destino (multicast CDP) |

### Ejemplos de Uso con Diferentes Parámetros

**Ejemplo 1: Ataque básico (testing)**
\\\ash
sudo python3 scripts/cdp_dos.py -i eth0 -c 500
\\\
- Envía 500 paquetes
- Delay: 0.001s (default)
- MAC: 01:00:0c:cc:cc:cc (default)

**Ejemplo 2: Ataque moderado**
\\\ash
sudo python3 scripts/cdp_dos.py -i eth0 -c 5000 -d 0.0005
\\\
- Envía 5000 paquetes
- Delay: 0.0005s (más rápido)
- Duración aproximada: 2.5 segundos

**Ejemplo 3: Ataque intenso (máximo impacto)**
\\\ash
sudo python3 scripts/cdp_dos.py -i eth0 -c 10000 -d 0.0001
\\\
- Envía 10000 paquetes
- Delay: 0.0001s (muy rápido)
- Duración aproximada: 1 segundo
- Mayor impacto en CPU del switch

**Ejemplo 4: Ataque con MAC específica**
\\\ash
sudo python3 scripts/cdp_dos.py -i eth0 -m aa:bb:cc:dd:ee:ff -c 5000
\\\
- MAC destino personalizada
- Útil para targeting específico

---

##  Requisitos para Utilizar la Herramienta

### Requisitos de Hardware
- CPU: Mínimo 2 cores
- RAM: Mínimo 2GB
- Tarjeta de red compatible con modo promiscuo

### Requisitos de Software

| Software | Versión Mínima | Propósito |
|----------|----------------|-----------|
| Sistema Operativo | Kali Linux 2023+ / Ubuntu 20.04+ | SO base |
| Python | 3.8+ | Ejecución del script |
| Scapy | 2.5.0+ | Manipulación de paquetes |
| pip3 | 20.0+ | Gestor de paquetes Python |
| tcpdump | 4.9+ | Captura de tráfico |
| Wireshark | 3.0+ (opcional) | Análisis de capturas |

### Requisitos de Red
- Acceso a laboratorio de red (GNS3/PNETLab/EVE-NG)
- Switches Cisco con CDP habilitado
- Conectividad con VLAN 23 (red del atacante)
- Privilegios de administrador (root/sudo)

### Instalación de Dependencias
\\\ash
# Instalar Python y herramientas
sudo apt update
sudo apt install -y python3 python3-pip tcpdump

# Instalar librerías Python
pip3 install -r requirements.txt
\\\


---

##  Medidas de Mitigación

### 1. Deshabilitar CDP Globalmente  (Más Efectiva)

\\\cisco
Router(config)# no cdp run
\\\

**Efectividad:**  100%  
**Impacto:** Elimina completamente la vulnerabilidad  
**Desventaja:** Se pierde funcionalidad de descubrimiento CDP

---

### 2. Deshabilitar CDP por Interfaz

\\\cisco
Router(config)# interface Ethernet0/1
Router(config-if)# no cdp enable
Router(config-if)# exit
\\\

**Efectividad:**  100% en interfaz específica  
**Uso:** Para interfaces hacia redes no confiables

---

### 3. Port Security

\\\cisco
Switch(config)# interface Ethernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 3
Switch(config-if)# switchport port-security violation restrict
Switch(config-if)# switchport port-security mac-address sticky
\\\

**Efectividad:**  80-85%  
**Beneficio:** Limita cantidad de direcciones MAC por puerto

---

### 4. Storm Control

\\\cisco
Switch(config)# interface Ethernet0/1
Switch(config-if)# storm-control multicast level 50.00
Switch(config-if)# storm-control broadcast level 50.00
Switch(config-if)# storm-control action shutdown
\\\

**Efectividad:**  70-75%  
**Beneficio:** Protege contra flooding de tráfico multicast/broadcast

---

### 5. Usar LLDP en Lugar de CDP

\\\cisco
Router(config)# lldp run
Router(config)# no cdp run
\\\

**Efectividad:**  100%  
**Ventaja:** LLDP es estándar IEEE 802.1AB (más seguro que CDP)

---

### 6. Monitoreo y Alertas SNMP

\\\cisco
Router(config)# logging buffered 64000 informational
Router(config)# snmp-server enable traps cpu threshold
Router(config)# snmp-server enable traps memory bufferpeak
\\\

**Efectividad:**  Detecta pero no previene  
**Uso:** Para alertas tempranas de ataques

---

### Verificación de Mitigaciones

\\\cisco
! Verificar estado de CDP
show cdp

! Verificar configuración de interfaces
show cdp interface

! Verificar port security
show port-security interface Ethernet0/1

! Verificar storm control
show storm-control
\\\

---

##  Video Demostración

 **Enlace:** https://youtu.be/9zV7ts267l0



---

##  Advertencia Legal

**USO EXCLUSIVO PARA LABORATORIO EDUCATIVO DE ITLA**

