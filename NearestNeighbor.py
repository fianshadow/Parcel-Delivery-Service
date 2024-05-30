import numpy as np
from Graph import *

def nearest_neighbor(graph):
    num_nodes = graph.count_vertices()
    visited = [False] * num_nodes
    tour = []

    # Start from node 1
    current_node = 1
    tour.append(current_node)
    visited[current_node] = True

    # Visit each node
    for _ in range(num_nodes - 1):
        min_distance = float('inf')
        nearest_node = None

        # Find the nearest unvisited neighbor
        for neighbor in graph.adjacency_list:
            if not visited[neighbor] and graph[current_node][neighbor] < min_distance:
                min_distance = graph[current_node][neighbor]
                nearest_node = neighbor

        # Move to the nearest unvisited neighbor
        tour.append(nearest_node)
        visited[nearest_node] = True
        current_node = nearest_node

    # Return to the starting node to complete the tour
    tour.append(0)

    return tour

# Find the tour using nearest neighbor algorithm
