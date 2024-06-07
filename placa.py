import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L = 1.0  # Tamaño de la placa en metros
Nx = 100  # Número de puntos en el eje x
Ny = 100  # Número de puntos en el eje y
Nt = 100  # Número de instantes de tiempo
# Temperatura inicial de la placa
T = np.zeros((Nx, Ny, Nt))
T[:, :, 0] = 5  # Temperatura inicial

# Colores
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'



def temperatura_bordes():
    print(GREEN)
    T[0,:,:]= int(input("Ingrese la temperatura del borde uno: "))
    T[99,:,:]= int(input("Ingrese la temperatura del borde dos: "))
    T[:,0,:]= int(input("Ingrese la temperatura del borde tres: "))
    T[:,99,:]= int(input("Ingrese la temperatura del borde cuatro: "))
    print(RESET)

temperatura_bordes()

def calcular_distribucion_temperaturas():
    # Calcular la distribución de temperaturas en el interior de la placa para todos los instantes de tiempo
    for k in range(Nt - 1):
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                T[i, j, k + 1] = (T[i + 1, j, k] + T[i - 1, j, k] + T[i, j + 1, k] + T[i, j - 1, k]) / 4
    
    # Calcular la velocidad del incremento de temperatura en el punto medio de la placa
    dt = 1.0  # Suponiendo un incremento de tiempo de 1 unidad arbitraria
    dT_dt = (T[Nx // 2, Ny // 2, Nt - 1] - T[Nx // 2, Ny // 2, 0]) / (Nt * dt)

    # Calcular la temperatura promedio en cada instante de tiempo
    T_promedio = np.mean(T[:, :, :], axis=(0, 1))

    # Imprimir resultados
    print(BLUE, "Velocidad de temperatura en el punto medio de la placa:", RESET, dT_dt)
    print(BLUE,"Temperatura promedio de la placa por instante de tiempo: \n", RESET, T_promedio)

#Función para realizar la animación
def update(frame):
    ax.clear()
    ax.set_xlabel('Posición X (m)')
    ax.set_ylabel('Posición Y (m)')
    ax.set_zlabel('Temperatura (°C)')
    ax.set_title(f'Distribución de Temperaturas en 3D (X, Y, t = {frame})')
    ax.plot_surface(X, Y, T[:, :, frame], cmap='viridis')



def grafico2D():
    # Graficar la distribución de temperaturas bidimensional
    plt.imshow(T[:, :, -1], cmap='viridis', extent=[0, L, 0, L])
    plt.xlabel('Posición X (m)')
    plt.ylabel('Posición Y (m)')
    plt.title('Distribución de temperaturas')
    plt.colorbar()
    plt.show()


#Funcion que muestra en 3D el resultado final de la animación

def grafico3D():
    # Graficar la distribución de temperaturas en 3D para el último instante de tiempo
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, L, Nx)
    y = np.linspace(0, L, Ny)
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, T[:, :, -1], cmap='viridis')
    ax.set_xlabel('Posición X (m)')
    ax.set_ylabel('Posición Y (m)')
    ax.set_zlabel('Temperatura (°C)')
    plt.show()


calcular_distribucion_temperaturas()

x = np.linspace(0, L, Nx)
y = np.linspace(0, L, Ny)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, update, frames=Nt, repeat=False)

plt.show()

grafico2D()
grafico3D()

