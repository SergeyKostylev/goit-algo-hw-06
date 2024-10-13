import networkx as nx
import matplotlib.pyplot as plt

from data import get_data

cities, edges = get_data()

G = nx.Graph()
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='green', node_size=3000)
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Вершини :")
for node in G.nodes():
    print(f"{node:>{10}} - {G.degree(node)}")
