"""
Task 4: Minimax Algorithm
Aim: Select the best move for the maximizing player in a small game tree.
"""

def minimax(tree, node, maximizing):
    children = tree.get(node)

    if not children:
        return node

    values = [minimax(tree, child, not maximizing) for child in children]

    if maximizing:
        return max(values)
    return min(values)


def main():
    # Leaf values are possible game scores.
    tree = {
        "root": ["A", "B"],
        "A": [3, 5],
        "B": [2, 9],
    }

    best_value = minimax(tree, "root", True)
    print("Best value for maximizing player:", best_value)


if __name__ == "__main__":
    main()
