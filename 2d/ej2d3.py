"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de regresión lineal entre el número promedio
de habitaciones por vivienda (RM) y el valor medio de las viviendas ocupadas por sus propietarios (MEDV) en el conjunto
de datos de viviendas, utilizando `scipy.stats.linregress` y `matplotlib` para la visualización. El archivo CSV
'housing.csv' contiene datos relevantes para este análisis.

Las funciones a desarrollar son:
1. Realizar análisis de regresión lineal: `perform_linear_regression(data: pd.Dataframe, variable_1: str, variable_2: str)
que lee un archivo CSV y realiza una regresión lineal entre dos variables dadas, devolviendo la pendiente, la
intersección, el valor r, el valor p y el error estándar de la pendiente.
2. Graficar la regresión lineal y los puntos de datos: `plot_regression_line(data: pd.Dataframe, variable_1: str,
variable_2: str, slope: float, intercept: float)` que utiliza `matplotlib` para visualizar la línea de regresión lineal
junto con los puntos de datos de las dos variables seleccionadas.

Parámetros:
    data ( pd.Dataframe): Pandas dataframe que contiene los datos de vivienda.
    variable_1 (str): Nombre de la primera variable para el análisis de regresión (e.g., 'RM').
    variable_2 (str): Nombre de la segunda variable para el análisis de regresión (e.g., 'MEDV').
    slope (float): Pendiente de la línea de regresión lineal.
    intercept (float): Intersección de la línea de regresión lineal con el eje y.

Ejemplo de uso:
    slope, intercept, r_value, p_value, std_err = perform_linear_regression(data, 'RM', 'MEDV')
    plot_regression_line(data, 'RM', 'MEDV', slope, intercept)

Salida esperada:
    Una gráfica que muestra tanto los puntos de datos de RM vs MEDV como la línea de regresión lineal calculada.
"""

from pathlib import Path
import pandas as pd
from scipy.stats import linregress
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt


def perform_linear_regression(
    data: pd.DataFrame, variable_1: str, variable_2: str
) -> Tuple[float, float, float, float, float]:
    # 1. Seleccionar las dos columnas del DataFrame
    df_variable_1 = data[variable_1]
    df_variable_2 = data[variable_2]
    
    # 2. Realizar la regresión lineal con linregress()
    res = linregress(df_variable_1, df_variable_2)
    
    # 3. Recuperar los cinco resultados
    pendiente = res.slope
    intercepcion = res.intercept
    coeficiente_correlacion = res.rvalue
    pvalor = res.pvalue
    error_estandar = res.stderr
    
    # 4. Devolver los resultados en el orden solicitado
    return pendiente, intercepcion, coeficiente_correlacion, pvalor, error_estandar


def plot_regression_line(
    data: pd.DataFrame,
    variable_1: str,
    variable_2: str,
    slope: float,
    intercept: float,
    return_fig_ax_test=False,
):
    # 1. Recuperar las dos variables
    df_variable1 = data[variable_1]
    df_variable2 = data[variable_2]

    # 2. Crear figura y ejes
    fig, ax = plt.subplots()
    
    # 2.1. Representar los puntos con plt.scatter()
    # x representa RM e y representa MEDV.
    ax.scatter(df_variable1, df_variable2)

    # 2.2. Generar los valores X con np.linspace(inicio, final, num)
    valores_x = np.linspace(df_variable1.min(), df_variable1.max(), 1000)

    # 2.3. Calcular los valores Y utilizando la ecuación de la recta
    valores_y = slope * valores_x + intercept
    
    # 2.4. Representar la regresión lineal
    ax.plot(valores_x, valores_y)
    ax.set_title("Linear Regression between RM and MEDV")
    ax.set_xlabel(variable_1)
    ax.set_ylabel(variable_2)
    
    # Comprobamos si NO estamos ejecutando los tests.
    # Si return_fig_ax_test es False, mostramos el gráfico en pantalla
    # mediante plt.show().
    if not return_fig_ax_test:
        plt.show()

    # Devolvemos siempre los objetos fig y ax, independientemente de si
    # hemos mostrado el gráfico o no.
    # Esto permite acceder posteriormente a la figura y a sus ejes,
    # además de facilitar su comprobación mediante los tests.
    return fig, ax


# Para probar el código, descomenta este código
if __name__ == '__main__':
    current_dir = Path(__file__).parent
    HOUSING_CSV_PATH = current_dir / 'data/housing.csv'
    variable_1 = 'RM'
    variable_2 = 'MEDV'
    data = pd.read_csv(HOUSING_CSV_PATH, skiprows=14)

    slope, intercept, r_value, p_value, std_err = perform_linear_regression(data, variable_1, variable_2)

    print(f'Análisis de Regresión Lineal entre {variable_1} y {variable_2}:')
    print(f'Pendiente: {slope}, Intersección: {intercept}, Valor r: {r_value}, Valor p: {p_value},'
        f'Error estándar: {std_err}')

    # Graficar la línea de regresión
    fig, ax = plot_regression_line(data, variable_1, variable_2, slope, intercept, return_fig_ax_test=False)
