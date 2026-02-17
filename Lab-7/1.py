import heapq

def best_first_search(grid, start, goal):
    """
    Best-First Search to find the treasure in a grid.

    Args:
        grid (list of lists): The grid representing the map.
        start (tuple): The starting coordinates (row, col).
        goal (tuple): The treasure coordinates (row, col).

    Returns:
        list of tuples: The path from start to goal, or None if no path is found.
    """
    rows, cols = len(grid), len(grid[0])
    
    def manhattan_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue to store cells to visit, prioritized by heuristic
    # (heuristic, current_path)
    open_list = [(manhattan_distance(start, goal), [start])]
    heapq.heapify(open_list)
    
    # Set to keep track of visited cells
    visited = {start}

    while open_list:
        _, path = heapq.heappop(open_list)
        current_cell = path[-1]

        if current_cell == goal:
            return path  # Treasure found

        r, c = current_cell
        
        # Explore neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                new_path = path + [(nr, nc)]
                heuristic_value = manhattan_distance((nr, nc), goal)
                heapq.heappush(open_list, (heuristic_value, new_path))
    
    return None # Treasure not found

def print_grid_with_path(grid, path):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if (r, c) in path:
                print("*", end=" ")
            else:
                print(cell, end=" ")
        print()

if __name__ == "__main__":
    # Define the grid, start, and goal
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2]
    ]
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    # Find the path
    path = best_first_search(grid, start_pos, goal_pos)

    if path:
        print("Treasure found! Path:")
        print_grid_with_path(grid, path)
        print("\nPath coordinates:", path)
    else:
        print("Treasure not found.")

    print("\n--- Heuristic Performance Analysis ---")
    print("The Best-First Search algorithm uses a heuristic function to estimate the 'closeness' of a cell to the treasure.")
    print("In this implementation, we use the Manhattan distance: h(n) = |x1 - x2| + |y1 - y2|.")
    print("\nHow heuristic choice affects performance:")
    print("1. Completeness: Best-First Search is not complete. A poor heuristic can lead it down an infinite path or a path that doesn't lead to the goal, even if one exists.")
    print("2. Optimality: It is not optimal. It follows a greedy approach, always choosing the most promising cell based on the heuristic. This might not result in the shortest path.")
    print("3. Time and Space Complexity: The worst-case time and space complexity is O(b^m), where 'b' is the branching factor and 'm' is the maximum depth. However, a good heuristic can significantly reduce the search space, improving performance by guiding the search more directly towards the goal.")
    print("\nThe Manhattan distance is a good heuristic for a grid when movement is restricted to four directions (up, down, left, right) because it accurately represents the minimum number of moves to reach the goal, ignoring any obstacles.")

