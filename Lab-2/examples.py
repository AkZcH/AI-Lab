# Input/Output Examples for Lab-2 Programs

# Example 1: first.py - Count edges
"""
Input:
Enter number of vertices: 4
Enter number of edges: 3
Enter first vertex: 0
Enter second vertex: 1
Enter first vertex: 1
Enter second vertex: 2
Enter first vertex: 2
Enter second vertex: 3

Output:
Number of edges: 3

Input:
Enter number of vertices: 3
Enter adjacency matrix:
Element [0][0]: 0
Element [0][1]: 1
Element [0][2]: 1
Element [1][0]: 1
Element [1][1]: 0
Element [1][2]: 0
Element [2][0]: 1
Element [2][1]: 0
Element [2][2]: 0

Output:
Number of edges: 2
"""

# Example 2: second.py - Check if nodes are connected
"""
Input:
Enter number of vertices: 4
Enter number of edges: 3
Enter first vertex: 0
Enter second vertex: 1
Enter first vertex: 1
Enter second vertex: 2
Enter first vertex: 2
Enter second vertex: 3
Enter first node to check: 0
Enter second node to check: 1

Output:
Connected (list): True

Input:
Enter number of vertices: 3
Enter adjacency matrix:
Element [0][0]: 0
Element [0][1]: 1
Element [0][2]: 0
Element [1][0]: 1
Element [1][1]: 0
Element [1][2]: 1
Element [2][0]: 0
Element [2][1]: 1
Element [2][2]: 0
Enter first node to check: 0
Enter second node to check: 2

Output:
Connected (matrix): False
"""

# Example 3: third.py - Find degree of vertices
"""
Input:
Enter number of vertices: 4
Enter number of edges: 3
Enter first vertex: 0
Enter second vertex: 1
Enter first vertex: 1
Enter second vertex: 2
Enter first vertex: 2
Enter second vertex: 3

Output:
Degrees (adjacency list):
Degree of vertex 0: 1
Degree of vertex 1: 2
Degree of vertex 2: 2
Degree of vertex 3: 1

Input:
Enter number of vertices: 3
Enter adjacency matrix:
Element [0][0]: 0
Element [0][1]: 1
Element [0][2]: 1
Element [1][0]: 1
Element [1][1]: 0
Element [1][2]: 1
Element [2][0]: 1
Element [2][1]: 1
Element [2][2]: 0

Output:
Degrees (adjacency matrix):
Degree of vertex 0: 2
Degree of vertex 1: 2
Degree of vertex 2: 2
"""

# Example 4: fourth.py - Check path existence
"""
Input:
Enter number of vertices: 4
Enter number of edges: 3
Enter first vertex: 0
Enter second vertex: 1
Enter first vertex: 1
Enter second vertex: 2
Enter first vertex: 2
Enter second vertex: 3
Enter number of nodes in path: 4
Enter node 0: 0
Enter node 1: 1
Enter node 2: 2
Enter node 3: 3

Output:
Path exists (list): True
Path length: 3

Input:
Enter number of vertices: 3
Enter adjacency matrix:
Element [0][0]: 0
Element [0][1]: 1
Element [0][2]: 0
Element [1][0]: 1
Element [1][1]: 0
Element [1][2]: 1
Element [2][0]: 0
Element [2][1]: 1
Element [2][2]: 0
Enter number of nodes in path: 3
Enter node 0: 0
Enter node 1: 1
Enter node 2: 2

Output:
Path exists (matrix): True
Path length: 2
"""
