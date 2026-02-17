from collections import deque

def get_next_states(state, cap1, cap2):
    x, y = state
    states = []

    # Fill jug1
    states.append((cap1, y))

    # Fill jug2
    states.append((x, cap2))

    # Empty jug1
    states.append((0, y))

    # Empty jug2
    states.append((x, 0))

    # Pour jug1 -> jug2
    transfer = min(x, cap2 - y)
    states.append((x - transfer, y + transfer))

    # Pour jug2 -> jug1
    transfer = min(y, cap1 - x)
    states.append((x + transfer, y - transfer))

    return states


def state_space_graph(cap1, cap2):
    visited = set()
    queue = deque([(0, 0)])

    graph = {}

    while queue:
        state = queue.popleft()
        if state in visited:
            continue

        visited.add(state)
        graph[state] = []

        for next_state in get_next_states(state, cap1, cap2):
            if next_state not in visited:
                queue.append(next_state)
            graph[state].append(next_state)

    return graph


# Example
graph = state_space_graph(4, 3)

for state in graph:
    print(f"{state} -> {graph[state]}")
