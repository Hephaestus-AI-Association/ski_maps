import networkx as nx
import matplotlib.pyplot as plt

def draw_labeled_multigraph(G, attr_name, ax=None, curvedlist=None):
    # slightly modified version of: https://github.com/networkx/networkx/blob/04f99630605414199dc3efb9ab7b00ce619b0a08/examples/drawing/plot_multigraphs.py#L24
    """
    Length of connectionstyle must be at least that of a maximum number of edges
    between pair of nodes. This number is maximum one-sided connections
    for directed graph and maximum total connections for undirected graph.
    """
    straightconnection = 'arc3,rad=0.0'
    curvedconnection = 'arc3,rad=0.2'

    straightlist = [edge for edge in G.edges if edge not in curvedlist]

    # use spring layout to make the graph aesthetically pleasing
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=20, ax=ax)
    nx.draw_networkx_edges(
        G, pos, edgelist = curvedlist, edge_color="grey", connectionstyle=curvedconnection, ax=ax
    )
    nx.draw_networkx_edges(
        G, pos, edgelist = straightlist, edge_color="grey", connectionstyle=straightconnection, ax=ax
    )

    labels = {
        tuple(edge): attrs[attr_name]
        for *edge, attrs in G.edges(data=True)
    }

    nx.draw_networkx_edge_labels(
        G,
        pos,
        labels,
        connectionstyle=curvedconnection,
        label_pos=0.5,
        font_color="blue",
        bbox={"alpha": 0},
        ax=ax,
    )


# G = nx.MultiDiGraph()

# #add single edges with recpective weight (you can do it also by defining first a list and then creating a graph on that edge_list)
# G.add_edge("a", "b", weight=1, key=0)
# G.add_edge("b", "a", weight=2, key=1)
# G.add_edge("a", "c", weight=0.2)
# G.add_edge("c", "d", weight=0.1)
# G.add_edge("c", "e", weight=0.7)
# G.add_edge("e", "c", weight=0.9, key=1)
# G.add_edge("c", "f", weight=0.9)
# G.add_edge("a", "d", weight=0.3)

# mask = [edge[2] for edge in G.edges(keys=True)]
# edgelist = list(compress(G.edges(keys=True), mask))
# print(edgelist)

# print(list(G.edges(keys=True)))

# draw_labeled_multigraph(G, 'weight', curvedlist=edgelist)
# # plt.show()