from os import listdir
from os.path import isfile, join

def printnames_dfs(dir_path, depth=0):
    """
    Print all file names in a directory tree using Depth-First Search.
    
    Args:
        dir_path (str): The directory path to traverse
        depth (int): Current depth level for indentation (used internally)
    """
    indent = "  " * depth
    
    if depth == 0:
        print(f"DFS traversal starting from: {dir_path}")
        print("-" * 40)
    
    print(f"{indent}Exploring directory: {dir_path}")
    
    for file in sorted(listdir(dir_path)):
        fullpath = join(dir_path, file)
        if isfile(fullpath):
            print(f"{indent}  File: {file}")
        else:
            print(f"{indent}  Directory: {file} (recursing)")
            printnames_dfs(fullpath, depth + 1)

if __name__ == "__main__":
    # Example usage
    print("=== Depth-First Search File System Traversal ===\n")
    
    # You can change this to any directory path
    start_directory = "pics"
    
    try:
        printnames_dfs(start_directory)
    except FileNotFoundError:
        print(f"Directory '{start_directory}' not found. Please create it or change the path.")
        print("Creating a sample directory structure for demonstration...")
        
        # Create a sample directory structure for demonstration
        import os
        os.makedirs("pics", exist_ok=True)
        os.makedirs("pics/nature", exist_ok=True)
        os.makedirs("pics/people", exist_ok=True)
        os.makedirs("pics/nature/mountains", exist_ok=True)
        
        # Create some sample files
        with open("pics/photo1.jpg", "w") as f:
            f.write("sample photo 1")
        with open("pics/photo2.jpg", "w") as f:
            f.write("sample photo 2")
        with open("pics/nature/landscape.jpg", "w") as f:
            f.write("landscape photo")
        with open("pics/nature/mountains/peak.jpg", "w") as f:
            f.write("mountain peak photo")
        with open("pics/people/portrait.jpg", "w") as f:
            f.write("portrait photo")
        
        print("Sample directory created. Running DFS traversal:\n")
        printnames_dfs(start_directory) 