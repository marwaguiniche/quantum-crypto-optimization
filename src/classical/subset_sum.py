"""
Exhaustive search for the Subset Sum problem.
"""

from itertools import product

from src.problem.subset_sum_problem import (
    NUMBERS,
    TARGET,
    evaluate_solution,
    is_valid_solution,
)


def exhaustive_search():
    """
    Explore all possible binary solutions.

    Returns
    -------
    list
        All valid solutions.
    """

    solutions = []

    for solution in product([0, 1], repeat=len(NUMBERS)):

        if is_valid_solution(solution):
            solutions.append(solution)

    return solutions


if __name__ == "__main__":

    solutions = exhaustive_search()

    print("Numbers:", NUMBERS)
    print("Target:", TARGET)
    print("Number of solutions:", len(solutions))

    print("\nSolutions:")

    for solution in solutions:

        selected = [
            NUMBERS[i]
            for i in range(len(NUMBERS))
            if solution[i] == 1
        ]

        total = evaluate_solution(solution)

        print(
            solution,
            "->",
            selected,
            "=",
            total
        )