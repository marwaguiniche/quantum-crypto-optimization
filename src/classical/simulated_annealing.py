
"""
Simulated Annealing for the Subset Sum problem.
"""

import math
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


def simulated_annealing(
    numbers,
    target,
    initial_temperature=10.0,
    cooling_rate=0.995,
    max_iterations=5000,
):
    """
    Solve the Subset Sum problem using Simulated Annealing.

    Parameters
    ----------
    numbers : list
        List of available numbers.

    target : int
        Desired target sum.

    initial_temperature : float
        Initial temperature.

    cooling_rate : float
        Rate at which the temperature decreases.

    max_iterations : int
        Maximum number of iterations.

    Returns
    -------
    list
        Best binary solution found.
    """

    # Random initial solution
    solution = [
        random.randint(0, 1)
        for _ in range(len(numbers))
    ]

    current_value = calculate_sum(
        numbers,
        solution
    )

    current_error = abs(
        current_value - target
    )

    best_solution = solution.copy()
    best_error = current_error

    temperature = initial_temperature

    for _ in range(max_iterations):

        # Create a neighboring solution
        neighbor = solution.copy()

        # Flip one binary variable
        index = random.randrange(len(numbers))

        neighbor[index] = 1 - neighbor[index]

        neighbor_value = calculate_sum(
            numbers,
            neighbor
        )

        neighbor_error = abs(
            neighbor_value - target
        )

        # Difference between new and current solution
        delta = neighbor_error - current_error

        # Accept a better solution
        if delta < 0:

            solution = neighbor
            current_error = neighbor_error

        # Sometimes accept a worse solution
        else:

            if temperature > 0:

                probability = math.exp(
                    -delta / temperature
                )

                if random.random() < probability:

                    solution = neighbor
                    current_error = neighbor_error

        # Keep track of the best solution
        if current_error < best_error:

            best_solution = solution.copy()
            best_error = current_error

        # Stop if target is reached
        if best_error == 0:
            break

        # Cool down
        temperature *= cooling_rate

        if temperature < 1e-8:
            break

    return best_solution


if __name__ == "__main__":

    numbers = [3, 5, 7, 10, 12]
    target = 15

    solution = simulated_annealing(
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

    print("Simulated Annealing")
    print("Binary:", solution)
    print("Selected:", selected)
    print("Sum:", total)
    print("Target:", target)
    print("Error:", abs(total - target))
