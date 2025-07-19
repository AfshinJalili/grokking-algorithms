import math

# Graph definition
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

# Costs table
infinity = math.inf
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

# Parents table
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

# Set of processed nodes
processed = set()

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Dijkstra's algorithm
def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs)

dijkstra()
# Log the final costs and parents tables, and print the shortest path from 'start' to 'fin'

import pprint

print("Final costs table:")
pprint.pprint(costs)

print("\nFinal parents table:")
pprint.pprint(parents)

# Reconstruct and log the shortest path from 'start' to 'fin'
def reconstruct_path(parents, end):
    path = []
    node = end
    while node:
        path.append(node)
        node = parents.get(node)
    path.reverse()
    return path

shortest_path = reconstruct_path(parents, "fin")
print("\nShortest path from 'start' to 'fin':")
print(" -> ".join(shortest_path))
