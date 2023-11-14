import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (2, 5), (2, 6), (6, 7), (7, 8), (7, 9), (7, 10)])  # добавляем вершины графа

pos = {1: (0, 0), 2: (0, 1), 3: (1, 2), 4: (2, 2), 5: (0,3), 6: (-1,2), 7: (-2,2), 8: (-3,3), 9: (-3,4), 10: (-3,5)}  # позиции вершин

node_color = ['orange' if node in [1, 2, 3, 6, 7] else 'beige' for node in G.nodes()]  # определяем цвета вершин

def remove_nodes_with_two_branches(graph):
    nodes_to_remove = [node for node in graph.nodes if graph.degree[node] == 2]
    graph.remove_nodes_from(nodes_to_remove)

remove_nodes_with_two_branches(G)
pos = {node: pos[node] for node in G.nodes}  # обновляем позиции вершин
G.add_edge(7, 2)
G.add_edge(4, 2)

node_color = ['orange' if node in [1, 2, 3, 6, 7] else 'beige' for node in G.nodes()]  # обновляем цвета вершин
nx.draw(G, pos, node_color=node_color, with_labels=True)  # рисуем обновленный граф
plt.show()