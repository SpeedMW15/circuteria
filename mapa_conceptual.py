import matplotlib.pyplot as plt
import networkx as nx

# 1. Crear el mapa de conceptos para Circuitería E/S
G = nx.DiGraph()

# Definir las conexiones (Origen -> Destino)
conexiones = [
    ("Circuiteria E/S", "Modulos E/S"),
    ("Circuiteria E/S", "Metodos Transferencia"),
    ("Circuiteria E/S", "Buses del Sistema"),
    ("Modulos E/S", "Registros Datos/Estado"),
    ("Modulos E/S", "Logica de Control"),
    ("Metodos Transferencia", "E/S Programada"),
    ("Metodos Transferencia", "Interrupciones"),
    ("Metodos Transferencia", "DMA"),
    ("Buses del Sistema", "Bus Datos"),
    ("Buses del Sistema", "Bus Direcciones"),
    ("Buses del Sistema", "Bus Control"),
]

G.add_edges_from(conexiones)

# 2. Configurar el diseño visual
plt.figure(figsize=(12, 7))
pos = nx.spring_layout(G, seed=42)  # Mantiene las posiciones fijas

# Dibujar nodos, conexiones y texto
nx.draw_networkx_nodes(
    G, pos, node_size=3500, node_color="#4A90E2", node_shape="s"
)
nx.draw_networkx_edges(
    G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=2
)
nx.draw_networkx_labels(
    G, pos, font_size=9, font_color="white", font_weight="bold"
)

plt.title("Mapa Conceptual - Circuitería de Entrada/Salida (E/S)", fontsize=14)
plt.axis("off")  # Ocultar ejes de coordenadas
plt.tight_layout()

# 3. Mostrar la ventana emergente con el mapa conceptual
plt.show()