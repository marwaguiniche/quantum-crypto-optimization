"""
QAOA parameter grid experiment.

This experiment evaluates different values of gamma and beta
and saves the results for later analysis.
"""

import csv
import os

from src.quantum.quantum_solver import run_qaoa
from src.utils.benchmarking import success_probability


def run_parameter_grid():

    gamma_values = [
        0.1,
        0.3,
        0.5,
        0.7,
        0.9,
        1.1,
        1.3,
        1.5,
    ]

    beta_values = [
        0.1,
        0.3,
        0.5,
        0.7,
        0.9,
        1.1,
        1.3,
        1.5,
    ]

    results = []

    print("Running QAOA parameter grid...")
    print("=" * 50)

    for gamma in gamma_values:

        for beta in beta_values:

            counts = run_qaoa(
                gamma=gamma,
                beta=beta,
                shots=2000,
            )

            probability = success_probability(counts)

            results.append([
                gamma,
                beta,
                probability,
            ])

            print(
                f"gamma={gamma:.1f}, "
                f"beta={beta:.1f}, "
                f"success={probability:.2%}"
            )

    return results


def save_results(results):

    output_directory = "results/quantum"

    os.makedirs(
        output_directory,
        exist_ok=True,
    )

    output_file = os.path.join(
        output_directory,
        "qaoa_parameter_grid.csv",
    )

    with open(
        output_file,
        "w",
        newline="",
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "gamma",
            "beta",
            "success_probability",
        ])

        writer.writerows(results)

    print()
    print("Results saved to:")
    print(output_file)


if __name__ == "__main__":

    results = run_parameter_grid()

    save_results(results)