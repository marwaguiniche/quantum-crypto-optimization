"""
Automatic optimization of QAOA parameters.
"""

import numpy as np

from src.quantum.quantum_solver import run_qaoa


def optimize_qaoa(
    numbers,
    target,
    shots=1000,
):
    """
    Search for the best gamma and beta parameters.
    """

    best_gamma = None
    best_beta = None
    best_probability = -1

    gamma_values = np.arange(
        0.1,
        1.1,
        0.1,
    )

    beta_values = np.arange(
        0.1,
        1.1,
        0.1,
    )

    print()
    print("QAOA Parameter Optimization")
    print("=" * 50)

    for gamma in gamma_values:

        for beta in beta_values:

            result = run_qaoa(
                numbers=numbers,
                target=target,
                gamma=float(gamma),
                beta=float(beta),
                shots=shots,
            )

            probability = result[
                "success_probability"
            ]

            print(
                f"gamma={gamma:.1f}, "
                f"beta={beta:.1f} -> "
                f"{probability:.2%}"
            )

            if probability > best_probability:

                best_probability = probability
                best_gamma = gamma
                best_beta = beta

    print()
    print("Best parameters:")
    print(
        f"Gamma = {best_gamma:.1f}"
    )
    print(
        f"Beta = {best_beta:.1f}"
    )
    print(
        f"Success probability = "
        f"{best_probability:.2%}"
    )

    return (
        best_gamma,
        best_beta,
        best_probability,
    )


if __name__ == "__main__":

    numbers = [3, 5, 7, 10, 12]
    target = 15

    optimize_qaoa(
        numbers,
        target,
        shots=1000,
    )