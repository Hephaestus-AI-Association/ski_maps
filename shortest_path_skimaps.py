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

# we make sure that FIFO is respected ???????????
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


#Edo + Maria ester
#DIJSTRA AS A FUNCTION OF TIME

#function that returns the key corresponding to the minumum value of a dictionary
def min_value(Q):
  minimum_value = min(Q.values())
  minimum_keys = [key for key in Q if Q[key]==minimum_value]
  return(minimum_keys)


def shortest_path(source, time): 
  #create queue and initialize it to all values infinity
  Q = {}
  for key in nodes:
      Q[key] = float("inf")

  #init starting time
  Q[source] = time

  #create a dict of visited nodes
  prev = {}

  #main loop: dynamic implementation of Dijkstra
  while len(Q) > 0:   
    u = min_value(Q)[0]
    for v in G.neighbors(u):
      if v in Q:
        if Q[v] > G.edges[(u, v)]['arrival'][Q[u]]:
          Q[v] = G.edges[(u, v)]['arrival'][Q[u]]
          prev[v] = u
    del Q[u]

  print(prev)


shortest_path("B", 0)