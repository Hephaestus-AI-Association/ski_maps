from function_to_weights import create_graph
from draw_wg import draw
import random
import networkx as nx

def model(node, t):
    # returns the wait time at a station given the time (in our case, random)
    return random.randint(0, 30)

G = create_graph('ski_station.csv', model)

draw(G)

#Edo + Maria ester
#DIJSTRA AS A FUNCTION OF TIME

#function that returns the key corresponding to the minumum value of a dictionary
def min_value(Q):
  minimum_value = min(Q.values())
  minimum_keys = [key for key in Q if Q[key]==minimum_value]
  return(minimum_keys)


def shortest_path(source, time, G): 
  #create queue and initialize it to all values infinity
  Q = {}
  for key in G.nodes:
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


print(shortest_path("B", 10, G))