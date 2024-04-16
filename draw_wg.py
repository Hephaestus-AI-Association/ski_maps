import networkx as nx
import matplotlib.pyplot as plt
import math as m 

def draw():
    #create a graph, can be either directed or undirected
    G = nx.DiGraph()
    
    

    #add single edges with recpective weight (you can do it also by defining first a list and then creating a graph on that edge_list)
    G.add_edge("a", "b", arrival = float('inf'))
    G.add_edge("a", "c", arrival = float('inf'))
    G.add_edge("c", "d", arrival = float('inf'))
    G.add_edge("c", "e", arrival = float('inf'))
    G.add_edge("c", "f", arrival = float('inf'))
    G.add_edge("a", "d", arrival = float('inf'))

    start = "a"
    start_time = 0

    #set node attributes = arrival times
    nx.set_node_attributes(G, float('inf'), 'arrival_time')

    #print(G.nodes['a']['arrival_time'])

    #init queue
    Q = set(G.nodes)

    #init start
    G.nodes[start]['arrival_time'] = start_time

    print(G.nodes[start]['arrival_time'])


    #while len(Q)!=0:

        
        
    




    #create an edge list, an array with the edges that wil be used in the drawing as an argument
    edge_list = [(u, v) for (u, v) in G.edges()] 

    #create a dictionary with edge weights associated to the respective edge (the key)
    edge_labels = nx.get_edge_attributes(G, "arrival") 

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


