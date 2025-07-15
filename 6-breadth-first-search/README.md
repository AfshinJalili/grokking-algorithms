# Chapter 6: Breadth-First Search

This chapter introduces the Breadth-First Search (BFS) algorithm, a fundamental graph traversal technique used to explore nodes and edges of a graph in the shortest-path order.

## 📚 Algorithms Implemented

### Breadth-First Search (`bfs.py`)
- **Purpose**: Find the shortest path (fewest edges) between nodes in an unweighted graph, or search for a node with a specific property
- **Time Complexity**: O(V + E) (V = number of vertices, E = number of edges)
- **Space Complexity**: O(V)
- **Usage**:
```python
from bfs import bfs, graph
bfs(graph, "you")
```

## 🎯 Key Concepts from Chapter 6

### What is Breadth-First Search?
Breadth-First Search is an algorithm for traversing or searching tree or graph data structures. It starts at a selected node (the "root") and explores all its neighbors at the present depth before moving on to nodes at the next depth level.

### How BFS Works
1. Start at the root node and add it to a queue
2. Remove the first node from the queue
3. For each unvisited neighbor, add it to the queue
4. Mark nodes as visited to avoid cycles
5. Repeat until the queue is empty or the goal is found

**Example graph:**
- "you" → ["alice", "bob", "claire"]
- "bob" → ["anuj", "peggy"]
- "alice" → ["peggy"]
- "claire" → ["thom", "jonny"]

**Sample run:**
- The algorithm searches for a person whose name ends with 'm' (a "mango seller")
- Output: `thom is a mango seller!`

### Time Complexity Analysis
- **Best/Average/Worst Case**: O(V + E) - Every node and edge is explored at most once
- **Space Complexity**: O(V) - For the queue and visited set

### Why Breadth-First Search?
**Advantages:**
- Finds the shortest path in unweighted graphs
- Simple and easy to implement
- Guarantees the shortest solution if one exists

**Disadvantages:**
- Can be memory-intensive for large graphs
- Not suitable for weighted graphs (use Dijkstra's algorithm instead)

## 🚀 Running the Example

```bash
# Run the BFS example
python3 6-breadth-first-search/bfs.py
```

## 📖 Learning Notes

- BFS is a foundational algorithm for many real-world problems (shortest path, social networks, web crawlers)
- The queue data structure is essential for BFS
- Marking nodes as visited prevents infinite loops in cyclic graphs
- BFS is the basis for more advanced algorithms like Dijkstra's and A*

## 🔗 Related Resources

- [Breadth-First Search Visualization](https://visualgo.net/en/dfsbfs) - Interactive BFS visualization
- [BFS on Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search) - Theory and applications 