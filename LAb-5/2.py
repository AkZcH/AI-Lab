class Node:
    def __init__(self, state):
        self.state = state
        self.left = None
        self.right = None


def fill_jug1(state, cap1):
    x, y = state
    return (cap1, y)


def pour_jug1_to_jug2(state, cap1, cap2):
    x, y = state
    transfer = min(x, cap2 - y)
    return (x - transfer, y + transfer)


def build_binary_tree(state, cap1, cap2, depth, visited):
    if depth == 0 or state in visited:
        return None

    visited.add(state)
    node = Node(state)

    left_state = fill_jug1(state, cap1)
    right_state = pour_jug1_to_jug2(state, cap1, cap2)

    node.left = build_binary_tree(left_state, cap1, cap2, depth - 1, visited)
    node.right = build_binary_tree(right_state, cap1, cap2, depth - 1, visited)

    return node


def print_tree(node, level=0):
    if node is not None:
        print("  " * level + str(node.state))
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)


# Example
root = build_binary_tree((0, 0), 4, 3, depth=5, visited=set())
print_tree(root)
