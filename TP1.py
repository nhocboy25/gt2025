def path_exists(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if path_exists(graph, neighbor, end, visited):
                return True
    return False

graph = {
    1: [2],
    2: [1, 5],
    5: [2],
    3: [6],
    6: [3, 4, 7],
    4: [6, 7],
    7: [6, 4]
}

start_node = int(input("Enter the starting node: "))
end_node = int(input("Enter the ending node: "))

if path_exists(graph, start_node, end_node):
    print("True")
else:
    print("False")
