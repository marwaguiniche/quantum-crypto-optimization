"""
Scalability benchmark for Exhaustive Search and MILP.
"""
import csv
import os
import time
import random
from itertools import product
from src.classical.local_search import local_search
from src.classical.simulated_annealing import simulated_annealing
def generate_problem(n, seed=42):

    random.seed(seed)

    numbers = [
        random.randint(1, 100)
        for _ in range(n)
    ]

    # Construct a target that is guaranteed
    # to have at least one solution.
    target = sum(numbers[:n // 2])

    return numbers, target


def exhaustive_search_scalability(numbers, target):

    solutions = []

    for solution in product(
        [0, 1],
        repeat=len(numbers)
    ):

        total = sum(
            numbers[i]
            for i in range(len(numbers))
            if solution[i] == 1
        )

        if total == target:
            solutions.append(solution)

    return solutions


def milp_scalability(numbers, target):

    from ortools.linear_solver import pywraplp

    solver = pywraplp.Solver.CreateSolver("SCIP")

    if solver is None:
        raise RuntimeError(
            "SCIP solver is not available."
        )

    x = [
        solver.IntVar(
            0,
            1,
            f"x_{i}"
        )
        for i in range(len(numbers))
    ]

    # Subset Sum constraint
    solver.Add(
        sum(
            numbers[i] * x[i]
            for i in range(len(numbers))
        ) == target
    )

    # Minimize number of selected elements
    solver.Minimize(
        sum(x)
    )

    status = solver.Solve()

    if status != pywraplp.Solver.OPTIMAL:
        return None

    solution = [
        int(variable.solution_value())
        for variable in x
    ]

    return solution


def run_scalability_experiment():

    sizes = [5, 10, 15, 20]

    print(
        "Exhaustive Search vs MILP Scalability"
    )

    print("=" * 50)
    results = []
    # Create the results directory
    results_directory = "results/classical"

    os.makedirs(
        results_directory,
        exist_ok=True
    )

    # CSV file where results will be saved
    results_file = os.path.join(
        results_directory,
        "scalability_results.csv"
    )


    for n in sizes:

        numbers, target = generate_problem(n)

        print()
        print(f"n = {n}")
        print(f"Target = {target}")

        # -------------------------
        # Exhaustive Search
        # -------------------------

        start = time.perf_counter()

        solutions = exhaustive_search_scalability(
            numbers,
            target
        )

        end = time.perf_counter()

        execution_time = end - start

        print(
            f"Exhaustive Search: "
            f"{execution_time:.6f} seconds"
        )

        print(
            f"Solutions found: "
            f"{len(solutions)}"
        )

        results.append({
            "n": n,
            "method": "Exhaustive Search",
            "time": execution_time,
            "solution_sum": target,
            "target": target
        })


        # -------------------------
        # MILP
        # -------------------------

        start = time.perf_counter()

        milp_solution = milp_scalability(
            numbers,
            target
        )

        end = time.perf_counter()

        milp_time = end - start

        if milp_solution is not None:

            milp_sum = sum(
                numbers[i]
                for i in range(len(numbers))
                if milp_solution[i] == 1
            )

            print(
                f"MILP: "
                f"{milp_time:.6f} seconds"
            )

            print(
                f"MILP solution sum: "
                f"{milp_sum}"
            )

            results.append({
                "n": n,
                "method": "MILP",
                "time": milp_time,
                "solution_sum": milp_sum,
                "target": target
            })


        else:

            print("MILP did not find a solution.")

        # -------------------------
        # Local Search
        # -------------------------

        start = time.perf_counter()

        local_solution = local_search(
            numbers,
            target
        )

        end = time.perf_counter()

        local_time = end - start

        local_sum = sum(
            numbers[i]
            for i in range(len(numbers))
            if local_solution[i] == 1
        )

        print(
            f"Local Search: "
            f"{local_time:.6f} seconds"
        )

        print(
            f"Local Search solution sum: "
            f"{local_sum}"
        )
        results.append({
            "n": n,
            "method": "Local Search",
            "time": local_time,
            "solution_sum": local_sum,
            "target": target
        })

        # -------------------------
        # Simulated Annealing
        # -------------------------

        start = time.perf_counter()

        sa_solution = simulated_annealing(
            numbers,
            target
        )

        end = time.perf_counter()

        sa_time = end - start

        sa_sum = sum(
            numbers[i]
            for i in range(len(numbers))
            if sa_solution[i] == 1
        )

        print(
            f"Simulated Annealing: "
            f"{sa_time:.6f} seconds"
        )

        print(
            f"Simulated Annealing solution sum: "
            f"{sa_sum}"
        )
        results.append({
            "n": n,
            "method": "Simulated Annealing",
            "time": sa_time,
            "solution_sum": sa_sum,
            "target": target
        })

    # Save all benchmark results to CSV
    with open(
        results_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "n",
                "method",
                "time",
                "solution_sum",
                "target"
            ]
        )

        writer.writeheader()

        writer.writerows(results)

    print()
    print("Results saved to:")
    print(results_file)


if __name__ == "__main__":

    run_scalability_experiment()
    