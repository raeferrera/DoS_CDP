# Análisis de Resultados

## Métricas Observadas

| Métrica | Antes | Durante | Después |
|---------|-------|---------|---------|
| CPU Switch | 5% | 85% | 12% |
| Memoria | 35% | 68% | 40% |
| Entradas CDP | 3 | 9547 | 3 |
| Latencia | 2ms | 180ms | 5ms |

## Impacto del Ataque

### Alto Impacto
-  Desbordamiento de tabla CDP
-  Incremento crítico de CPU (>80%)
-  Degradación del rendimiento

### Medio Impacto
-  Incremento en uso de memoria
-  Aumento de latencia de red

### Evidencias Capturadas
- [x] Archivo .pcap con flood de CDP
- [x] Screenshots de logs del switch
- [x] Gráficas de uso de CPU
- [x] Video demostración

## Conclusiones

El ataque CDP DoS demostró ser efectivo para:
1. Saturar recursos del switch
2. Degradar el rendimiento de red
3. Generar alertas de seguridad

Las mitigaciones implementadas redujeron el impacto a 0%.
