"""
Conversion from QUBO to Ising formulation.
"""

import numpy as np

from src.quantum.qubo import build_qubo


def qubo_to_ising(Q):
    """
    Convert a QUBO matrix Q into Ising coefficients.

    QUBO:
        E(x) = x^T Q x

    with:
        x_i in {0, 1}

    Ising:
        E(z) = constant + sum_i h_i z_i
                         + sum_{i<j} J_ij z_i z_j

    with:
        z_i in {-1, +1}
    """

    n = Q.shape[0]

    h = np.zeros(n)
    J = np.zeros((n, n))

    constant = 0.0

    # Diagonal terms
    for i in range(n):

        constant += Q[i, i] / 2
        h[i] -= Q[i, i] / 2

    # Off-diagonal terms
    for i in range(n):

        for j in range(i + 1, n):

            q = Q[i, j]

            constant += q / 4

            h[i] -= q / 4
            h[j] -= q / 4

            J[i, j] += q / 4

    return constant, h, J


if __name__ == "__main__":

    Q = build_qubo()

    constant, h, J = qubo_to_ising(Q)

    print("QUBO matrix:")
    print(Q)

    print("\nIsing constant:")
    print(constant)

    print("\nIsing h coefficients:")
    print(h)

    print("\nIsing J coefficients:")
    print(J)