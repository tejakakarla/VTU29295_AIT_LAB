"""
Task 7: Monkey and Banana Problem
Aim: Represent the classic problem and show the action sequence that lets the
monkey obtain the banana.
"""

def solve_monkey_banana():
    actions = [
        "Monkey moves to the box.",
        "Monkey pushes the box under the banana.",
        "Monkey climbs onto the box.",
        "Monkey grabs the banana.",
    ]
    return actions


def main():
    print("Initial state: Monkey is on the floor; banana is out of reach.")
    for step, action in enumerate(solve_monkey_banana(), start=1):
        print(f"{step}. {action}")
    print("Goal state: Monkey has the banana.")


if __name__ == "__main__":
    main()
