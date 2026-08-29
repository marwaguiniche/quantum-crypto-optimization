"""
Scalability benchmark for QAOA.

Measures the probability of obtaining a valid
Subset Sum solution for different problem sizes.
"""

import csv
import os
import random
import time

from src.quantum.quantum_solver import run_qaoa


def generate_problem(n, seed=42):
    """
    Generate a random Subset Sum problem.

    The target is constructed from the first half
    of the generated numbers so that at least one
    valid solution exists.
    """

    random.seed(seed)

    numbers = [
        random.randint(1, 100)
        for _ in range(n)
    ]

    target = sum(
        numbers[: n // 2]
    )

    return numbers, target


def run_qaoa_scalability():

    # Problem sizes
    sizes = [5, 10, 15, 20]

    # Optimized QAOA parameters
    gamma = 0.6
    beta = 0.5

    # Number of measurements
    shots = 1000

    print("QAOA Scalability Benchmark")
    print("=" * 50)

    # Store all results
    results = []

    # Create results directory
    results_directory = "results/quantum"

    os.makedirs(
        results_directory,
        exist_ok=True
    )

    # CSV output file
    results_file = os.path.join(
        results_directory,
        "qaoa_scalability_results.csv"
    )

    for n in sizes:

        numbers, target = generate_problem(n)

        print()
        print(f"n = {n}")
        print(f"Target = {target}")

        # Measure execution time
        start = time.perf_counter()

        result = run_qaoa(
            numbers=numbers,
            target=target,
            gamma=gamma,
            beta=beta,
            shots=shots,
        )

        end = time.perf_counter()

        execution_time = end - start

        success_probability = (
            result["success_probability"]
        )

        print(
            f"Success probability: "
            f"{success_probability:.2%}"
        )

        print(
            f"Execution time: "
            f"{execution_time:.6f} seconds"
        )

        # Save result
        results.append({
            "n": n,
            "gamma": gamma,
            "beta": beta,
            "shots": shots,
            "success_probability":
                success_probability,
            "time":
                execution_time,
            "target":
                target,
        })

    # Save results to CSV
    with open(
        results_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "n",
                "gamma",
                "beta",
                "shots",
                "success_probability",
                "time",
                "target",
            ]
        )

        writer.writeheader()

        writer.writerows(results)

    print()
    print("Results saved to:")
    print(results_file)


if __name__ == "__main__":

    run_qaoa_scalability()