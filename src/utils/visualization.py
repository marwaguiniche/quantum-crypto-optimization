"""
Visualization utilities for QAOA experiments.
"""

import os

import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


# ============================================================
# 1. QAOA PARAMETER GRID
# ============================================================

def plot_qaoa_parameter_grid(
    csv_file="results/quantum/qaoa_parameter_grid.csv",
    output_file="figures/convergence/qaoa_parameter_heatmap.png",
):
    """
    Plot QAOA success probability as a function
    of gamma and beta.
    """

    data = pd.read_csv(csv_file)

    matrix = data.pivot(
        index="gamma",
        columns="beta",
        values="success_probability",
    )

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True,
    )

    plt.figure(figsize=(8, 6))

    plt.imshow(
        matrix.values,
        origin="lower",
        aspect="auto",
    )

    plt.colorbar(
        label="Success Probability"
    )

    plt.xticks(
        range(len(matrix.columns)),
        matrix.columns,
    )

    plt.yticks(
        range(len(matrix.index)),
        matrix.index,
    )

    plt.xlabel("Beta")
    plt.ylabel("Gamma")

    plt.title(
        "QAOA Parameter Optimization"
    )

    plt.tight_layout()

    plt.savefig(
        output_file,
        dpi=300,
    )

    plt.close()

    print(
        "Figure saved to:",
        output_file,
    )


# ============================================================
# 2. CLASSICAL SCALABILITY
# ============================================================

def plot_classical_scalability(
    csv_file="results/classical/scalability_results.csv",
    output_file="figures/scalability/classical_scalability.png",
):
    """
    Plot execution time of classical algorithms
    as a function of problem size.
    """

    data = pd.read_csv(csv_file)

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True,
    )

    plt.figure(figsize=(9, 6))

    methods = data["method"].unique()

    for method in methods:

        method_data = data[
            data["method"] == method
        ]

        plt.plot(
            method_data["n"],
            method_data["time"],
            marker="o",
            label=method,
        )

    plt.xlabel("Problem Size (n)")
    plt.ylabel("Execution Time (seconds)")

    plt.title(
        "Classical Algorithms Scalability"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        output_file,
        dpi=300,
    )

    plt.close()

    print(
        "Figure saved to:",
        output_file,
    )


# ============================================================
# 3. QAOA SCALABILITY
# ============================================================

def plot_qaoa_scalability(
    csv_file="results/quantum/qaoa_scalability_results.csv",
    output_file="figures/scalability/qaoa_scalability.png",
):
    """
    Plot QAOA success probability
    for different problem sizes.
    """

    data = pd.read_csv(csv_file)

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True,
    )

    plt.figure(figsize=(8, 6))

    plt.plot(
        data["n"],
        data["success_probability"],
        marker="o",
    )

    plt.xlabel("Problem Size (n)")
    plt.ylabel("Success Probability")

    plt.title(
        "QAOA Scalability"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        output_file,
        dpi=300,
    )

    plt.close()

    print(
        "Figure saved to:",
        output_file,
    )


# ============================================================
# 4. CLASSICAL VS QUANTUM
# ============================================================

def plot_classical_vs_quantum(
    csv_file="results/comparison/classical_vs_quantum.csv",
    output_file="figures/comparison/classical_vs_quantum.png",
):
    """
    Compare execution time of classical methods
    with QAOA.
    """

    data = pd.read_csv(csv_file)

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True,
    )

    plt.figure(figsize=(9, 6))

    methods = data["method"].unique()

    for method in methods:

        method_data = data[
            data["method"] == method
        ]

        if method_data["time"].isna().all():
            continue

        plt.plot(
            method_data["n"],
            method_data["time"],
            marker="o",
            label=method,
        )

    plt.xlabel("Problem Size (n)")
    plt.ylabel("Execution Time (seconds)")

    plt.title(
        "Classical vs Quantum Scalability"
    )

    plt.yscale("log")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        output_file,
        dpi=300,
    )

    plt.close()

    print(
        "Figure saved to:",
        output_file,
    )


# ============================================================
# 5. QAOA NOISE
# ============================================================

def plot_qaoa_noise(
    csv_file="results/quantum/qaoa_noise_results.csv",
    output_file="figures/noise/qaoa_noise.png",
):
    """
    Plot QAOA success probability
    as a function of the error rate
    for different problem sizes.
    """

    import os

    # Load results
    data = pd.read_csv(csv_file)

    # Create output directory
    os.makedirs(
        "figures/noise",
        exist_ok=True
    )

    # Create figure
    plt.figure(figsize=(9, 6))

    # Plot one curve for each problem size
    for n in sorted(data["n"].unique()):

        subset = data[
            data["n"] == n
        ]

        plt.plot(
            subset["error_rate"],
            subset["success_probability"],
            marker="o",
            label=f"n = {n}",
        )

    plt.xlabel("Error Rate")
    plt.ylabel("Success Probability")

    plt.title(
        "QAOA Performance Under Noise"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        output_file,
        dpi=300,
    )

    print(
        "Figure saved to:",
        output_file,
    )



# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Generating final project figures")
    print("=" * 60)

    print()

    plot_qaoa_parameter_grid()

    plot_classical_scalability()

    plot_qaoa_scalability()

    plot_classical_vs_quantum()

    plot_qaoa_noise()

    print()
    print("=" * 60)
    print("All figures generated successfully.")
    print("=" * 60)