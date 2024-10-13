import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

from data import get_data


def dfs(graph, start, finish):
    visited = set()
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == finish:
                return path
            for neighbor in graph.neighbors(vertex):
                stack.append((neighbor, path + [neighbor]))
    return None

def bfs(graph, start, finish):
    visited = set()
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == finish:
                return path
            for neighbor in graph.neighbors(vertex):
                queue.append((neighbor, path + [neighbor]))
    return None

cities, edges = get_data()

G = nx.Graph()

G.add_edges_from(edges)

start_city = "Київ"
finish_city = "Осло"

dfs_path = dfs(G, start_city, finish_city)
bfs_path = bfs(G, start_city, finish_city)

print(f"(DFS): з : {" -> ".join(dfs_path)}")
print(f"(BFS): з : {" -> ".join(bfs_path)}")