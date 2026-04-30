import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# 1. Gráfica del Sistema C (2x2) - 2D
# ---------------------------------------------
x_vals = np.linspace(0, 5, 100)
# Ecuación 1: x + 2y = 3  =>  y = (3 - x) / 2
y1 = (3 - x_vals) / 2
# Ecuación 2: 2x + 4.0001y = 6.0001 => y = (6.0001 - 2x) / 4.0001
y2 = (6.0001 - 2*x_vals) / 4.0001

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label="x + 2y = 3", color='blue')
plt.plot(x_vals, y2, label="2x + 4.0001y = 6.0001", color='red', linestyle='--')
plt.title("Sistema (c) - Rectas casi paralelas (Mal Condicionado)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------
# 2. Gráfica del Sistema A (3x3 Hilbert) - 3D
# ---------------------------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear malla de puntos para x e y
x_grid, y_grid = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

# Despejando z de cada ecuación de la Matriz de Hilbert:
# Eq 1: x + 0.5y + 0.333z = 1    => z = (1 - x - 0.5y) * 3
z1 = (1 - x_grid - (1/2)*y_grid) * 3
# Eq 2: 0.5x + 0.333y + 0.25z = 0 => z = (0 - 0.5x - (1/3)y) * 4
z2 = (0 - (1/2)*x_grid - (1/3)*y_grid) * 4
# Eq 3: 0.333x + 0.25y + 0.2z = 0 => z = (0 - (1/3)x - 0.25y) * 5
z3 = (0 - (1/3)*x_grid - (1/4)*y_grid) * 5

ax.plot_surface(x_grid, y_grid, z1, alpha=0.5, color='cyan')
ax.plot_surface(x_grid, y_grid, z2, alpha=0.5, color='magenta')
ax.plot_surface(x_grid, y_grid, z3, alpha=0.5, color='yellow')

ax.set_title("Sistema (a) - Planos intersecándose (Hilbert)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# Nota: El sistema b) es de 4 variables (Hiperplanos en 4D), 
# por lo que no es posible graficarlo geométricamente en R2 o R3.
