INF = float("infinity")

# Use libraries like NetworkX
# Define graph as dictionary representing adjacency list.
# graph = {
#     "U": {"V": 6, "W": 7},
#     "V": {"U": 6, "X": 10},
#     "W": {"U": 7, "X": 1},
#     "X": {"W": 1, "V": 10}
# }
# [('U', 0), ('V', 6), ('W', 7), ('X', 8)]

graph = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "C": 5, "D": 2, "E": 2},
    "C": {"B": 5, "E": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "C": 5, "D": 1}
}
# [('A', 0), ('B', 3), ('C', 7), ('D', 1), ('E', 2)]


unvisited_min_distances = {vertex: INF for vertex in graph}
visited_vertices = {}

current_vertex = "A"  # The start node

unvisited_min_distances[current_vertex] = 0  # Distance from the start node

while len(unvisited_min_distances) > 0:
    # sorted is not efficient, use priority queue and dequeue the item with
    # lowest distance
    current_vertex, current_distance = sorted(unvisited_min_distances.items(),
                                              key=lambda x: x[1])[0]
    unvisited_min_distances.pop(current_vertex)
    visited_vertices[current_vertex] = current_distance
    for neighbor, distance in graph[current_vertex].items():
        if neighbor in unvisited_min_distances:
            new_distance = current_distance + distance
            if new_distance < unvisited_min_distances[neighbor]:
                unvisited_min_distances[neighbor] = new_distance


print(sorted(visited_vertices.items()))
