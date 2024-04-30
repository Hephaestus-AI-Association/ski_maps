import networkx as nx
import matplotlib.pyplot as plt
import math as m 
import itertools as it

def draw(G):
    #create an edge list, an array with the edges that wil be used in the drawing as an argument
    edge_list = [(u, v) for (u, v) in G.edges()] 

    #create a dictionary with edge weights associated to the respective edge (the key)
    edge_labels = nx.get_edge_attributes(G, "weight")

    #define a position for all nodes, required arugment in draw_ntwrkx_nodes
    pos = nx.planar_layout(G)

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

def draw_labeled_multigraph(G, attr_name, ax=None):
    """
    Length of connectionstyle must be at least that of a maximum number of edges
    between pair of nodes. This number is maximum one-sided connections
    for directed graph and maximum total connections for undirected graph.
    """
    # Works with arc3 and angle3 connectionstyles
    connectionstyle = [f"arc3,rad={r}" for r in it.accumulate([0.15] * 4)]
    # connectionstyle = [f"angle3,angleA={r}" for r in it.accumulate([30] * 4)]

    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=20, ax=ax)
    nx.draw_networkx_edges(
        G, pos, edge_color="grey", connectionstyle=connectionstyle, ax=ax
    )

    labels = {
        tuple(edge): f"{attr_name}={attrs[attr_name]}"
        for *edge, attrs in G.edges(data=True)
    }
    nx.draw_networkx_edge_labels(
        G,
        pos,
        labels,
        connectionstyle=connectionstyle,
        label_pos=0.3,
        font_color="blue",
        bbox={"alpha": 0},
        ax=ax,
    )


G = nx.Graph()

#add single edges with recpective weight (you can do it also by defining first a list and then creating a graph on that edge_list)
G.add_edge("a", "b", weight=1)
G.add_edge("b", "a", weight=2)
G.add_edge("a", "c", weight=0.2)
G.add_edge("c", "d", weight=0.1)
G.add_edge("c", "e", weight=0.7)
G.add_edge("c", "f", weight=0.9)
G.add_edge("a", "d", weight=0.3)

draw_labeled_multigraph(G, 'weight')
#plt.show()