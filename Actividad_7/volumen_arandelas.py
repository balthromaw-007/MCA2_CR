import numpy as np
import matplotlib.pyplot as plt

# Rango de x para la gráfica general
x = np.linspace(-1, 3, 400)
f_x = x**2
g_x = x**2 - 2*x + 4

# Rango de x solo para el área sombreada (de 0 a 2)
x_fill = np.linspace(0, 2, 100)
f_x_fill = x_fill**2
g_x_fill = x_fill**2 - 2*x_fill + 4

plt.figure(figsize=(8, 6))

# Graficamos las funciones
plt.plot(x, f_x, label='f(x) = x^2 (Radio menor)', color='blue')
plt.plot(x, g_x, label='g(x) = x^2 - 2x + 4 (Radio mayor)', color='red')

# Sombreamos el área que va a rotar
plt.fill_between(x_fill, f_x_fill, g_x_fill, color='gray', alpha=0.3, label='Región a rotar')

# Ejes y detalles
plt.axvline(0, color='black', linewidth=1.5, linestyle='--', label='Eje y (x=0)')
plt.axhline(0, color='black', linewidth=1)
plt.title('Región a rotar - Método de Arandelas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
