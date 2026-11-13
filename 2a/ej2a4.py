"""
Enunciado:
Desarrolla la función enhanced_compare_monthly_sales para visualizar y analizar datos de ventas de tres años distintos
utilizando la biblioteca Matplotlib. Esta función debe crear gráficos para comparar las ventas mensuales de dos años y
mostrar la distribución de las ventas de un tercer año.

Detalles de la Implementación:

    Gráfico de Barras y Líneas:
        Crea un gráfico de barras para comparar las ventas mensuales de los dos primeros años.
        Superpone un gráfico de líneas en el mismo eje para mostrar las ventas acumuladas de estos dos años.
        Utiliza ejes gemelos para manejar las escalas de los gráficos de barras y líneas adecuadamente.

    Gráfico de Pastel en Subfigura:
        Presenta las ventas del tercer año en un gráfico de pastel en una subfigura separada, mostrando la distribución
        porcentual de las ventas por mes.

Parámetros de la Función:
    sales_year1 (List[int]): Lista de ventas mensuales para el primer año.
    sales_year2 (List[int]): Lista de ventas mensuales para el segundo año.
    sales_year3 (List[int]): Lista de ventas mensuales para el tercer año.
    months (List[str]): Lista de nombres de los meses.

Especificaciones de los Gráficos:
    Gráfico de Barras y Líneas:
        Título: "Comparación de Ventas Mensuales: 2020 vs 2021"
        Ejes:
            Eje X: Nombres de los meses.
            Eje Y izquierdo: Ventas mensuales.
            Eje Y derecho: Ventas acumuladas.
        Leyendas para diferenciar cada año y las ventas acumuladas.

    Gráfico de Pastel:
        Título: "Distribución de Ventas Mensuales para 2022"
        Etiquetas para cada segmento del pastel, mostrando el porcentaje de ventas por mes.

Ejemplo:
    Entrada:
        sales_2020 = [120, 150, 180, 200, ...] # Ventas para cada mes en 2020
        sales_2021 = [130, 160, 170, 210, ...] # Ventas para cada mes en 2021
        sales_2022 = [140, 155, 175, 190, ...] # Ventas para cada mes en 2022
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    Ejecución:
        enhanced_compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    Salida:
        Dos gráficos dentro de la misma figura, uno combinando barras y líneas para 2020 y 2021, y otro en forma de
        pastel para 2022.
"""

import matplotlib.pyplot as plt
import numpy as np
import typing as t


def compare_monthly_sales(
    sales_year1: list, sales_year2: list, sales_year3: list, months: list
) -> t.Tuple[plt.Figure, plt.Axes, plt.Axes]:
    # Primero creamos la figura y sus dos zonas independientes
    # plt.subplots(filas, columnas)
    # fig: figura completa, ax1: primer gráfico, ax2: segundo gráfico
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    # Creamos un segundo eje Y sobre el primero para evitar aplastar por la escala
    # ax1 gráfico de barras y eje Y izquierdo
    # ax1_twin gráfico de líneas y eje Y derecho
    # ax2 gráfico de pastel
    ax1_twin = ax1.twinx()
    
    # ax1.bar(x, height), x: posiciones horizontales de las barras. height: altura de cada barra
    ## Primero creamos las posiciones de los meses
    x = np.arange(len(months))
    ## El -0.2 y +0.2 es para separar las barras de cada año y que no se solapen en la misma posición
    ### Para añadir una leyenda se usa label
    ax1.bar(x - 0.2, sales_year1, label ="2020")
    ax1.bar(x + 0.2, sales_year2, label ="2021")
    
    # Calculamos la suma acumulada de elementos de cada año
    suma_year1 = np.cumsum(sales_year1)
    suma_year2 = np.cumsum(sales_year2)
    # ax1_twin.plot(x, y) x: posiciones de los meses, y_ valores que queremos representar
    ax1_twin.plot(x, suma_year1, label ="2020")
    ax1_twin.plot(x, suma_year2, label ="2021")
    
    # set_xticks() establece las posiciones y set_xticklabels() asigna los nombres
    ax1.set_xticks(x)
    ax1.set_xticklabels(months)
    # Para establecer el título ax1.set_title("...")
    ax1.set_title("Monthly Sales Comparison: 2020 vs 2021")
    # Para etiquetar los ejes:
    ax1.set_xlabel("Meses")
    ax1.set_ylabel("ventas mensuales")
    ax1_twin.set_ylabel("ventas acumuladas")
    
    # Combinar las leyendas
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax1_twin.get_legend_handles_labels()
    ax1.legend(handles1 + handles2, labels1 + labels2)
    
    # Creamos el gráfico de pastel, autopct muestra automáticamente los porcentajes (1 decimal y el símbolo %)
    ax2.pie(sales_year3, labels=months, autopct="%1.1f%%")
    # Ponemos el título
    ax2.set_title("2022 Monthly Sales Distribution")
    
    return fig, ax1, ax2


# Para probar el código, descomenta las siguientes líneas
sales_2020 = np.random.randint(100, 500, 12)
sales_2021 = np.random.randint(100, 500, 12)
sales_2022 = np.random.randint(100, 500, 12)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


if __name__ == "__main__":
    fig, ax1, ax2 = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    plt.show()
