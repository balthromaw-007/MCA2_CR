import numpy as np
import matplotlib.pyplot as plt

# Definimos el intervalo de x de 1 a 2
x = np.linspace(1, 2, 200)

# Ecuación de la curva
y = (x**3 / 3) + (1 / (4 * x))

plt.figure(figsize=(8, 6))

# Graficamos la curva principal
plt.plot(x, y, label='y = x^3/3 + 1/(4x)', color='purple', linewidth=2.5)

# Puntos inicial y final para resaltar la longitud de arco
plt.scatter([1, 2], [(1**3/3) + 1/4, (2**3/3) + 1/8], color='red', zorder=5)
plt.text(1.05, 0.6, 'x=1', fontsize=12)
plt.text(1.9, 2.7, 'x=2', fontsize=12)

# Configuraciones visuales
plt.title('Longitud de Arco en el intervalo [1, 2]')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
