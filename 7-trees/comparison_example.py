"""
Comparison of BFS vs DFS for File System Traversal

This example demonstrates the difference between Breadth-First Search (BFS) 
and Depth-First Search (DFS) when traversing a file system directory tree.
"""

from bfs_file_system import printnames_bfs
from dfs_file_system import printnames_dfs
import os

def create_sample_directory():
    """Create a sample directory structure for demonstration."""
    # Create directories
    os.makedirs("pics", exist_ok=True)
    os.makedirs("pics/nature", exist_ok=True)
    os.makedirs("pics/people", exist_ok=True)
    os.makedirs("pics/nature/mountains", exist_ok=True)
    os.makedirs("pics/nature/forests", exist_ok=True)
    os.makedirs("pics/people/family", exist_ok=True)
    
    # Create sample files
    sample_files = [
        "pics/photo1.jpg",
        "pics/photo2.jpg",
        "pics/nature/landscape.jpg",
        "pics/nature/mountains/peak.jpg",
        "pics/nature/mountains/valley.jpg",
        "pics/nature/forests/trees.jpg",
        "pics/people/portrait.jpg",
        "pics/people/family/group.jpg"
    ]
    
    for file_path in sample_files:
        with open(file_path, "w") as f:
            f.write(f"sample content for {file_path}")
    
    print("Sample directory structure created successfully!")
    print("Directory structure:")
    print("pics/")
    print("├── photo1.jpg")
    print("├── photo2.jpg")
    print("├── nature/")
    print("│   ├── landscape.jpg")
    print("│   ├── mountains/")
    print("│   │   ├── peak.jpg")
    print("│   │   └── valley.jpg")
    print("│   └── forests/")
    print("│       └── trees.jpg")
    print("└── people/")
    print("    ├── portrait.jpg")
    print("    └── family/")
    print("        └── group.jpg")
    print()

def main():
    print("=== BFS vs DFS File System Traversal Comparison ===\n")
    
    # Create sample directory if it doesn't exist
    if not os.path.exists("pics"):
        create_sample_directory()
    
    print("1. BREADTH-FIRST SEARCH (BFS) TRAVERSAL")
    print("=" * 50)
    print("BFS explores all files at the current level before going deeper.")
    print("It uses a queue to process directories level by level.\n")
    
    # Capture BFS output
    import io
    import sys
    
    # Redirect stdout to capture BFS output
    bfs_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = bfs_output
    
    printnames_bfs("pics")
    
    # Restore stdout and print captured output
    sys.stdout = original_stdout
    print(bfs_output.getvalue())
    
    print("\n" + "=" * 80 + "\n")
    
    print("2. DEPTH-FIRST SEARCH (DFS) TRAVERSAL")
    print("=" * 50)
    print("DFS explores as far as possible along each branch before backtracking.")
    print("It uses recursion to go deep into each directory first.\n")
    
    # Capture DFS output
    dfs_output = io.StringIO()
    sys.stdout = dfs_output
    
    printnames_dfs("pics")
    
    # Restore stdout and print captured output
    sys.stdout = original_stdout
    print(dfs_output.getvalue())
    
    print("\n" + "=" * 80 + "\n")
    
    print("3. KEY DIFFERENCES")
    print("=" * 50)
    print("• BFS explores level by level (breadth-first)")
    print("• DFS explores branch by branch (depth-first)")
    print("• BFS uses a queue data structure")
    print("• DFS uses recursion (stack-based)")
    print("• BFS is better for finding shortest paths")
    print("• DFS is better for exploring deep structures")
    print("• BFS uses more memory for wide trees")
    print("• DFS uses more memory for deep trees")

if __name__ == "__main__":
    main() 