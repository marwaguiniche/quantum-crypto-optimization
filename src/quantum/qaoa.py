"""
QAOA circuit for the QUBO/Ising problem.
"""

import numpy as np
from qiskit import QuantumCircuit


def create_qaoa_circuit(
    h,
    J,
    gamma,
    beta,
):
    """
    Create a one-layer QAOA circuit.

    Parameters
    ----------
    h : array
        Linear Ising coefficients.

    J : matrix
        Quadratic Ising coefficients.

    gamma : float
        Cost Hamiltonian angle.

    beta : float
        Mixer Hamiltonian angle.
    """

    n = len(h)

    qc = QuantumCircuit(n)

    # ------------------------------------------------
    # 1. Initial state: uniform superposition
    # ------------------------------------------------

    for i in range(n):
        qc.h(i)

    # ------------------------------------------------
    # 2. Cost Hamiltonian
    # ------------------------------------------------

    for i in range(n):

        if abs(h[i]) > 1e-12:

            qc.rz(
                2 * gamma * h[i],
                i
            )

    for i in range(n):

        for j in range(i + 1, n):

            if abs(J[i, j]) > 1e-12:

                qc.cx(i, j)

                qc.rz(
                    2 * gamma * J[i, j],
                    j
                )

                qc.cx(i, j)

    # ------------------------------------------------
    # 3. Mixer Hamiltonian
    # ------------------------------------------------

    for i in range(n):

        qc.rx(
            2 * beta,
            i
        )

    # ------------------------------------------------
    # 4. Measurement
    # ------------------------------------------------

    qc.measure_all()

    return qc


if __name__ == "__main__":

    from src.quantum.ising import qubo_to_ising
    from src.quantum.qubo import build_qubo

    Q = build_qubo()

    constant, h, J = qubo_to_ising(Q)

    gamma = 0.5
    beta = 0.5

    circuit = create_qaoa_circuit(
        h,
        J,
        gamma,
        beta
    )

    print(circuit)