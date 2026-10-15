"""
Task 10C: Simple Facts with kanren
Aim: Find students who study Python and determine Rahul's subject.
Dependency: pip install kanren
"""

from kanren import Relation, facts, var, run


def main():
    is_student = Relation()
    studies = Relation()

    facts(is_student, "Rahul", "Priya", "Arun", "Sneha")
    facts(
        studies,
        ("Rahul", "Python"),
        ("Priya", "Java"),
        ("Arun", "Python"),
        ("Sneha", "C++"),
    )

    x = var()
    python_students = run(0, x, is_student(x), studies(x, "Python"))
    print(f"Students studying Python: {python_students}")

    subject = var()
    rahul_subject = run(1, subject, studies("Rahul", subject))
    print(f"Rahul studies: {rahul_subject[0]}")


if __name__ == "__main__":
    main()
