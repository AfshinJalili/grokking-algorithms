from os import listdir
from os.path import isfile, join
from collections import deque

def printnames_bfs(start_dir):
    """
    Print all file names in a directory tree using Breadth-First Search.
    
    Args:
        start_dir (str): The starting directory path to traverse
    """
    search_queue = deque()
    search_queue.append(start_dir)
    
    print(f"BFS traversal starting from: {start_dir}")
    print("-" * 40)
    
    while search_queue:
        current_dir = search_queue.popleft()
        print(f"Exploring directory: {current_dir}")
        
        for file in sorted(listdir(current_dir)):
            fullpath = join(current_dir, file)
            if isfile(fullpath):
                print(f"  File: {file}")
            else:
                print(f"  Directory: {file} (added to queue)")
                search_queue.append(fullpath)
        print()

if __name__ == "__main__":
    # Example usage
    print("=== Breadth-First Search File System Traversal ===\n")
    
    # You can change this to any directory path
    start_directory = "pics"
    
    try:
        printnames_bfs(start_directory)
    except FileNotFoundError:
        print(f"Directory '{start_directory}' not found. Please create it or change the path.")
        print("Creating a sample directory structure for demonstration...")
        
        # Create a sample directory structure for demonstration
        import os
        os.makedirs("pics", exist_ok=True)
        os.makedirs("pics/nature", exist_ok=True)
        os.makedirs("pics/people", exist_ok=True)
        
        # Create some sample files
        with open("pics/photo1.jpg", "w") as f:
            f.write("sample photo 1")
        with open("pics/photo2.jpg", "w") as f:
            f.write("sample photo 2")
        with open("pics/nature/landscape.jpg", "w") as f:
            f.write("landscape photo")
        with open("pics/people/portrait.jpg", "w") as f:
            f.write("portrait photo")
        
        print("Sample directory created. Running BFS traversal:\n")
        printnames_bfs(start_directory) 