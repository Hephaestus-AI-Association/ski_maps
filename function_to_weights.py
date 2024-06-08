import csv
import matplotlib.pyplot as plt
import networkx as nx

# open the csv file with the ski station data
def import_station(filename):
    """
    Imports ski station data from a CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing the following elements:
            - nodes (list): A list of unique node names.
            - edges (list): A list of edges, where each edge is represented as a tuple.
            - skilifts (list): A list of skilifts, where each skilift is represented as a tuple.
            - slopes (list): A list of slopes, where each slope is represented as a tuple.
    """
    data = None
    skilifts = []
    slopes = []
    with open(filename) as f:
        data = csv.reader(f, delimiter=';')
        lines = [line for line in data][1:]
        nodes = sorted(set([line[1].strip() for line in lines] + [line[2].strip() for line in lines]))
        for line in lines:
            if line[0].strip().lower() == 'skilift':
                skilifts.append((line[1].strip(), line[2].strip(), int(line[3].strip())))
            else:
                slopes.append((line[1].strip(), line[2].strip(), int(line[3].strip())))
        edges = skilifts + slopes
    return nodes, edges, skilifts, slopes




def create_graph(filename, model):
    """
    Create a directed graph representing a ski station.

    Parameters:
    - filename (str): The path to the file containing the ski station data.
    - model (function): A function that calculates the wait time at a node based on the node and time.

    Returns:
    - G (networkx.DiGraph): The directed graph representing the ski station.

    """
    nodes, edges, skilifts, slopes = import_station(filename)

    # initialize the directed graph of the ski station
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    
    # add wait times to the nodes, based on the model
    times = range(0, 1440)
    # we make sure that FIFO is respected
    for node in nodes:
        for t in times:
            if t == 0:
                G.nodes[node][t] = model(node, t)
            else:
                G.nodes[node][t] = max(model(node, t), G.nodes[node][t-1]-1)
    
    # for each skilift, compute the arrival time at the destination node based on the starting time (by adding up time, skilift length and wait time at the station)
    for edge in skilifts:
        if isinstance(G.edges[edge[:2]]['weight'], int):
            G.edges[edge[:2]]['arrival'] = [G.nodes[edge[0]][t] + G.edges[edge[:2]]['weight'] + t for t in times]
        else:
            update = [min(G.nodes[edge[0]][t] + G.edges[edge[:2]]['weight'] + t, G.edges[edge[:2]]['weight'][t]) for t in times]
            G.edges[edge[:2]]['arrival'] = update
    
    # for each slope, compute the arrival time at the destination node based on the starting time (by simply adding up time and slope length)
    for edge in slopes:
        if isinstance(G.edges[edge[:2]]['weight'], int):
            G.edges[edge[:2]]['arrival'] = [G.nodes[edge[0]][t] + G.edges[edge[:2]]['weight'] + t for t in times]
        else:
            update = [min(G.nodes[edge[0]][t] + G.edges[edge[:2]]['weight'] + t, G.edges[edge[:2]]['weight'][t]) for t in times]
            G.edges[edge[:2]]['arrival'] = update

    return G

