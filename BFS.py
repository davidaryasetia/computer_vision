from collections import defaultdict, deque

def bfs(graph, distances, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        # Dequeue a path from queue
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            # Iterate over each neighbor
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                # Update distances if the new path is shorter
                if distances[neighbor] > distances[node] + graph[node][neighbor]:
                    distances[neighbor] = distances[node] + graph[node][neighbor]

                # If neighbor is the end node, return the path
                if neighbor == end:
                    return new_path
            
            visited.add(node)

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

distances[start_node] = 0  # Distance from start node to itself is 0

# Run BFS and print the result
result = bfs(graph, distances, start_node, end_node)
if result:
    print(' - '.join(result))
    print("Total distance: ", distances[end_node])
else:
    print("No path available from {} to {}".format(start_node, end_node))