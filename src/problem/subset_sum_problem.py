"""
Subset Sum problem definition.

The goal is to select a subset of numbers whose sum
is exactly equal to a target value.
"""

NUMBERS = [3, 5, 7, 10, 12]
TARGET = 15


def evaluate_solution(solution):
    """
    Compute the sum represented by a binary solution.

    Parameters
    ----------
    solution : list[int]
        Binary vector such as [1, 0, 1, 0, 0].

    Returns
    -------
    int
        Sum of the selected numbers.
    """

    return sum(
        NUMBERS[i] * solution[i]
        for i in range(len(NUMBERS))
    )


def constraint_violation(solution):
    """
    Measure how far a solution is from the target.

    A value of 0 means that the solution is valid.
    """

    return abs(
        evaluate_solution(solution) - TARGET
    )


def is_valid_solution(solution):
    """
    Check whether a solution satisfies the target exactly.
    """

    return constraint_violation(solution) == 0