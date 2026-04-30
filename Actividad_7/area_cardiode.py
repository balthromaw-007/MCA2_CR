import numpy as np
import matplotlib.pyplot as plt

# Para graficar, asumimos que la constante 'a' vale 1
a = 1 
# El lóbulo superior va de 0 a pi
t = np.linspace(0, np.pi, 500) 

x = a * (2 * np.cos(t) - np.cos(2*t))
y = a * (2 * np.sin(t) - np.sin(2*t))

plt.figure(figsize=(8, 6))
# Graficamos y rellenamos el lóbulo superior
plt.plot(x, y, label='Cardiode (Mitad superior)', color='purple')
plt.fill_between(x, y, 0, color='purple', alpha=0.2, label='Área con el eje x (3πa²)')

# Dibujamos la cardiode completa en línea punteada para dar contexto
t_full = np.linspace(0, 2*np.pi, 1000)
x_full = a * (2 * np.cos(t_full) - np.cos(2*t_full))
y_full = a * (2 * np.sin(t_full) - np.sin(2*t_full))
plt.plot(x_full, y_full, color='purple', linestyle='--', alpha=0.3)

plt.title('Área de la Cardiode con el Eje X')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.axis('equal') # Para que no se deforme la curva
plt.legend()
plt.grid(True)
plt.show()
