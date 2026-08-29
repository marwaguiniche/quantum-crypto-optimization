"""
MILP formulation of the Subset Sum problem.
"""

from ortools.linear_solver import pywraplp

from src.problem.subset_sum_problem import (
    NUMBERS,
    TARGET,
)


def solve_milp():

    # Create the solver
    solver = pywraplp.Solver.CreateSolver("SCIP")

    if solver is None:
        raise RuntimeError("SCIP solver could not be created.")

    # Binary decision variables
    x = [
        solver.IntVar(0, 1, f"x_{i}")
        for i in range(len(NUMBERS))
    ]

    # Constraint:
    # sum(numbers[i] * x[i]) == TARGET
    solver.Add(
        sum(
            NUMBERS[i] * x[i]
            for i in range(len(NUMBERS))
        )
        == TARGET
    )

    # Objective:
    # minimize the number of selected elements
    solver.Minimize(sum(x))

        # Solve the optimization problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:

        solution = [
            int(variable.solution_value())
            for variable in x
        ]

        selected = [
            NUMBERS[i]
            for i in range(len(NUMBERS))
            if solution[i] == 1
        ]

        total = sum(selected)

        print("MILP solution")
        print("Binary:", solution)
        print("Selected:", selected)
        print("Number of selected elements:", len(selected))
        print("Sum:", total)
        print("Target:", TARGET)

        return solution

    else:
        print("No optimal solution found.")
        return None


if __name__ == "__main__":
    solve_milp()