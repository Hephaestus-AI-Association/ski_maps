import networkx as nx
import matplotlib.pyplot as plt

#create a graph, can be either directed or undirected
G = nx.Graph()
l= input()

#add single edges with recpective weight (you can do it also by defining first a list and then creating a graph on that edge_list)
G.add_edge("a", "b", weight=l)
G.add_edge("a", "c", weight=0.2)
G.add_edge("c", "d", weight=0.1)
G.add_edge("c", "e", weight=0.7)
G.add_edge("c", "f", weight=0.9)
G.add_edge("a", "d", weight=0.3)

#create an edge list, an array with the edges that wil be used in the drawing as an argument
edge_list = [(u, v) for (u, v) in G.edges()] 

#create a dictionary with edge weights associated to the respective edge (the key)
edge_labels = nx.get_edge_attributes(G, "weight") 

#define a position for all nodes, required arugment in draw_ntwrkx_nodes
pos = nx.spring_layout(G, seed=7)

#draw the nodes
nx.draw_networkx_nodes(G, pos) 

#add nodes' label to the graph
nx.draw_networkx_labels(G, pos)

#draw the edges
nx.draw_networkx_edges(G, pos, edge_list) 

#draw the labels
nx.draw_networkx_edge_labels(G, pos, edge_labels)

#display the result
plt.show()
