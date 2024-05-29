import copy
import datetime
import pandas as pd
import networkx as nx
from HashTable import *

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def load_vertices(self, vertices_file):
        vertices_df = pd.read_csv(vertices_file)
        for idx, row in vertices_df.iterrows():
            self.graph.add_node(row['vertex_id'])

    def load_edges(self, edges_file):
        edges_df = pd.read_csv(edges_file)
        for idx, row in edges_df.iterrows():
            self.graph.add_edge(row['start_vertex'], row['end_vertex'], weight=row['edge_weight'])

    def get_distance(self, start_vertex, end_vertex):
        return self.graph.edges[start_vertex, end_vertex]['weight']

    def get_vertex(self, vertex_id):
        return self.graph.nodes[vertex_id]['vertex_id']


my_graph = Graph()
my_graph.load_vertices('WGUVertices.csv')
my_graph.load_edges('WGUEdges.csv')
for v in my_graph.graph.nodes:
    print(my_graph.graph.nodes[v]['vertex_id'])


def find_dropoff_vertex(packageID):
    package = myHash.search(packageID)
    for key in location_vertex_dict:
        if package.address == key:
            return location_vertex_dict[key]

def find_closest_vertex(start_vertex, package_list, g):
    distances = []
    for i, v in enumerate(g.adjacency_list):
        if not start_vertex.label == v.label:
            for packageID in package_list:
                corresponding_vertex = find_dropoff_vertex(packageID)
                if corresponding_vertex == int(v.label):
                    distances.append([v.distance, f"Vertex: {i + 1}"])
    sorted_distances = sorted(distances)

    return sorted_distances

def get_distance(graph, start_vertex, end_vertex):
    return graph[start_vertex][end_vertex]


location_vertex_dict = {
    "4001 South 700 East" : 1,
    "1060 Dalton Ave S" : 2,
    "1330 2100 S" : 3,
    "1488 4800 S" : 4,
    "177 W Price Ave" : 5,
    "195 W Oakland Ave" : 6,
    "2010 W 500 S" : 7,
    "2300 Parkway Blvd" : 8,
    "233 Canyon Rd" : 9,
    "2530 S 500 E" : 10,
    "2600 Taylorsville Blvd" : 11,
    "2835 Main St" : 12,
    "300 State St" : 13,
    "3060 Lester St" : 14,
    "3148 S 1100 W" : 15,
    "3365 S 900 W" : 16,
    "3575 W Valley Central Station Bus Loop" : 17,
    "3595 Main St" : 18,
    "380 W 2880 S" : 19,
    "410 S State St" : 20,
    "4300 S 1300 E" : 21,
    "4580 S 2300 E" : 22,
    "5025 State St" : 23,
    "5100 South 2700 West" : 24,
    "5383 South 900 East #104" : 25,
    "600 E 900 South" : 26,
    "6351 South 900 East" : 27
}