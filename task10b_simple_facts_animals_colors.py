"""
Task 10B: Simple Facts with kanren
Aim: Find green animals and query the color of a canary.
Dependency: pip install kanren
"""

from kanren import Relation, facts, var, run


def main():
    is_animal = Relation()
    has_color = Relation()

    facts(is_animal, "Frog", "Crocodile", "Canary", "Flamingo")
    facts(
        has_color,
        ("Frog", "Green"),
        ("Crocodile", "Green"),
        ("Canary", "Yellow"),
        ("Flamingo", "Pink"),
    )

    x = var()
    green_animals = run(0, x, is_animal(x), has_color(x, "Green"))
    print(f"Green animals: {green_animals}")

    color = var()
    canary_color = run(1, color, has_color("Canary", color))
    print(f"A canary is: {canary_color[0]}")


if __name__ == "__main__":
    main()
