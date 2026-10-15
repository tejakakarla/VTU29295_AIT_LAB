"""
Task 2: Hill Climbing Algorithm using a Small Game
Aim: Find the highest-scoring position by repeatedly moving to a better neighbor.
The game uses a one-dimensional score landscape.
"""


def score(position):
    return -(position - 3) ** 2 + 10


def hill_climb(start):
    current = start

    while True:
        neighbors = [current - 1, current + 1]
        best_neighbor = max(neighbors, key=score)

        if score(best_neighbor) <= score(current):
            return current

        current = best_neighbor


def main():
    start = 0
    best_position = hill_climb(start)

    print("Starting position:", start)
    print("Starting score:", score(start))
    print("Best position found:", best_position)
    print("Best score:", score(best_position))


if __name__ == "__main__":
    main()
