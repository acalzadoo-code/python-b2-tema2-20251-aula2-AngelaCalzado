"""
Enunciado:
Explora el análisis de datos mediante la realización de una regresión lineal y la interpolación de un conjunto de datos.
Este ejercicio se centra en el uso de scipy.optimize para llevar a cabo una regresión lineal y en la aplicación de
scipy.interpolate para la interpolación de datos.

Implementa la función linear_regression_and_interpolation(data_x, data_y) que realice lo siguiente:
    - Regresión Lineal: Ajustar una regresión lineal a los datos proporcionados.
    - Interpolación: Crear una interpolación lineal de los mismos datos.

Adicionalmente, implementa la función plot_results(data_x, data_y, results) para graficar los datos originales,
la regresión lineal y la interpolación.

Parámetros:
    - data_x (List[float]): Lista de valores en el eje x.
    - data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    - results (Dict): Resultados de la regresión lineal e interpolación.

Ejemplo:
    - Entrada:
        data_x = np.linspace(0, 10, 100)
        data_y = 3 - data_x + 2 + np.random.normal(0, 0.5, 100) # Datos con tendencia lineal y algo de ruido
    - Ejecución:
        results = linear_regression_and_interpolation(data_x, data_y)
        plot_results(data_x, data_y, results)
    - Salida:
        Un gráfico mostrando los datos originales, la regresión lineal y la interpolación.
"""

from scipy.optimize import curve_fit
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import typing as t

def regresion(x, m, b):
    result = m*x + b
    return result

def linear_regression_and_interpolation(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Dict[str, t.Any]:
    # 1. Regresion lineal
    # curve_fit (function, xdata, ydata)
    popt, pcov = curve_fit(regresion, data_x, data_y)
    # devuelve popt (contiene los parámetros que ha encontrado para que la recta se ajuste lo mejor posible a los datos)
    ## popt[0]: pendiente y popt[1]: ordenada en el origen
    pendiente = popt[0]
    ordenada_origen = popt[1]
    
    # 2. Interpolacion
    # interpolate.interp1d(x,y) crea una función de interpolación a partir de nuestros datos
    interpolacion = interpolate.interp1d(data_x, data_y)
        
    # 3. Crear un diccionario con ambos apartados
    resultado = {
        "linear_regression": {
            "slope": pendiente,
            "intercept": ordenada_origen
        },
        "interpolated_data": interpolacion(data_x)
    }
    return resultado


def plot_results(data_x: t.List[float], data_y: t.List[float], results: t.Dict):
    # 1. Representar los puntos originales
    plt.scatter(data_x, data_y)
    
    # 2. Representar la regresión
    slope = results["linear_regression"]["slope"]
    intercept = results["linear_regression"]["intercept"]
    resultado_y = regresion(data_x, slope, intercept)
    plt.plot(data_x, resultado_y)
    
    # 3. Interpolación
    valores_y_interpolados = results["interpolated_data"]
    plt.plot(data_x, valores_y_interpolados)
    
    # 4. Mostrar en pantalla
    plt.show()

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
data_x = np.linspace(0, 10, 100)
data_y = 3 * data_x + 2 + np.random.normal(0, 2, 100)
results = linear_regression_and_interpolation(data_x, data_y)
plot_results(data_x, data_y, results)
