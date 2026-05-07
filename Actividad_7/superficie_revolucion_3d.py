import numpy as np
import matplotlib.pyplot as plt

# Definimos el intervalo de x (0 a 2) y el ángulo de rotación (0 a 2pi)
x = np.linspace(0, 2, 50)
theta = np.linspace(0, 2*np.pi, 50)

# Creamos una malla (mesh) con x y theta
X, THETA = np.meshgrid(x, theta)

# Funciones de radio
R_interior = X**2
R_exterior = X**2 - 2*X + 4

# Coordenadas 3D para la superficie interior
Y_int = R_interior * np.cos(THETA)
Z_int = R_interior * np.sin(THETA)

# Coordenadas 3D para la superficie exterior
Y_ext = R_exterior * np.cos(THETA)
Z_ext = R_exterior * np.sin(THETA)

# Configuramos la gráfica 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficamos ambas superficies
ax.plot_surface(X, Y_int, Z_int, color='blue', alpha=0.5, label='Superficie Interior f(x)')
ax.plot_surface(X, Y_ext, Z_ext, color='red', alpha=0.3, label='Superficie Exterior g(x)')

# Configuraciones visuales
ax.set_title('Sólido de Revolución - Vista 3D')
ax.set_xlabel('Eje X (Longitud)')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
