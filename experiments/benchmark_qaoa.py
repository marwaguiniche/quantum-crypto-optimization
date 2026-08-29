"""
Benchmark different QAOA parameter values.
"""

from src.quantum.quantum_solver import run_qaoa
from src.utils.benchmarking import success_probability


def benchmark_qaoa():

    best_probability = 0
    best_gamma = None
    best_beta = None

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

    print("QAOA parameter search")
    print("=" * 40)

    for gamma in gamma_values:

        for beta in beta_values:

            counts = run_qaoa(
                gamma=gamma,
                beta=beta,
                shots=2000,
            )

            probability = success_probability(counts)

            print(
                f"gamma={gamma:.1f}, "
                f"beta={beta:.1f} "
                f"-> success={probability:.2%}"
            )

            if probability > best_probability:

                best_probability = probability
                best_gamma = gamma
                best_beta = beta

    print("\nBest parameters")
    print("=" * 40)

    print("Gamma:", best_gamma)
    print("Beta:", best_beta)
    print(
        "Success probability:",
        f"{best_probability:.2%}"
    )


if __name__ == "__main__":
    benchmark_qaoa()