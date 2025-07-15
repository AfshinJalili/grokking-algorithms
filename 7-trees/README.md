# Chapter 7: Trees

This chapter explores tree data structures and demonstrates how to traverse them using both Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms, applied to file system traversal.

## 📚 Algorithms Implemented

### Breadth-First Search File System Traversal (`bfs_file_system.py`)
- **Purpose**: Traverse a directory tree level by level, exploring all files at the current depth before going deeper
- **Time Complexity**: O(V + E) where V is the number of directories and E is the number of files
- **Space Complexity**: O(W) where W is the maximum width of the tree
- **Data Structure**: Queue (deque)

### Depth-First Search File System Traversal (`dfs_file_system.py`)
- **Purpose**: Traverse a directory tree by exploring each branch completely before backtracking
- **Time Complexity**: O(V + E) where V is the number of directories and E is the number of files
- **Space Complexity**: O(H) where H is the maximum height of the tree
- **Data Structure**: Recursion (implicit stack)

### Comparison Example (`comparison_example.py`)
- **Purpose**: Demonstrates the differences between BFS and DFS approaches side by side
- **Features**: Creates sample directory structure and shows traversal order differences

## 🎯 Key Concepts from Chapter 7

### What are Trees?
A tree is a hierarchical data structure consisting of nodes connected by edges. In the context of file systems:
- **Nodes**: Directories and files
- **Edges**: Parent-child relationships
- **Root**: The starting directory
- **Leaves**: Files (nodes with no children)

### BFS vs DFS for File System Traversal

**Breadth-First Search (BFS):**
- Explores all files at the current level before going deeper
- Uses a queue to process directories level by level
- Better for finding files that are close to the root
- More memory usage for wide directory structures

**Depth-First Search (DFS):**
- Explores as far as possible along each branch before backtracking
- Uses recursion (implicit stack) to go deep into each directory first
- Better for exploring deep directory structures
- More memory usage for deep directory structures

### Example Directory Structure
```
pics/
├── photo1.jpg
├── photo2.jpg
├── nature/
│   ├── landscape.jpg
│   ├── mountains/
│   │   ├── peak.jpg
│   │   └── valley.jpg
│   └── forests/
│       └── trees.jpg
└── people/
    ├── portrait.jpg
    └── family/
        └── group.jpg
```

**BFS Traversal Order:**
1. pics/photo1.jpg, pics/photo2.jpg, pics/nature/, pics/people/
2. pics/nature/landscape.jpg, pics/nature/mountains/, pics/nature/forests/
3. pics/people/portrait.jpg, pics/people/family/
4. pics/nature/mountains/peak.jpg, pics/nature/mountains/valley.jpg
5. pics/nature/forests/trees.jpg
6. pics/people/family/group.jpg

**DFS Traversal Order:**
1. pics/photo1.jpg, pics/photo2.jpg, pics/nature/landscape.jpg
2. pics/nature/mountains/peak.jpg, pics/nature/mountains/valley.jpg
3. pics/nature/forests/trees.jpg
4. pics/people/portrait.jpg, pics/people/family/group.jpg

## 🚀 Running the Examples

### Run BFS File System Traversal:
```bash
python3 7-trees/bfs_file_system.py
```

### Run DFS File System Traversal:
```bash
python3 7-trees/dfs_file_system.py
```

### Run Comparison Example:
```bash
python3 7-trees/comparison_example.py
```

### Run All Examples:
```bash
# Run BFS
python3 7-trees/bfs_file_system.py
echo -e "\n" && echo "="*50 && echo -e "\n"
# Run DFS
python3 7-trees/dfs_file_system.py
echo -e "\n" && echo "="*50 && echo -e "\n"
# Run comparison
python3 7-trees/comparison_example.py
```

## 📖 Learning Notes

- **Tree Traversal**: Both BFS and DFS are fundamental algorithms for exploring tree structures
- **File System as Tree**: Directory structures naturally form tree hierarchies
- **Memory Considerations**: BFS uses more memory for wide trees, DFS for deep trees
- **Use Cases**: 
  - BFS: Finding files near the root, level-by-level processing
  - DFS: Exploring deep directory structures, recursive file operations
- **Implementation**: BFS uses a queue, DFS uses recursion (stack)

## 🔗 Related Resources

- [Tree Data Structure](https://en.wikipedia.org/wiki/Tree_(data_structure)) - Theory and applications
- [BFS vs DFS Visualization](https://visualgo.net/en/dfsbfs) - Interactive comparison
- [File System Traversal](https://docs.python.org/3/library/os.html) - Python os module documentation 