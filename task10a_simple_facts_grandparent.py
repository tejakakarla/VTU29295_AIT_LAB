"""
Task 10A: Simple Facts with kanren
Aim: Store parent facts and query the grandparent of Bart.
Dependency: pip install kanren
"""

from kanren import Relation, facts, var, run, conde


def main():
    parent = Relation()
    facts(
        parent,
        ("Abe", "Homer"),
        ("Homer", "Bart"),
        ("Homer", "Lisa"),
    )

    def grandparent(x, z):
        y = var()
        return conde((parent(x, y), parent(y, z)))

    x = var()
    result = run(1, x, grandparent(x, "Bart"))
    print(f"The grandparent of Bart is: {result[0]}")


if __name__ == "__main__":
    main()
