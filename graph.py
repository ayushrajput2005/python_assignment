# ----------------- Graph Setup -----------------

# Locations
locations = ['A', 'B', 'C', 'D']
n = len(locations)  # number of nodes

# Adjacency Matrix for DFS
# 0 = A, 1 = B, 2 = C, 3 = D
adj_matrix = [
    [0, 1, 1, 0],  # A -> B, C
    [0, 0, 0, 1],  # B -> D
    [0, 0, 0, 1],  # C -> D
    [0, 0, 0, 0]   # D -> no outgoing edges
]

# Adjacency List for BFS
adj_list = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# ----------------- DFS using Adjacency Matrix -----------------
def dfs_matrix(start_index, visited):
    visited[start_index] = True
    print(locations[start_index], end=' ')
    for j in range(n):
        if adj_matrix[start_index][j] == 1 and not visited[j]:
            dfs_matrix(j, visited)

# ----------------- BFS using Adjacency List -----------------
from collections import deque

def bfs_list(start_node):
    visited = {node: False for node in adj_list}
    queue = deque()
    
    visited[start_node] = True
    queue.append(start_node)
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# ----------------- Main Program -----------------
print("DFS Traversal (Adjacency Matrix) starting from A:")
visited = [False] * n
dfs_matrix(0, visited)  # 0 corresponds to A
print("\n")

print("BFS Traversal (Adjacency List) starting from A:")
bfs_list('A')
print()
