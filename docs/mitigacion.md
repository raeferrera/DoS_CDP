# Guía de Mitigación

## 1. Deshabilitar CDP

### Solución más efectiva
```cisco
! Globalmente
no cdp run

! Por interfaz
interface Ethernet0/1
 no cdp enable
```

## 2. Port Security
```cisco
interface Ethernet0/1
 switchport port-security
 switchport port-security maximum 3
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

## 3. Storm Control
```cisco
interface Ethernet0/1
 storm-control multicast level 50.00
 storm-control action shutdown
```

## 4. Usar LLDP
```cisco
! Habilitar LLDP (estándar IEEE)
lldp run

! Deshabilitar CDP
no cdp run
```

## 5. Monitoreo y Alertas
```cisco
! Configurar logging
logging buffered 64000 informational

! SNMP
snmp-server enable traps cpu threshold
```

## Verificación de Mitigaciones
```cisco
show cdp
show port-security
show storm-control
```
