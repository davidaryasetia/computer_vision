from collections import defaultdict

def dfs(graph, distances, start, end, visited, path):
    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for neighbor, distance in graph[start].items():
        if neighbor not in visited:
            new_path = dfs(graph, distances, neighbor, end, visited, path.copy())
            if new_path:
                return new_path
    
    return None

# Function to input graph manually
def input_graph():
    graph = defaultdict(dict)

    while True:
        edge = input("Enter an edge (format: from_node to_node distance), or type 'done' to finish: ").split()
        if edge[0] == 'done':
            break
        from_node, to_node, distance = edge
        graph[from_node][to_node] = int(distance)
    
    return graph

# Input the graph manually
graph = input_graph()

# Collect all nodes in the graph
all_nodes = set(graph.keys())
for neighbors in graph.values():
    all_nodes.update(neighbors.keys())

# Initialize distances with infinity for all nodes
distances = {node: float('inf') for node in all_nodes}

# Input the start and end nodes
start_node = input("Enter the start node: ")
end_node = input("Enter the end node: ")

# Run DFS and print the result
visited = set()
path = dfs(graph, distances, start_node, end_node, visited, [])
if path:
    print(' - '.join(path))
    print("Total distance: ", sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)))
else:
    print("No path available from {} to {}".format(start_node, end_node))