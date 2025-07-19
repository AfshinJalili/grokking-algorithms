# Chapter 9: Dijkstra's Algorithm

## Overview

Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a graph. It works by maintaining a set of unvisited nodes and iteratively selecting the node with the lowest cost, then updating the costs of its neighbors.

## Key Concepts

- **Graph**: A data structure consisting of nodes (vertices) connected by edges with weights
- **Cost**: The total weight/distance from the start node to a given node
- **Parents table**: Tracks the previous node in the shortest path to each node
- **Processed nodes**: Nodes that have been fully explored

## Algorithm Steps

1. Initialize costs table with infinity for all nodes except start (cost = 0)
2. Initialize parents table with None for all nodes
3. While there are unprocessed nodes:
   - Find the unprocessed node with the lowest cost
   - For each neighbor of this node:
     - Calculate new cost = current node cost + edge weight
     - If new cost < existing cost, update cost and parent
   - Mark current node as processed
4. Reconstruct the shortest path using the parents table

## Implementation Details

The implementation includes:

- **Graph representation**: Adjacency list with weighted edges
- **Costs table**: Tracks shortest known distance to each node
- **Parents table**: Tracks the previous node in the shortest path
- **Processed set**: Keeps track of fully explored nodes

## Example Graph

```
start --6--> a --1--> fin
  |          ^
  |          |
  2          3
  |          |
  +----> b --5--> fin
```

## Running the Code

```bash
python dijkstra.py
```

## Expected Output

The algorithm will find the shortest path from 'start' to 'fin' and display:
- Final costs table showing minimum distances
- Parents table showing the path reconstruction
- The actual shortest path: start → b → a → fin (total cost: 6)

## Time Complexity

- **Best/Average/Worst**: O(V²) where V is the number of vertices
- Can be optimized to O((V + E) log V) using a priority queue

## Space Complexity

- O(V) for storing costs, parents, and processed nodes

## Use Cases

- GPS navigation systems
- Network routing protocols
- Social network analysis
- Game AI pathfinding
- Transportation planning 