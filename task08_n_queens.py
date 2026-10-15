"""
Task 8: N-Queens Problem
Aim: Place N queens on an N x N chessboard so that no two queens attack each other.
"""

def solve_n_queens(n):
    positions = []
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(positions.copy())
            return

        for col in range(n):
            safe = all(
                col != previous_col
                and abs(col - previous_col) != abs(row - previous_row)
                for previous_row, previous_col in enumerate(positions)
            )
            if safe:
                positions.append(col)
                backtrack(row + 1)
                positions.pop()

    backtrack(0)
    return solutions


def main():
    n = 4
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-Queens:", len(solutions))

    if solutions:
        print("One solution (column positions by row, 0-based):", solutions[0])
        for queen_col in solutions[0]:
            print(" ".join("Q" if col == queen_col else "." for col in range(n)))


if __name__ == "__main__":
    main()
