"""
Quantum simulation of the QAOA circuit.
"""

from src.utils.benchmarking import success_probability

from qiskit_aer import AerSimulator

from src.quantum.qubo import build_qubo
from src.quantum.ising import qubo_to_ising
from src.quantum.qaoa import create_qaoa_circuit


def run_qaoa(
    numbers=None,
    target=None,
    gamma=0.5,
    beta=0.5,
    shots=10000,
):

    # ------------------------------------------------
    # 1. Build QUBO
    # ------------------------------------------------

    Q = build_qubo(
        numbers=numbers,
        target=target,
    )

    # ------------------------------------------------
    # 2. Convert QUBO to Ising
    # ------------------------------------------------

    constant, h, J = qubo_to_ising(Q)

    # ------------------------------------------------
    # 3. Create QAOA circuit
    # ------------------------------------------------

    circuit = create_qaoa_circuit(
        h,
        J,
        gamma,
        beta,
    )

    # ------------------------------------------------
    # 4. Create simulator
    # ------------------------------------------------

    simulator = AerSimulator()

    # ------------------------------------------------
    # 5. Execute circuit
    # ------------------------------------------------

    result = simulator.run(
        circuit,
        shots=shots,
    ).result()

    # ------------------------------------------------
    # 6. Get measurement counts
    # ------------------------------------------------

    counts = result.get_counts()

    # ------------------------------------------------
    # 7. Calculate success probability
    # ------------------------------------------------

    probability = success_probability(
        counts,
        numbers=numbers,
        target=target,
    )

    return {
        "counts": counts,
        "success_probability": probability,
    }


if __name__ == "__main__":

    result = run_qaoa()

    counts = result["counts"]

    print("QAOA measurement results:")
    print()

    for state, count in sorted(
        counts.items(),
        key=lambda item: item[1],
        reverse=True,
    ):

        probability = count / 10000

        print(
            state,
            "->",
            count,
            "shots",
            f"({probability:.2%})"
        )

    probability = result[
        "success_probability"
    ]

    print()

    print(
        "Probability of measuring a valid solution:",
        f"{probability:.2%}"
    )
