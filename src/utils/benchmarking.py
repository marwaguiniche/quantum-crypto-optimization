"""
Utilities for evaluating QAOA results.
"""

from src.problem.subset_sum_problem import (
    NUMBERS,
    TARGET,
)


def binary_to_sum(
    state,
    numbers=None,
):
    """
    Convert a measured binary state into
    the corresponding subset sum.
    """

    if numbers is None:
        numbers = NUMBERS

    # Qiskit displays classical bits
    # in reverse order.
    bits = state[::-1]

    return sum(
        numbers[i]
        for i in range(len(numbers))
        if bits[i] == "1"
    )


def is_valid_state(
    state,
    numbers=None,
    target=None,
):
    """
    Check whether a measured state reaches
    the target.
    """

    if numbers is None:
        numbers = NUMBERS

    if target is None:
        target = TARGET

    return (
        binary_to_sum(
            state,
            numbers,
        )
        == target
    )


def success_probability(
    counts,
    numbers=None,
    target=None,
):
    """
    Calculate the probability of measuring
    a valid solution.
    """

    if numbers is None:
        numbers = NUMBERS

    if target is None:
        target = TARGET

    total_shots = sum(
        counts.values()
    )

    successful_shots = sum(
        count
        for state, count in counts.items()
        if is_valid_state(
            state,
            numbers,
            target,
        )
    )

    if total_shots == 0:
        return 0.0

    return (
        successful_shots
        / total_shots
    )

