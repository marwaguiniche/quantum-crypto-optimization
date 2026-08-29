"""
QUBO formulation of the Subset Sum problem.
"""

import numpy as np

from src.problem.subset_sum_problem import (
    NUMBERS,
    TARGET,
)

def build_qubo(
    numbers=None,
    target=None,
    penalty=1.0,
):

    # Use the default problem if no custom
    # numbers or target are provided.
    if numbers is None:
        numbers = NUMBERS

    if target is None:
        target = TARGET

    n = len(numbers)

    Q = np.zeros((n, n))

    # Linear terms
    for i in range(n):

        Q[i, i] += penalty * (
            numbers[i] ** 2
            - 2 * target * numbers[i]
        )

    # Quadratic terms
    for i in range(n):

        for j in range(i + 1, n):

            Q[i, j] += (
                2
                * penalty
                * numbers[i]
                * numbers[j]
            )

    # Constant term target^2 is ignored
    # because it does not affect the optimizer.

    return Q


def qubo_energy(solution, Q):

    x = np.array(solution)

    return float(
        x @ Q @ x
    )


if __name__ == "__main__":

    Q = build_qubo()

    print("QUBO matrix:")
    print(Q)

    solution = [1, 1, 1, 0, 0]

    energy = qubo_energy(
        solution,
        Q
    )

    print("\nSolution:", solution)
    print("QUBO energy:", energy)