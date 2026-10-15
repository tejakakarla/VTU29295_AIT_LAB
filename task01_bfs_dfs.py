"""
Task 1: Breadth-First Search (BFS) and Depth-First Search (DFS)
Aim: Implement BFS and DFS traversal on a graph containing three nodes.
"""

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return order


def dfs(graph, start):
    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }

    print("BFS traversal:", " -> ".join(bfs(graph, "A")))
    print("DFS traversal:", " -> ".join(dfs(graph, "A")))


if __name__ == "__main__":
    main()
