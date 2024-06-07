El repositorio contiene los siguientes elementos:

- placa.py
- engine_crank.py

## Placa.py

Para la primera Se desea conocer el cambio de temperatura en el interior de una placa plana cuadrada, con un tamaño de 1m, para puntos en su interior cada 1 cm. La expresión del comportamiento de la temperatura para cualquier punto en el interior se indica en la siguiente ecuación:

T_{i,j}^k=\frac{T_{i+1,j}^{k-1}+T_{i-1,j}^{k-1}+T_{i,j+1}^{k-1}+T_{i,j-1}^{k-1}}{4}

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
T_{i,j}^k=\frac{T_{i+1,j}^{k-1}+T_{i-1,j}^{k-1}+T_{i,j+1}^{k-1}+T_{i,j-1}^{k-1}}{4}

A la siguiente:
T_{i,j}^{k+1}=\frac{T_{i+1,j}^k+T_{i-1,j}^k+T_{i,j+1}^k+T_{i,j-1}^k}{4}


La velocidad del incremento de temperatura para el punto medio de la placa la obtenemos a partir de la siguiente fórmula:

\frac{\partial T}{\partial t}=\frac{T\left[\frac{\left(Nx,Ny\right)}{2},tf\right]-T\left[\frac{\left(Nx,Ny\right)}{2},t0\right]}{Nt\cdot d t}

**RESULTADOS**

![Gráfica 1a](img/placa_out_2d.png)
![Gráfica 2a](img/placa_out_3d.png)
![Gráfica 3a](img/placa_out_consola.jpg)

## Engine_crank.py

Simula el comportamiento de un mecanismo de biela-manivela en un motor a través del cálculo de la posición, velocidad, aceleración, volumen y presión del pistón en función del ángulo de la manivela. Posteriormente, se agrega una sección para calcular y graficar los torques en los ejes de la biela, el pistón y el cigüeñal.

Las fórmulas proporcionadas para la posición, velocidad y aceleración del pistón son independientes del cilindraje del motor (CC). Estas ecuaciones modelan el comportamiento del pistón y la biela en función de la geometría del motor y la velocidad angular. No hay una dependencia directa de la cilindrada en estas ecuaciones.

**FÓRMULAS UTILIZADAS:**

Donde **r_motor** = Longitud del cigüeñal
**B_motor** = longitud de la Biela

**Posición del Pistón:**
y=r_{\mathrm{motor}}\cos{\left(\theta\right)}+\sqrt{b_{\mathrm{motor}}^2-r_{\mathrm{motor}}^2\sin^2{\left(\theta\right)}}

**Velocidad del Pistón:**
v=r_{\mathrm{motor}}\omega\left(\sin{\left(\theta\right)}+\frac{r_{\mathrm{motor}}}{b_{\mathrm{motor}}}\sin{\left(2\theta\right)}\right)

**Aceleración del Pistón:**
a=\left(r_{\mathrm{motor}}\omega^2\right)\left(\cos{\left(\theta\right)}+\frac{r_{\mathrm{motor}}}{b_{\mathrm{motor}}}\cos{\left(2\theta\right)}\right)


**Volumen de la cámara de combustión**
V=\frac{\pi}{4}d_{\mathrm{motor}}^2\left(r_{\mathrm{motor}}\left(1-\cos{\left(\theta\right)}\right)\cdot\left(\sin{\left(\theta\right)}+\frac{b_{\mathrm{motor}}}{r_{\mathrm{motor}}}\sqrt{1-\left(\frac{e-r_{\mathrm{motor}}\cos{\left(\theta\right)}}{b_{\mathrm{motor}}}\right)^2}\right)\cdot\left(1-\frac{r_{\mathrm{motor}}\sin{\left(\theta\right)}}{b_{\mathrm{motor}}+r_{\mathrm{motor}}\cos{\left(\theta\right)}}\right)\right)
O de manera más simplificada

V=\frac{\pi}{4}d_{\mathrm{motor}}^2\left(r_{\mathrm{motor}}\left(1-\cos{\left(\theta\right)}\right)\cdots\cdot\left(1-\frac{r_{\mathrm{motor}}\sin{\left(\theta\right)}}{b_{\mathrm{motor}}+r_{\mathrm{motor}}\cos{\left(\theta\right)}}\right)\right)

donde
s=r_{\mathrm{motor}}\left(\sin{\left(\theta\right)}+\frac{b_{\mathrm{motor}}}{r_{\mathrm{motor}}}\sqrt{1-\left(\frac{e-r_{\mathrm{motor}}\cos{\left(\theta\right)}}{b_{\mathrm{motor}}}\right)^2}\right)

y
e=r_{\mathrm{motor}}\left(1-\cos{\left(\theta\right)}\right)


**Presión del pistón**
P=\frac{R\cdotT}{\mathrm{V}}
	Torques en los ejes
\mathrm{T_biela}=\mathrm{F}\cdotb_{motor}\sin{\left(\theta\right)}
\mathrm{T_piston}=\mathrm{F}\cdot\left(b_{\mathrm{motor}}+r_{\mathrm{motor}}\right)\sin{\left(\theta\right)}
\mathrm{T_ciguenal}=\mathrm{F}\cdotr_{\mathrm{motor}}\sin{\left(\theta\right)}


**EJEMPLO**
Para un diámetro de pistón de 0.5m y una longitud de biela de 2m:

**Gráfica 1:** Posición pistón vs Angulo de la manivela:
![Gráfica 1](img/1_pos_vs_angle.jpg)

**Gráfica 2:** Velocidad del pistón vs Angulo de la manivela
![Gráfica 2](img/2_speed_vs_angle.jpg)

**Gráfica 3:** Aceleración Vs Ángulo de la manivela
![Gráfica 3](img/3_acel_vs_angle.jpg)
 
**Gráfica 4:** Volumen de la cámara Vs Ángulo de la manivela
![Gráfica 4](img/4_vol_vs_angle.jpg)

**Gráfica 5:** Presión de la cámara Vs Ángulo de la manivela
![Gráfica 5](img/5_press_vs_angle.jpg)

**Gráfica 6:** Torque en los ejes Vs Ángulo de la manivela
![Gráfica 6](img/6_torq_vs_angle.jpg)




## Referencias

Nigus, H. (2015). "Kinematics and Load Formulation of Engine Crank Mechanism." *Mechanics, Materials Science & Engineering.* [DOI](https://doi.org/10.13140/rg.2.1.3257.1928)

Ranjbarkohan, M., Rasekh, M., Hoseini, A. H., Kheiralipour, K., & Asadi, M. R. (2011). "Kinematics and kinetic analysis of the slider-crank mechanism in Otto linear four cylinder Z24 engine." *Mechanical Engineering Research,* 3(3), 85-95. [DOI](https://doi.org/10.5897/jmer.9000033)

Kwak, S. W., Shim, J. K., & Mo, Y. K. (2020). "Kinematic conceptual design of In-Line Four-Cylinder variable compression ratio engine mechanisms considering vertical second harmonic acceleration." *Applied Sciences,* 10(11), 3765. [DOI](https://doi.org/10.3390/app10113765)
