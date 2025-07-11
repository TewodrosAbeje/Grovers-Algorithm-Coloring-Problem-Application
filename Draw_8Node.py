import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random



G=nx.Graph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")
G.add_node("G")
G.add_node("H")

G.add_edge("G", "A")
G.add_edge("G", "D")
G.add_edge("D", "E")
G.add_edge("A", "H")
G.add_edge("A", "F")
G.add_edge("E", "F")
G.add_edge("H", "F")
G.add_edge("C", "F")
G.add_edge("B", "F")
G.add_edge("C", "B")
G.add_edge("B", "D")
G.add_edge("C", "B")
G.add_edge("B", "E")
G.add_edge("A", "E")
G.add_edge("G", "H")
pos={
    "A": (0.5, 1.55),
    "B": (1, 0),
    "C": (2, 1),
    "D": (0, 1),
    "E": (0.5, 1),
    "F": (1, 1),
    "G": (0, 1.55),
    "H": (0.5, 2)
}


nx.draw(G,pos=pos, node_color='Black',with_labels=True, node_size=500, font_color='white', font_size=16)
plt.show()