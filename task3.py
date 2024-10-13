import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge('Київ', 'Афіни', weight=2401)
G.add_edge('Київ', 'Стамбул', weight=1831)
G.add_edge('Афіни', 'Стамбул', weight=1205)
G.add_edge('Лондон', 'Осло', weight=1741)
G.add_edge('Лондон', 'Стамбул', weight=3100)
G.add_edge('Київ', 'Париж', weight=2485)
G.add_edge('Париж', 'Рим', weight=1437)
G.add_edge('Лондон', 'Париж', weight=465)

pos = nx.spring_layout(G, seed=45)
plt.figure(figsize=(7, 7))

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, width=3)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

start = 'Київ'
finish = 'Осло'

path = nx.dijkstra_path(G, start, finish)
length = nx.dijkstra_path_length(G, start, finish)

print(f"Оптимальний шлях ({length}):\n {" -> ".join(path)}")