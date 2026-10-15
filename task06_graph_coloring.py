"""
Task 6: Graph Coloring
Aim: Color graph vertices so that adjacent vertices do not share a color.
"""

def graph_coloring(graph, colors):
    assigned = {}

    def is_safe(node, color):
        return all(assigned.get(neighbor) != color for neighbor in graph[node])

    def backtrack(nodes, index=0):
        if index == len(nodes):
            return True

        node = nodes[index]
        for color in colors:
            if is_safe(node, color):
                assigned[node] = color
                if backtrack(nodes, index + 1):
                    return True
                del assigned[node]

        return False

    if backtrack(list(graph)):
        return assigned
    return None


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"],
    }
    colors = ["Red", "Green", "Blue"]
    result = graph_coloring(graph, colors)

    if result:
        for node, color in result.items():
            print(f"Node {node}: {color}")
    else:
        print("No valid coloring found.")


if __name__ == "__main__":
    main()
