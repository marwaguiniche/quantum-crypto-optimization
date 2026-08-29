from src.problem.subset_sum_problem import (
    evaluate_solution,
    constraint_violation,
    is_valid_solution,
)


def test_valid_solution():

    solution = [1, 1, 1, 0, 0]

    assert evaluate_solution(solution) == 15
    assert constraint_violation(solution) == 0
    assert is_valid_solution(solution)


def test_invalid_solution():

    solution = [1, 0, 1, 0, 0]

    assert evaluate_solution(solution) == 10
    assert constraint_violation(solution) == 5
    assert not is_valid_solution(solution)