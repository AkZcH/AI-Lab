#wap to count the no. of edges in an undirected graph

def count_edges_list(adj_list):
    return sum(len(adj_list[i]) for i in range(len(adj_list))) // 2

def count_edges_matrix(matrix):
    return sum(sum(row) for row in matrix) // 2

#adjacency list
v = int(input("Enter number of vertices: "))
adj_list = [[] for _ in range(v)]

e = int(input("Enter number of edges: "))
for _ in range(e):
    u = int(input("Enter first vertex: "))
    w = int(input("Enter second vertex: "))
    adj_list[u].append(w)
    adj_list[w].append(u)

print(f"Number of edges: {count_edges_list(adj_list)}")

#adjacency matrix
v = int(input("\nEnter number of vertices: "))
matrix = [[0] * v for _ in range(v)]

print("Enter adjacency matrix:")
for i in range(v):
    for j in range(v):
        matrix[i][j] = int(input(f"Element [{i}][{j}]: "))

print(f"Number of edges: {count_edges_matrix(matrix)}")
