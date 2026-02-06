# Guía Rápida de Configuración

## MÁQUINA ATACANTE (10.21.23.2)

1. Copiar archivo al atacante:
```bash
scp configs/setup_attacker.sh user@10.21.23.2:/tmp/
```

2. En la máquina atacante ejecutar:
```bash
chmod +x /tmp/setup_attacker.sh
sudo /tmp/setup_attacker.sh
```

3. Verificar conectividad:
```bash
ping -c 4 192.168.100.1
ping -c 4 10.21.24.2
```

4. Ejecutar ataque:
```bash
sudo python3 scripts/cdp_dos.py -i eth0 -c 1000
```

---

## MÁQUINA VÍCTIMA (10.21.24.2)

1. Copiar archivo a la víctima:
```bash
scp configs/setup_victim.sh user@10.21.24.2:/tmp/
```

2. En la máquina víctima ejecutar:
```bash
chmod +x /tmp/setup_victim.sh
sudo /tmp/setup_victim.sh
```

3. Monitorear tráfico durante el ataque:
```bash
sudo tcpdump -i e0 ether dst 01:00:0c:cc:cc:cc
```
