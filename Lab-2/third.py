#wap to find the degree of all vertices from adjacency matrix and list

def degree_list(adj_list):
    for i in range(len(adj_list)):
        print(f"Degree of vertex {i}: {len(adj_list[i])}")

def degree_matrix(matrix):
    for i in range(len(matrix)):
        print(f"Degree of vertex {i}: {sum(matrix[i])}")

#adjacency list
v = int(input("Enter number of vertices: "))
adj_list = [[] for _ in range(v)]

e = int(input("Enter number of edges: "))
for _ in range(e):
    u = int(input("Enter first vertex: "))
    w = int(input("Enter second vertex: "))
    adj_list[u].append(w)
    adj_list[w].append(u)

print("\nDegrees (adjacency list):")
degree_list(adj_list)

#adjacency matrix
v = int(input("\nEnter number of vertices: "))
matrix = [[0] * v for _ in range(v)]

print("Enter adjacency matrix:")
for i in range(v):
    for j in range(v):
        matrix[i][j] = int(input(f"Element [{i}][{j}]: "))

print("\nDegrees (adjacency matrix):")
degree_matrix(matrix)
