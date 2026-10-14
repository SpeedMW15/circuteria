# Mapa Conceptual: Circuitería de Entrada/Salida (E/S)

Este repositorio contiene la estructura y documentación sobre los componentes y funcionamiento de la circuitería de Entrada/Salida en sistemas computacionales.

## Diagrama Conceptual

```mermaid
graph TD
    A[Circuitería de Entrada/Salida - E/S] --> B[Módulos / Controladores de E/S]
    A --> C[Métodos de Transferencia de Datos]
    A --> D[Buses del Sistema]

    %% Módulos de E/S
    B --> B1[Registro de Datos]
    B --> B2[Registro de Estado]
    B --> B3[Lógica de Control]
    B --> B4[Decodificación de Direcciones]

    %% Métodos de Transferencia
    C --> C1[E/S Programada]
    C --> C2[E/S por Interrupciones]
    C --> C3[Acceso Directo a Memoria - DMA]

    %% Buses
    D --> D1[Bus de Datos]
    D --> D2[Bus de Direcciones]
    D --> D3[Bus de Control]

    %% Estilos opcionales
    style A fill:#2b5c8f,color:#fff,stroke:#333,stroke-width:2px
    style B fill:#4a90e2,color:#fff
    style C fill:#4a90e2,color:#fff
    style D fill:#4a90e2,color:#fff
```

## Descripción de Componentes

1. **Módulos de E/S:** Interfaz entre la CPU/memoria y uno o más dispositivos periféricos.
2. **Métodos de Transferencia:**
   - **Programada:** La CPU espera activamente a que el dispositivo esté listo (Polling).
   - **Por Interrupciones:** El dispositivo avisa a la CPU cuando necesita atención.
   - **DMA (Direct Memory Access):** La transferencia ocurre directamente entre periférico y memoria sin pasar por la CPU.
3. **Buses:** Líneas físicas encargadas de transportar información, direcciones y señales de sincronización.