"""
Comparison between classical and quantum approaches.
"""

import os
import pandas as pd


def compare_results():

    # -----------------------------------------
    # 1. Load classical results
    # -----------------------------------------

    classical_file = (
        "results/classical/scalability_results.csv"
    )

    classical_data = pd.read_csv(
        classical_file
    )

    # -----------------------------------------
    # 2. Load QAOA results
    # -----------------------------------------

    quantum_file = (
        "results/quantum/qaoa_scalability_results.csv"
    )

    quantum_data = pd.read_csv(
        quantum_file
    )

    # -----------------------------------------
    # 3. Keep only useful classical columns
    # -----------------------------------------

    classical_data = classical_data[
        [
            "n",
            "method",
            "time",
            "solution_sum",
            "target",
        ]
    ]

    # -----------------------------------------
    # 4. Prepare QAOA data
    # -----------------------------------------

    quantum_data["method"] = "QAOA"

    quantum_data["solution_sum"] = None

    quantum_data = quantum_data[
        [
            "n",
            "method",
            "time",
            "solution_sum",
            "target",
            "success_probability",
        ]
    ]

    # -----------------------------------------
    # 5. Add success probability to classical
    # -----------------------------------------

    classical_data["success_probability"] = (
        classical_data["solution_sum"]
        == classical_data["target"]
    ).astype(float)
    
    # -----------------------------------------
    # 6. Combine results
    # -----------------------------------------

    comparison = pd.concat(
        [
            classical_data,
            quantum_data,
        ],
        ignore_index=True,
    )

    # -----------------------------------------
    # 7. Create comparison directory
    # -----------------------------------------

    output_directory = (
        "results/comparison"
    )

    os.makedirs(
        output_directory,
        exist_ok=True,
    )

    # -----------------------------------------
    # 8. Save comparison
    # -----------------------------------------

    output_file = os.path.join(
        output_directory,
        "classical_vs_quantum.csv",
    )

    comparison.to_csv(
        output_file,
        index=False,
    )

    print()
    print("Comparison results saved to:")
    print(output_file)

    print()
    print(comparison)


if __name__ == "__main__":

    compare_results()