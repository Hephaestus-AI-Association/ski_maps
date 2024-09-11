# ski_maps
This is the implementation of a dynamic version of Dijkstra's algorithm, as described in our paper Ski Maps (soon available). Please refer to the paper for the motivation of this code and more information on the theory behind it.

## How to use the tool
If you want to try this out with your own data, replace the `ski_station.csv` file. The file is a table representing a a graph of the ski resort you want to apply the algorithm to. The format is table of edges in between vertices, with information about wether they are slopes or skilifts (which will tell us wether wait time should be considered or not), start vertex, end vertex and travel time/length.
