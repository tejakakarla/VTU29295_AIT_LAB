"""
Task 3: A* Search Algorithm
Aim: Find a least-cost path from the start node to the goal using g(n) + h(n).
"""

import heapq


def a_star(graph, heuristic, start, goal):
    frontier = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while frontier:
        _, cost, node, path = heapq.heappop(frontier)

        if node == goal:
            return path, cost

        if cost > best_cost.get(node, float("inf")):
            continue

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(
                    frontier, (priority, new_cost, neighbor, path + [neighbor])
                )

    return None, float("inf")


def main():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    heuristic = {"A": 4, "B": 3, "C": 1, "D": 0}

    path, cost = a_star(graph, heuristic, "A", "D")
    print("Path:", " -> ".join(path) if path else "No path found")
    print("Total cost:", cost)


if __name__ == "__main__":
    main()
