import random
import networkx as nx
import csv
import matplotlib.pyplot as plt

# open the csv file with the ski station data
data = None
skilifts = []
slopes = []
with open('ski_station.csv') as f:
    data = csv.reader(f, delimiter=';')
    lines = [line for line in data][1:]
    nodes = sorted(set([line[1].strip() for line in lines] + [line[2].strip() for line in lines]))
    for line in lines:
        if line[0].strip().lower() == 'skilift':
            skilifts.append((line[1].strip(), line[2].strip(), int(line[3].strip())))
        else:
            slopes.append((line[1].strip(), line[2].strip(), int(line[3].strip())))
    edges = skilifts + slopes
    

# initialize the directed graph of the ski station
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# add wait times to the nodes, based on the model
times = range(0, 1440)
def model(node, t):
    # returns the wait time at a station given the time (in our case, random)
    return random.randint(0, 30)

for t in times:
    for node in nodes:
        G.nodes[node][t] = model(node, t)

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
