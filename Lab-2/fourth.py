#wap to check whether there exists a path with a given sequence of nodes, if yes, then find the length of the path

def check_path_list(adj_list, path):
    for i in range(len(path) - 1):
        if path[i + 1] not in adj_list[path[i]]:
            return False, 0
    return True, len(path) - 1

def check_path_matrix(matrix, path):
    for i in range(len(path) - 1):
        if matrix[path[i]][path[i + 1]] == 0:
            return False, 0
    return True, len(path) - 1

#adjacency list
v = int(input("Enter number of vertices: "))
adj_list = [[] for _ in range(v)]

e = int(input("Enter number of edges: "))
for _ in range(e):
    u = int(input("Enter first vertex: "))
    w = int(input("Enter second vertex: "))
    adj_list[u].append(w)
    adj_list[w].append(u)

n = int(input("Enter number of nodes in path: "))
path = [int(input(f"Enter node {i}: ")) for i in range(n)]

exists, length = check_path_list(adj_list, path)
print(f"Path exists (list): {exists}")
if exists:
    print(f"Path length: {length}")

#adjacency matrix
v = int(input("\nEnter number of vertices: "))
matrix = [[0] * v for _ in range(v)]

print("Enter adjacency matrix:")
for i in range(v):
    for j in range(v):
        matrix[i][j] = int(input(f"Element [{i}][{j}]: "))

n = int(input("Enter number of nodes in path: "))
path = [int(input(f"Enter node {i}: ")) for i in range(n)]

exists, length = check_path_matrix(matrix, path)
print(f"Path exists (matrix): {exists}")
if exists:
    print(f"Path length: {length}")
