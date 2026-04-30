import numpy as np
import matplotlib.pyplot as plt

# Definimos el intervalo de -pi/3 a pi/3
x = np.linspace(-np.pi/3, np.pi/3, 400)
y1 = 8 * np.cos(x)
y2 = 1 / (np.cos(x)**2) # equivalente a sec^2(x)

plt.figure(figsize=(8, 6))
# Graficamos las curvas
plt.plot(x, y1, label='y = 8 cos(x)', color='blue')
plt.plot(x, y2, label='y = sec^2(x)', color='red')

# Rellenamos el área entre las curvas
plt.fill_between(x, y1, y2, color='gray', alpha=0.3, label='Área (6√3)')

plt.title('Área entre y = 8 cos(x) y y = sec^2(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
