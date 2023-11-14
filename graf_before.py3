import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (2, 5), (2, 6), (6, 7), (7, 8), (7, 9), (7, 10)])  # добавляем вершины графа

pos = {1: (0, 0), 2: (0, 1), 3: (1, 2), 4: (2, 2), 5: (0,3), 6: (-1,2), 7: (-2,2), 8: (-3,3), 9: (-3,4), 10: (-3,5)}  # позиции вершин

node_color = ['orange' if node in [1, 2, 3, 6, 7] else 'beige' for node in G.nodes()]  # определяем цвета вершин

nx.draw(G, pos, node_color=node_color, with_labels=True)  # рисуем граф
plt.show()