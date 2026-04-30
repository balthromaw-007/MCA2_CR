import numpy as np
import scipy.linalg as la

# Matriz de coeficientes A y vector de resultados b
A = np.array([
    [-2, -3, 1, 2],
    [7, 6, 0, -3],
    [0, 3, 1, 5],
    [2, -2, 6, 6]
], dtype=float)

b = np.array([2, -4, 1, 8], dtype=float)

# Resolviendo el sistema (scipy usa pivoteo parcial por defecto en LU)
P, L, U = la.lu(A)
x = np.linalg.solve(A, b)

print("Matriz P (Intercambio de Renglones por Pivoteo):")
print(P)
print("\nVector Solución (x, y, z, w):")
for var, val in zip(['x', 'y', 'z', 'w'], x):
    print(f"{var} = {val:.4f}")
