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
            self.graph.add_edge(int(row['start_vertex']), int(row['end_vertex']), weight=row['edge_weight'])

    def get_distance(self, start_vertex, end_vertex):
        return self.graph.edges[start_vertex, end_vertex]['weight']

    def vertices(self):
        return self.graph.nodes(data=True)

    def edges(self):
        return self.graph.edges(data=True)

    def count_vertices(self):
        """Return the number of vertices in the graph."""
        return self.graph.number_of_nodes()

my_graph = Graph()
my_graph.load_vertices('WGUVertices.csv')
my_graph.load_edges('WGUEdges.csv')

print(my_graph.get_distance(1,7))
# vertices_list = list(my_graph.vertices())
#
# print(my_graph.count_vertices())

# for i, v in enumerate(vertices_list):
#     print(vertices_list[i][0])

def find_dropoff_vertex(packageID):
    package = myHash.search(packageID)
    for key in location_vertex_dict:
        if package.address == key:
            return location_vertex_dict[key]

def find_closest_vertex(start_vertex, package_list, g):
    distances = []
    vertices_list = list(g.vertices())
    for i, v in enumerate(vertices_list):
        # if start_vertex != vertices_list[i][0]:
        for packageID in package_list:
            corresponding_vertex = find_dropoff_vertex(packageID)
            if corresponding_vertex == vertices_list[i][0]:
                travel_distance = g.get_distance(start_vertex, corresponding_vertex)
                vertex = i + 1
                distances.append([travel_distance, vertex])
    sorted_distances = sorted(distances)

    return sorted_distances[0][1], sorted_distances[0][0]

def view_remaining_vertex(start_vertex, package_list, g):
    distances = []
    vertices_list = list(g.vertices())
    for i, v in enumerate(vertices_list):
        # if start_vertex != vertices_list[i][0]:
        for packageID in package_list:
            corresponding_vertex = find_dropoff_vertex(packageID)
            if corresponding_vertex == vertices_list[i][0]:
                travel_distance = g.get_distance(start_vertex, corresponding_vertex)
                vertex = i + 1
                distances.append([travel_distance, f"Package: {packageID} to Vertex: {vertex}  "])
    sorted_distances = sorted(distances)

    return sorted_distances

def find_address_from_vertex(dictionary, vertex):
    # Return the first key (address) in dictionary that maps to 'value'
    # If value is not found, return None
    for key, value in dictionary.items():
        if value == int(vertex):
            return key
    return None

def find_package_by_vertex(vertex, package_list):
    for packageID in package_list:
        if find_dropoff_vertex(packageID) == vertex:
            print(f'Package {packageID} is going to Vertex {vertex}: {find_address_from_vertex(location_vertex_dict, vertex)}')
            return packageID



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