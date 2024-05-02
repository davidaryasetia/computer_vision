class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.distances = {}

def dfs(node, visited, total_distance):
    visited.add(node)
    print(node.value, total_distance)
    for neighbor, distance in node.distances.items():
        if neighbor not in visited:
            dfs(neighbor, visited, total_distance + distance)

def bfs(node, visited, total_distance):
    queue = [(node, total_distance)]
    while queue:
        node, total_distance = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node.value, total_distance)
            for neighbor, distance in node.distances.items():
                if neighbor not in visited:
                    queue.append((neighbor, total_distance + distance))

# Buat node-node
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
Z = Node("Z")
E = Node("E")
F = Node("F")

# Hubungkan node-node dan tambahkan jarak
A.neighbors.append(B)
A.distances[B] = 5
A.neighbors.append(C)
A.distances[C] = 10
B.neighbors.append(D)
B.distances[D] = 15
B.neighbors.append(E)
B.distances[E] = 20
C.neighbors.append(F)
C.distances[F] = 25

# Jalankan DFS dan BFS
visited = set()
dfs(A, visited, 0)

visited = set()
bfs(A, visited, 0)
