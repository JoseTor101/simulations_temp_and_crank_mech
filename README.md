El repositorio contiene los siguientes elementos:

- placa.py
- engine_crank.py

## Placa.py

Para la primera Se desea conocer el cambio de temperatura en el interior de una placa plana cuadrada, con un tamaño de 1m, para puntos en su interior cada 1 cm. La expresión del comportamiento de la temperatura para cualquier punto en el interior se indica en la siguiente ecuación:

![f1](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f1.jpg)

Encuentre:

1. La distribución de temperaturas en el interior de la placa para cualquier
instante de tiempo.
2. La velocidad del incremento de temperatura para el punto medio de la placa.
(se puede calcular como el cambio de temperatura por unidad de tiempo)
3. La temperatura promedio de la placa para cualquier instante de tiempo y su
ubicación aproximada.
4. Grafique la distribución de temperaturas tridimensional bidimensionalmente
para cada incremento del tiempo.

Para la solución planteada, encontramos que la manera más sencilla de implementar la solución era modificando la manera en que planteábamos la ecuación, de:
![f1](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f1.jpg)

A la siguiente:
![f2](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f2.jpg)


La velocidad del incremento de temperatura para el punto medio de la placa la obtenemos a partir de la siguiente fórmula:

![f3](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f3.jpg)

**RESULTADOS**

![Gráfica 1a](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/placa_out_consola.jpg)
![Gráfica 2a](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/placa_out_2d.png)
![Gráfica 3a](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/placa_out_3d.png)

## Engine_crank.py

Simula el comportamiento de un mecanismo de biela-manivela en un motor a través del cálculo de la posición, velocidad, aceleración, volumen y presión del pistón en función del ángulo de la manivela. Posteriormente, se agrega una sección para calcular y graficar los torques en los ejes de la biela, el pistón y el cigüeñal.

Las fórmulas proporcionadas para la posición, velocidad y aceleración del pistón son independientes del cilindraje del motor (CC). Estas ecuaciones modelan el comportamiento del pistón y la biela en función de la geometría del motor y la velocidad angular. No hay una dependencia directa de la cilindrada en estas ecuaciones.

**FÓRMULAS UTILIZADAS:**

Donde **r_motor** = Longitud del cigüeñal

**B_motor** = longitud de la Biela

**Posición del Pistón:**

![f4](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f4.jpg)

**Velocidad del Pistón:**

![f5](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f5.jpg)

**Aceleración del Pistón:**

![f6](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f6.jpg)

**Volumen de la cámara de combustión:**

![f7](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f7.jpg)

O de manera más simplificada

![f8](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f8.jpg)

donde
![f9](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f9.jpg)

y
![f10](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f10.jpg)


**Presión del pistón:**

![f11](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f11.jpg)

**Torques en los ejes**

![f12](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/f12.jpg)


**EJEMPLO**
Para un diámetro de pistón de 0.5m y una longitud de biela de 2m:

**Gráfica 1:** Posición pistón vs Angulo de la manivela:

![Gráfica 1](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/1_pos_vs_angle.jpg)

**Gráfica 2:** Velocidad del pistón vs Angulo de la manivela

![Gráfica 2](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/2_speed_vs_angle.jpg)

**Gráfica 3:** Aceleración Vs Ángulo de la manivela

![Gráfica 3](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/3_acel_vs_angle.jpg)
 
**Gráfica 4:** Volumen de la cámara Vs Ángulo de la manivela

![Gráfica 4](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/4_vol_vs_angle.jpg)

**Gráfica 5:** Presión de la cámara Vs Ángulo de la manivela
![Gráfica 5](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/5_press_vs_angle.jpg)

**Gráfica 6:** Torque en los ejes Vs Ángulo de la manivela
![Gráfica 6](https://github.com/JoseTor101/simulations_temp_and_crank_mech/blob/master/imgs/6_torq_vs_angle.jpg)




## Referencias

Nigus, H. (2015). "Kinematics and Load Formulation of Engine Crank Mechanism." *Mechanics, Materials Science & Engineering.* [DOI](https://doi.org/10.13140/rg.2.1.3257.1928)

Ranjbarkohan, M., Rasekh, M., Hoseini, A. H., Kheiralipour, K., & Asadi, M. R. (2011). "Kinematics and kinetic analysis of the slider-crank mechanism in Otto linear four cylinder Z24 engine." *Mechanical Engineering Research,* 3(3), 85-95. [DOI](https://doi.org/10.5897/jmer.9000033)

Kwak, S. W., Shim, J. K., & Mo, Y. K. (2020). "Kinematic conceptual design of In-Line Four-Cylinder variable compression ratio engine mechanisms considering vertical second harmonic acceleration." *Applied Sciences,* 10(11), 3765. [DOI](https://doi.org/10.3390/app10113765)
