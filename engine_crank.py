import numpy as np
import matplotlib.pyplot as plt

"""
Variables usadas:

d_piston: Diametro del piston 
r_motor: Radio cigueñal 
b_motor: Longitud biela
theta: Ángulos en radianes para 4 revoluciones (1440 grados)
omega: Velocidad angular (La cual es constante)

"""

def posicion_piston(theta, r_motor, b_motor):
    return r_motor * np.cos(theta) + np.sqrt(b_motor**2 - r_motor**2 * np.sin(theta)**2)

def velocidad_piston(r_motor, b_motor, theta, omega):
    return (r_motor*omega) * (np.sin(theta) + ((r_motor/b_motor) * np.sin(2*theta))/2 )

def aceleracion_piston(r_motor, b_motor, theta, omega):
    factor_escala = 1e4  # Para remover los ceros innecesarios 
    return (r_motor * omega**2) * (np.cos(theta) + ((r_motor/b_motor) * np.cos(2*theta)))/factor_escala

def volumen_camara_combustion(d_motor, r_motor, b_motor, theta):
    e = r_motor * (1-np.cos(theta))
    s = r_motor * ( np.sin(theta)  + (b_motor/r_motor) * np.sqrt( 1 - ((e - r_motor*np.cos(theta))/b_motor)**2))
    r_theta = r_motor * np.sin(theta) / (b_motor + r_motor * np.cos(theta))

    return ((np.pi / 4) * d_motor**2) * (s * (1 - r_theta))


def presion_piston(volumen,R,T):
    factor_escala = 1e4  # Para remover los ceros innecesarios 
    return (R*T/volumen)/factor_escala


def calcular_torque(d_piston, presion, b_motor, r_motor, theta):
    # Calcular el radio del pistón
    r_piston = d_piston / 2.0
    area_piston = np.pi * (r_piston**2)
    r_biela = b_motor * np.cos(theta)  # Longitud de la biela en función del ángulo
    
    # Fuerza ejercida por el pistón
    fuerza = presion * area_piston
    
    # Calcular los torques para los tres ejes
    torque_biela = fuerza * r_biela * np.sin(theta)
    torque_piston = fuerza * (r_biela + r_motor) * np.sin(theta)  # Longitud total del pistón es la suma de la biela y el cigüeñal
    torque_ciguenal = fuerza * r_motor * np.sin(theta)
    
    return torque_piston, torque_biela,  torque_ciguenal


def main():
    # Ingreso de dimensiones geométricas por el usuario
    d_piston = float(input("Ingrese el diámetro del pistón (en m): "))
    
    # Calcular el radio del motor (mitad del diámetro del pistón)
    r_motor = d_piston / 2.0
    
    # Ingreso de la longitud de la biela por el usuario
    b_motor = float(input("Ingrese la longitud de la biela (en m): "))
    
    # Velocidad angular constante en radianes por segundo (1750 rpm)
    omega = 1750 * 2 * np.pi / 60
    
    # Número de puntos para el gráfico (por revolución)
    num_points_per_revolution = 360
    
    # Ángulos en radianes para 4 revoluciones (1440 grados)
    theta = np.linspace(0, 4 * 2 * np.pi, 4 * num_points_per_revolution)
   

     # Calcular la posición vertical del pistón
    y = posicion_piston(theta, r_motor, b_motor)
    
    # Graficar la posición vs. el ángulo
    plt.plot(np.degrees(theta), y)
    plt.title('Posición del pistón vs. Ángulo de la manivela')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Posición vertical del pistón (m)')
    plt.grid(True)
    plt.show()

    v_ins = velocidad_piston(r_motor, b_motor, theta, omega)

    # Graficar la velocidad vs. el ángulo
    plt.plot(np.degrees(theta), v_ins)
    plt.title('Velocidad del pistón vs. Ángulo de la manivela')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Velocidad del pistón (m/s)')
    plt.grid(True)
    plt.show()

    a_ins = aceleracion_piston(r_motor, b_motor, theta, omega)

    # Graficar la aceleración vs. el ángulo
    plt.plot(np.degrees(theta), a_ins)
    plt.title('Aceleración del pistón vs. Ángulo de la manivela')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Aceleración del pistón (m/s^2)')
    plt.grid(True)
    plt.show()

    volumen = volumen_camara_combustion(d_piston, r_motor, b_motor, theta)

    # Graficar el volumen vs. el ángulo
    plt.plot(np.degrees(theta), volumen)
    plt.title('Volumen de la cámara vs. Ángulo de la manivela')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Volumen de la cámara (m^3)')
    plt.grid(True)
    plt.show()

    presion = presion_piston(volumen, R=286.9, T=300)
    
    # Graficar la presión vs. el ángulo
    plt.plot(np.degrees(theta), presion)
    plt.title('Presión de la cámara vs. Ángulo de la manivela')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Presión de la cámara (Pa)')
    plt.grid(True)
    plt.show()

    # Calcular área del pistón y torques para los tres ejes
    torque_piston, torque_biela, torque_ciguenal = calcular_torque(d_piston, presion, b_motor, r_motor, theta)
    
    # Graficar los torques vs. el ángulo
    plt.plot(np.degrees(theta), torque_piston, label='Torque en eje del pistón')
    plt.plot(np.degrees(theta), torque_biela, label='Torque en eje de la biela')
    plt.plot(np.degrees(theta), torque_ciguenal, label='Torque en eje del cigüeñal')
    
    plt.title('Torques en los ejes vs. Ángulo de la manivela')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Torque (Nm)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
