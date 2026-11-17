"""
Enunciado:

Explora el análisis avanzado de datos y la aplicación de ajustes no lineales mediante el uso de SciPy. Este ejercicio se
centra en ajustar una función gaussiana a un conjunto de datos usando el módulo scipy.optimize.curve_fit y en calcular
la integral de esta curva con scipy.integrate.quad.

Implementar la función gaussian_fit_and_integration(data_x, data_y) que realice lo siguiente:
    Ajuste de Curva Gaussiana: Utilizar scipy.optimize.curve_fit para ajustar una curva gaussiana a los datos.
    Integración Numérica: Calcular la integral de la curva gaussiana ajustada sobre el rango de data_x utilizando
    scipy.integrate.quad.

Además, implementar la función plot_gaussian_fit(data_x, data_y, gaussian_params) para visualizar los datos originales
y la curva gaussiana ajustada.

Parámetros:
    data_x (List[float]): Lista de valores en el eje x.
    data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    gaussian_params (Tuple[float]): Parámetros (amplitud, centro, ancho) de la curva gaussiana ajustada.

Ejemplo:
    Entrada:
        data_x = np.linspace(-5, 5, 100)
        data_y = 3 * np.exp(-(data_x - 1)**2 / (2 * 1.5**2)) + np.random.normal(0, 0.2, 100)
    Ejecución:
        gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
        plot_gaussian_fit(data_x, data_y, gaussian_params)
    Salida:
        Un gráfico mostrando los datos originales y la curva gaussiana ajustada.
        La integral de la curva gaussiana ajustada.
"""

from scipy import optimize, integrate
import numpy as np
import matplotlib.pyplot as plt
import typing as t


def gaussian(x: float, amplitude: float, mean: float, stddev: float) -> float:
    # ** se utiliza para elevar y np.exp se usa para elevar e a lo que hay dentro del paréntesis
    funcion = amplitude * np.exp(-(x - mean)**2 / (2 * stddev**2))
    return funcion

def gaussian_fit_and_integration(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Tuple[t.Tuple[float], float]:
    # 1. Calcular gaussiana
    # curve_fit (function, xdata, ydata)
    popt, pcov = optimize.curve_fit(gaussian, data_x, data_y)
    # devuelve popt (contiene los parámetros óptimos que ha encontrado para ajustar la curva)
    ## popt[0]: amplitud, popt[1]: media y popt[2]: desviación estándar
    amplitud = popt[0]
    media = popt[1]
    desviacion = popt[2]
    
    # 2. Integrar
    # lambda crea una función anónima que recibe un valor x
    # Cada vez que se evalúa la función, cambia x, así conseguimos que quad pueda
    # calcular el área bajo nuestra curva ajustada
    funcion_lambda = lambda x: gaussian(x, amplitud, media, desviacion)
    # integrate.quad(funcion, a, b), a: límite inferior, b: límite superior
    # integral: valor numérico que estima SciPy para el área bajo la curva
    # error: una estimación del error absoluto que podría tener ese resultado debido al método de integración numérica
    integral, error = integrate.quad(funcion_lambda, np.min(data_x), np.max(data_x))
    
    return popt, integral


def plot_gaussian_fit(
    data_x: t.List[float], data_y: t.List[float], gaussian_params: t.Tuple[float]
):
    # np.linspace genera valores equidistantes entre el mínimo y el máximo del conjunto de datos
    # np.linspace(inicio, fin, número_de_valores) --> para generar una línea suave
    x_smooth = np.linspace(np.min(data_x), np.max(data_x), 1000)
    # * sirve para desempaquetar gaussian_params
    y_smooth = gaussian(x_smooth, *gaussian_params)
    # 1. Representar con puntos los datos originales
    plt.scatter(data_x, data_y)
    
    # 2. Representar con una línea los datos ajustados
    plt.plot(x_smooth, y_smooth)
    
    # 3. Mostrar en pantalla
    plt.show()


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
data_x = np.linspace(-5, 5, 100)
data_y = 3 * np.exp(-(data_x - 1) ** 2 / (2 * 1.5 ** 2)) + np.random.normal(0, 0.2, 100)
gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
print("Integral de la curva gaussiana ajustada:", integral)
plot_gaussian_fit(data_x, data_y, gaussian_params)
