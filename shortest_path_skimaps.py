from function_to_weights import import_station, create_graph
from draw_wg import draw_labeled_multigraph
import random
import networkx as nx
import matplotlib.pyplot as plt

def model(node, t):
    # returns the wait time at a station given the time (in our case, random)
    return random.randint(0, 30)

filename = 'ski_station.csv'
nodes, edges, skilifts, slopes = import_station(filename)
G = create_graph(filename, model)

draw_labeled_multigraph(G, 'weight', curvedlist = skilifts)
plt.show()

#function that returns the key corresponding to the minumum value of a dictionary
def min_value(Q):
  """
  Find the minimum value(s) in a dictionary and return the corresponding key(s).

  Parameters:
  Q (dict): A dictionary containing key-value pairs.

  Returns:
  list: A list of keys that have the minimum value in the dictionary.
  """
  minimum_value = min(Q.values())
  minimum_keys = [key for key in Q if Q[key] == minimum_value]
  return minimum_keys



def shortest_path(source, time, G): 
  """
  Finds the shortest path from a given source node to all other nodes in a graph.

  Args:
    source (node): The source node from which to find the shortest paths.
    time (float): The starting time for the shortest paths.
    G (graph): The graph in which to find the shortest paths.

  Returns:
    dict: A dictionary containing the previous node in the shortest path for each node.
  """
  # create queue and initialize it to all values infinity
  Q = {}
  for key in G.nodes:
    Q[key] = float("inf")

  # init starting time
  Q[source] = time

  # create a dict of visited nodes
  prev = {}

  # main loop: dynamic implementation of Dijkstra's algorithm
  while len(Q) > 0:   
    u = min_value(Q)[0]
    for v in G.neighbors(u):
      if v in Q:
        if Q[v] > G.edges[(u, v)]['arrival'][Q[u]]:
          Q[v] = G.edges[(u, v)]['arrival'][Q[u]]
          prev[v] = u
    del Q[u]

  return prev

print(shortest_path("B", 100, G))
