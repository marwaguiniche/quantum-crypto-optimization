# quantum-crypto-optimization
Exploration of quantum and classical methods applied to optimization problems in cryptography
# Quantum vs Classical Optimization for Cryptography-Inspired Problems

## 📌 Overview

This project explores and compares classical and quantum optimization methods on problems inspired by cryptographic applications.

The main objective is not to assume that quantum computing is superior, but to investigate experimentally when quantum approaches can be useful, where classical methods remain more effective, and what limitations arise in current quantum optimization methods.

The project focuses on the formulation of binary optimization problems and their transformation into QUBO and Ising models, followed by a comparison between classical optimization techniques and quantum algorithms such as QAOA.

---

## 🎯 Research Questions

The project investigates the following questions:

- How can cryptography-inspired optimization problems be formulated as binary optimization problems?
- How can these problems be transformed into QUBO and Ising formulations?
- How do classical optimization methods compare with quantum approaches such as QAOA?
- How does QAOA performance change with problem size and circuit depth?
- What is the impact of noise on quantum optimization results?
- Under which conditions, if any, can quantum methods become competitive with classical baselines?

---

## 🧠 Methods

### Classical optimization

The project will investigate:

- Mixed-Integer Linear Programming (MILP)
- Local Search
- Simulated Annealing
- Classical QUBO optimization

### Quantum optimization

The project will investigate:

- QUBO formulation
- Ising Hamiltonians
- Quantum Approximate Optimization Algorithm (QAOA)
- Quantum circuit simulation
- Noisy quantum simulation
- Quantum hardware experiments when accessible

---

## 🔬 Experimental Methodology

For each problem instance, classical and quantum methods will be evaluated using reproducible experiments.

The comparison will consider:

- Solution quality
- Optimality gap
- Feasibility
- Runtime
- Number of objective evaluations
- QAOA circuit depth
- Measurement probability distributions
- Noise sensitivity

Small instances will first be solved exactly when possible in order to establish reliable reference solutions.

---

## 🛠️ Technologies

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Qiskit
- PennyLane
- OR-Tools
- NetworkX

Additional optimization and benchmarking tools may be incorporated as the project develops.

---

## 📂 Project Structure

```text
quantum-classical-cryptographic-optimization/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── problem.py
│   ├── milp_solver.py
│   ├── local_search.py
│   ├── qubo.py
│   ├── ising.py
│   ├── qaoa_qiskit.py
│   └── qaoa_pennylane.py
│
├── experiments/
│
├── notebooks/
│
├── data/
│
├── figures/
│
├── tests/
│
└── docs/
