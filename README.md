# Ejercicios-Clasificaci-n-con-Algoritmo-AQ---Autos-El-ctricos-y-Socio-Activo-de-Gimnasio

Este proyecto contiene dos ejercicios prácticos de clasificación utilizando el **algoritmo AQ en Python**.

El objetivo es analizar ejemplos positivos y negativos para identificar características distintivas y generar reglas de clasificación.

## Ejercicio 1: Compra de automóvil eléctrico

Se analizaron clientes de una concesionaria utilizando los atributos:

- Edad
- Ingreso
- Tiene garaje
- Distancia al trabajo

El algoritmo compara los valores de los ejemplos positivos (clientes que compraron un automóvil eléctrico) con los negativos (clientes que no lo compraron).

### Regla obtenida

```text id="v5xqmo"
SI tiene_garaje = Si
ENTONCES Compra_Auto_Electrico = Sí
```

La característica que permite diferenciar los ejemplos es `tiene_garaje`, ya que todos los ejemplos positivos tienen garaje y los negativos no.

## Ejercicio 2: Socio activo de un gimnasio

Se analizaron socios de un gimnasio utilizando los atributos:

- Edad
- Frecuencia de asistencia
- Plan contratado

El algoritmo compara los valores presentes en los ejemplos positivos y negativos para encontrar aquellos que permiten diferenciarlos.

### Regla obtenida

```text id="ejvsvy"
SI frecuencia = frecuente
Y plan = premium
ENTONCES Socio_Activo = Sí
```

También se detecta `edad = 45` como un valor exclusivo de los ejemplos positivos, aunque no es necesario para construir la regla general.

## Funcionamiento del programa

1. Se cargan los ejemplos positivos y negativos.
2. Se analizan los atributos.
3. Se comparan los valores de cada atributo.
4. Se identifican los valores exclusivos de los ejemplos positivos.
5. Se genera una regla de clasificación utilizando el formato `SI - ENTONCES`.

## Tecnología utilizada

- Python
- Algoritmo AQ
