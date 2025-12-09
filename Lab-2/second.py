#wap to check if 2 nodes are directly connected or not

def is_connected_matrix(matrix, u, v):
    return matrix[u][v] == 1

def is_connected_list(adj_list, u, v):
    return v in adj_list[u]

#adjacency list
v = int(input("Enter number of vertices: "))
adj_list = [[] for _ in range(v)]

e = int(input("Enter number of edges: "))
for _ in range(e):
    u = int(input("Enter first vertex: "))
    w = int(input("Enter second vertex: "))
    adj_list[u].append(w)
    adj_list[w].append(u)

u = int(input("Enter first node to check: "))
v = int(input("Enter second node to check: "))
print(f"Connected (list): {is_connected_list(adj_list, u, v)}")

#adjacency matrix
v = int(input("\nEnter number of vertices: "))
matrix = [[0] * v for _ in range(v)]

print("Enter adjacency matrix:")
for i in range(v):
    for j in range(v):
        matrix[i][j] = int(input(f"Element [{i}][{j}]: "))

u = int(input("Enter first node to check: "))
w = int(input("Enter second node to check: "))
print(f"Connected (matrix): {is_connected_matrix(matrix, u, w)}")
