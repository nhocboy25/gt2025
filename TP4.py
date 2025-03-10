from heapq import heappush, heappop

def create_weighted_graph():
    n = 9
    matrix = [[0] * n for _ in range(n)]
    
    edges = [
        (1, 2, 4), (1, 5, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 7, 2), (6, 4, 5),
        (7, 8, 8), (7, 9, 2),
        (8, 9, 1)
    ]
    
    for u, v, w in edges:
        matrix[u-1][v-1] = w  
        matrix[v-1][u-1] = w  
        
    return matrix

def prims_algorithm(graph, root):
    n = len(graph)
    visited = [False] * n
    mst_edges = []
    total_weight = 0
    
    # queue to store (weight, current_vertex, parent)
    pq = [(0, root-1, None)] 
    while pq:
        weight, current, parent = heappop(pq)
        
        if visited[current]:
            continue
            
        visited[current] = True
        
        if parent is not None:  
            mst_edges.append((parent+1, current+1, weight))  
            total_weight += weight
        
        # Add edges to priority queue
        for next_vertex in range(n):
            if (graph[current][next_vertex] > 0 and 
                not visited[next_vertex]):
                heappush(pq, (graph[current][next_vertex], 
                             next_vertex, current))
    
    return mst_edges, total_weight

def find_set(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find_set(parent, parent[vertex])
    return parent[vertex]

def union_sets(parent, rank, vertex1, vertex2):
    root1 = find_set(parent, vertex1)
    root2 = find_set(parent, vertex2)
    
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskals_algorithm(graph):
    n = len(graph)
    edges = []
    # Collect all edges
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] > 0:
                edges.append((graph[i][j], i, j))
    edges.sort()
    
    # Initialize disjoint sets
    parent = list(range(n))
    rank = [0] * n
    
    mst_edges = []
    total_weight = 0
    
    for weight, u, v in edges:
        if find_set(parent, u) != find_set(parent, v):
            union_sets(parent, rank, u, v)
            mst_edges.append((u+1, v+1, weight)) 
            total_weight += weight
    
    return mst_edges, total_weight

graph = create_weighted_graph()
root = int(input("Enter root node (1-9): "))

# Prim's algorithm
print("\nPrim's Algorithm Results:")
prims_edges, prims_weight = prims_algorithm(graph, root)
print("MST Edges:", prims_edges)
print("Total Weight:", prims_weight)

# Kruskal's algorithm
print("\nKruskal's Algorithm Results:")
kruskals_edges, kruskals_weight = kruskals_algorithm(graph)
print("MST Edges:", kruskals_edges)
print("Total Weight:", kruskals_weight)