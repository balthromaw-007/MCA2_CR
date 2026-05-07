import numpy as np
import matplotlib.pyplot as plt

# Definimos el rango de y según la gráfica del problema
y = np.linspace(0, 2, 200)

# Ecuaciones de las curvas (x en función de y)
x_izquierda = (y**4 / 4) - (y**2 / 2)
x_derecha = (y**2 / 2)

plt.figure(figsize=(8, 6))

# Graficamos las curvas invirtiendo los ejes para que se vea como en tu PDF (y vertical, x horizontal)
plt.plot(x_izquierda, y, label='x = y^4/4 - y^2/2', color='blue')
plt.plot(x_derecha, y, label='x = y^2/2', color='red')

# Rellenamos el área entre las curvas
plt.fill_betweenx(y, x_izquierda, x_derecha, color='gray', alpha=0.3, label='Región a rotar')

# Marcamos el eje de rotación
plt.axhline(5, color='green', linestyle='--', linewidth=2, label='Eje de rotación (y=5)')

# Configuraciones visuales para igualar la Figura 1
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.title('Método de los Cascarones (Rotación respecto a y=5)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Ajustamos los límites de la gráfica para ver bien el eje de rotación
plt.ylim(-0.5, 5.5)
plt.show()
