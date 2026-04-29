import numpy as np

# --- Sistema a) Matriz de Hilbert 3x3 ---
A_hilbert = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

evals_a, evecs_a = np.linalg.eig(A_hilbert)

print("--- Sistema a) Matriz de Hilbert ---")
print("Eigenvalores:\n", evals_a)
print("Eigenvectores (columnas):\n", evecs_a)
print("\n" + "="*40 + "\n")

# --- Sistema b) Matriz de Vandermonde 4x4 ---
A_vandermonde = np.array([
    [1, 1, 1, 1],
    [1.01, 1.02, 1.03, 1.04],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
])

evals_b, evecs_b = np.linalg.eig(A_vandermonde)

print("--- Sistema b) Matriz de Vandermonde ---")
print("Eigenvalores:\n", evals_b)
print("Eigenvectores (columnas):\n", evecs_b)

