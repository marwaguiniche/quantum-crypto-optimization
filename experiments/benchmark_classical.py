import itertools
import time

from src.problem.subset_sum_problem import (
    NUMBERS,
    TARGET,
)
from src.classical.local_search import local_search


def exhaustive_search():
    solutions = []

    for solution in itertools.product([0, 1], repeat=len(NUMBERS)):
        total = sum(
            NUMBERS[i] * solution[i]
            for i in range(len(NUMBERS))
        )

        if total == TARGET:
            solutions.append(solution)

    return solutions


def run_exhaustive_search():
    start = time.perf_counter()

    solutions = exhaustive_search()

    elapsed = time.perf_counter() - start

    return len(solutions), elapsed


def run_local_search():
    start = time.perf_counter()

    solution = local_search()

    elapsed = time.perf_counter() - start

    total = sum(
        NUMBERS[i] * solution[i]
        for i in range(len(NUMBERS))
    )

    return total, elapsed


if __name__ == "__main__":

    print("=== Classical Optimization Benchmark ===")

    # Exhaustive Search
    number_of_solutions, exhaustive_time = run_exhaustive_search()

    print("\nExhaustive Search")
    print("Solutions found:", number_of_solutions)
    print("Time:", exhaustive_time, "seconds")

    # Local Search
    local_result, local_time = run_local_search()

    print("\nLocal Search")
    print("Obtained sum:", local_result)
    print("Target:", TARGET)
    print("Time:", local_time, "seconds")