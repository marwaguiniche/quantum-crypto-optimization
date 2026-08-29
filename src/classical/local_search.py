"""
Local Search for the Subset Sum problem.
"""

import random


def calculate_sum(numbers, solution):
    """
    Calculate the sum represented by a binary solution.
    """

    return sum(
        numbers[i]
        for i in range(len(numbers))
        if solution[i] == 1
    )


def objective(numbers, solution, target):
    """
    Calculate the absolute error from the target.
    """

    return abs(
        calculate_sum(numbers, solution) - target
    )


def local_search(numbers, target, max_iterations=1000):
    """
    Solve the Subset Sum problem using Local Search.

    Parameters
    ----------
    numbers : list
        List of available numbers.

    target : int
        Desired target sum.

    max_iterations : int
        Maximum number of iterations.

    Returns
    -------
    list
        Binary solution.
    """

    # Start with a random binary solution
    solution = [
        random.randint(0, 1)
        for _ in range(len(numbers))
    ]

    current_error = objective(
        numbers,
        solution,
        target
    )

    for _ in range(max_iterations):

        # Generate a neighboring solution
        neighbor = solution.copy()

        # Flip one randomly selected variable
        index = random.randrange(len(numbers))

        neighbor[index] = 1 - neighbor[index]

        neighbor_error = objective(
            numbers,
            neighbor,
            target
        )

        # Accept the neighbor if it is better
        if neighbor_error < current_error:

            solution = neighbor
            current_error = neighbor_error

        # Stop if an exact solution is found
        if current_error == 0:
            break

    return solution


if __name__ == "__main__":

    numbers = [3, 5, 7, 10, 12]
    target = 15

    solution = local_search(
        numbers,
        target
    )

    selected = [
        numbers[i]
        for i in range(len(numbers))
        if solution[i] == 1
    ]

    total = calculate_sum(
        numbers,
        solution
    )

    print("Local Search solution:")
    print("Binary:", solution)
    print("Selected:", selected)
    print("Sum:", total)
    print("Target:", target)