
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


def find_dropoff_vertex(packageID):
    package = myHash.search(packageID)
    for key in location_vertex_dict:
        if package.address[-1][0] == key:
            return location_vertex_dict[key]


def find_address_from_vertex(dictionary, vertex):
    # Return the first key (address) in dictionary that maps to 'value'
    # If value is not found, return None
    for key, value in dictionary.items():
        if value == int(vertex):
            return key
    return None


# Looks through the package_list to find any packages at current vertex.
# If package is found, return packageID
def find_package_by_vertex(vertex, package_list):
    for packageID in package_list:
        if find_dropoff_vertex(packageID) == vertex:
            # PRINT FOR DEBUGGING PURPOSES
            # print(f'Package {packageID} is going to Vertex {vertex}: {find_address_from_vertex(
            # location_vertex_dict, vertex)}')
            return packageID


# This function is a modification of the nearest neighbor algorithm. First it checks to see which packages have
# deadlines. Packages with deadlines are sorted by shortest distance and delivered first. Then the remaining packages
# are sorted and delivered.
def find_closest_vertex(start_vertex, package_list, g):
    distances = []
    priority_list = []
    vertices_list = list(g.vertices())
    for i, v in enumerate(vertices_list):

        for packageID in package_list:
            # Find the vertex that corresponds with the packageID
            corresponding_vertex = find_dropoff_vertex(packageID)
            if corresponding_vertex == vertices_list[i][0]:
                # Get the distance between the current vertex and the associated package vertex
                travel_distance = g.get_distance(start_vertex, corresponding_vertex)
                vertex = i + 1
                distances.append([travel_distance, vertex])
                # Check if there is a package to drop off at the current location
                if travel_distance == 0:
                    # Sort list by shortest distance
                    sorted_distances = sorted(distances)
                    return sorted_distances[0][1], sorted_distances[0][0]
                else:
                    # Check if package has deadline
                    package = myHash.search(packageID)
                    # If package has deadline, create a priority list of packages
                    if 'EOD' not in package.deadline[-1][0]:
                        priority_list.append([travel_distance, vertex])
                    # While there are packages with deadlines, deliver them first
                    while (priority_list):
                        # Sort list by shortest distance
                        sorted_priority_list = sorted(priority_list)
                        return sorted_priority_list[0][1], sorted_priority_list[0][0]

    # Sort list by shortest distance
    sorted_distances = sorted(distances)
    return sorted_distances[0][1], sorted_distances[0][0]


# This function allows you to view the remaining packages to be delivered.
# USEFUL FOR DEBUGGING
def view_remaining_vertex(start_vertex, package_list, g):
    distances = []
    priority_list = []
    vertices_list = list(g.vertices())
    for i, v in enumerate(vertices_list):

        for packageID in package_list:
            # Find the vertex that corresponds with the packageID
            corresponding_vertex = find_dropoff_vertex(packageID)
            if corresponding_vertex == vertices_list[i][0]:
                # Get the distance between the current vertex and the associated package vertex
                travel_distance = g.get_distance(start_vertex, corresponding_vertex)
                vertex = i + 1
                distances.append([travel_distance, f"Package: {packageID} to Vertex: {vertex}"])

    # Sort list by shortest distance
    sorted_distances = sorted(distances)
    return sorted_distances


location_vertex_dict = {
    "4001 South 700 East": 1,
    "1060 Dalton Ave S": 2,
    "1330 2100 S": 3,
    "1488 4800 S": 4,
    "177 W Price Ave": 5,
    "195 W Oakland Ave": 6,
    "2010 W 500 S": 7,
    "2300 Parkway Blvd": 8,
    "233 Canyon Rd": 9,
    "2530 S 500 E": 10,
    "2600 Taylorsville Blvd": 11,
    "2835 Main St": 12,
    "300 State St": 13,
    "3060 Lester St": 14,
    "3148 S 1100 W": 15,
    "3365 S 900 W": 16,
    "3575 W Valley Central Station Bus Loop": 17,
    "3595 Main St": 18,
    "380 W 2880 S": 19,
    "410 S State St": 20,
    "4300 S 1300 E": 21,
    "4580 S 2300 E": 22,
    "5025 State St": 23,
    "5100 South 2700 West": 24,
    "5383 South 900 East #104": 25,
    "600 E 900 South": 26,
    "6351 South 900 East": 27
}
