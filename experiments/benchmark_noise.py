"""
Noise benchmark for QAOA.

Compares ideal QAOA with noisy QAOA
for different noise levels.
"""

import csv
import os

from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

from src.quantum.qubo import build_qubo
from src.quantum.ising import qubo_to_ising
from src.quantum.qaoa import create_qaoa_circuit
from src.utils.benchmarking import success_probability


def create_noise_model(error_rate):
    """
    Create a depolarizing noise model.
    """

    noise_model = NoiseModel()

    single_qubit_error = depolarizing_error(
        error_rate,
        1,
    )

    two_qubit_error = depolarizing_error(
        error_rate,
        2,
    )

    noise_model.add_all_qubit_quantum_error(
        single_qubit_error,
        ["h", "rx", "rz"],
    )

    noise_model.add_all_qubit_quantum_error(
        two_qubit_error,
        ["cx"],
    )

    return noise_model


def run_noisy_qaoa(
    numbers,
    target,
    gamma=0.6,
    beta=0.5,
    shots=1000,
    error_rate=0.0,
):
    """
    Run QAOA with a specified noise level.
    """

    Q = build_qubo(
        numbers=numbers,
        target=target,
    )

    constant, h, J = qubo_to_ising(Q)

    circuit = create_qaoa_circuit(
        h,
        J,
        gamma,
        beta,
    )

    if error_rate == 0.0:

        simulator = AerSimulator()

    else:

        noise_model = create_noise_model(
            error_rate
        )

        simulator = AerSimulator(
            noise_model=noise_model
        )

    result = simulator.run(
        circuit,
        shots=shots,
    ).result()

    counts = result.get_counts()

    probability = success_probability(
        counts,
        numbers=numbers,
        target=target,
    )

    return probability


def generate_problem(n, seed=42):
    """
    Generate a Subset Sum problem.
    """

    import random

    random.seed(seed)

    numbers = [
        random.randint(1, 100)
        for _ in range(n)
    ]

    target = sum(
        numbers[: n // 2]
    )

    return numbers, target


def run_noise_benchmark():

    sizes = [5, 10, 15, 20]

    noise_levels = [
        0.0,
        0.001,
        0.005,
        0.01,
    ]

    gamma = 0.6
    beta = 0.5
    shots = 1000

    print("QAOA Noise Benchmark")
    print("=" * 50)

    results = []

    results_directory = "results/quantum"

    os.makedirs(
        results_directory,
        exist_ok=True,
    )

    results_file = os.path.join(
        results_directory,
        "qaoa_noise_results.csv",
    )

    for n in sizes:

        numbers, target = generate_problem(n)

        print()
        print(f"n = {n}")
        print(f"Target = {target}")

        for error_rate in noise_levels:

            probability = run_noisy_qaoa(
                numbers=numbers,
                target=target,
                gamma=gamma,
                beta=beta,
                shots=shots,
                error_rate=error_rate,
            )

            print(
                f"Noise = {error_rate:.3f} "
                f"-> Success probability: "
                f"{probability:.2%}"
            )

            results.append({
                "n": n,
                "error_rate": error_rate,
                "gamma": gamma,
                "beta": beta,
                "shots": shots,
                "success_probability":
                    probability,
            })

    with open(
        results_file,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "n",
                "error_rate",
                "gamma",
                "beta",
                "shots",
                "success_probability",
            ],
        )

        writer.writeheader()
        writer.writerows(results)

    print()
    print("Results saved to:")
    print(results_file)


if __name__ == "__main__":

    run_noise_benchmark()