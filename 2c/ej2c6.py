"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de componentes principales (PCA) utilizando
`sklearn.decomposition.PCA` en el conjunto de datos de viviendas. Este conjunto de datos contiene varias características
de viviendas en áreas suburbanas de Boston, y el objetivo es reducir la dimensionalidad de los datos para identificar
las principales componentes que explican la mayor parte de la varianza en el conjunto de datos.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_pca(file_path: str)` que lee el archivo CSV y prepara los datos eliminando
cualquier característica no numérica. Se debe saltar las primeras 14 filas del archivo CSV, que contienen información
adicional sobre el conjunto de datos.
2. Realizar PCA: `perform_pca(data, n_components: int)` que realiza PCA en los datos preparados, reduciendo a
`n_components` número de dimensiones, en este caso a 4 dimensiones.
3. Visualizar los resultados: `plot_pca_results(pca)` que visualiza los resultados de PCA, incluyendo la varianza
explicada por cada componente principal.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de viviendas.
    n_components (int): Número de componentes principales a retener en el análisis PCA.

Ejemplo de uso:
    pca = perform_pca(data, 4)
    plot_pca_results(pca)

Salida esperada:
    Una visualización de la varianza explicada por los componentes principales y, opcionalmente, una transformación de
    los datos originales proyectada en las principales componentes.
"""

from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def prepare_data_for_pca(file_path: str) -> pd.DataFrame:
    # Lee el archivo csv y omite las primeras 14 filas
    df = pd.read_csv(file_path, skiprows=14)
    # Selecciona exclusivamente las columnas numéricas
    df = df.select_dtypes(include="number")
    
    # Eliminamos la columna MEDV, que representa la variable objetivo
    # (valor medio de las viviendas) y no debe incluirse como variable de entrada
    # en el análisis de componentes principales.
    df = df.drop(columns=["MEDV"])
    
    return df


def perform_pca(data: pd.DataFrame, n_components: int) -> PCA:
    # Creamos un objeto StandardScaler para estandarizar los datos
    # Esto es importante porque las variables pueden tener escalas y unidades diferentes.
    scaler = StandardScaler()
    
    # Ajustamos el escalador a los datos y los transformamos.
    # fit() calcula la media y la desviación estándar de cada columna.
    # transform() aplica la estandarización utilizando esos valores.
    # fit_transform() realiza ambas operaciones consecutivamente.
    # El resultado es una matriz NumPy con los datos estandarizados.
    datos_escalados = scaler.fit_transform(data)
    
    # Creamos un objeto PCA indicando el número de componentes principales
    # que queremos conservar en el análisis.
    pca = PCA(n_components=n_components)
    
    # Ajustamos el modelo PCA a los datos estandarizados.
    # Durante este proceso se identifican las direcciones de máxima varianza
    # y se calculan los componentes principales
    pca.fit(datos_escalados)
    
    # Devolvemos el objeto PCA ajustado, que contiene información sobre
    # los componentes principales y la proporción de varianza explicada.
    return pca


def plot_pca_results(pca: PCA) -> tuple:
    # Obtenemos la proporción de varianza explicada por cada componente principal.
    # Este atributo contiene un valor para cada componente del modelo PCA.
    explained_variance = pca.explained_variance_ratio_
    
    # Creamos una figura (fig) y unos ejes (ax) para representar los resultados.
    fig, ax = plt.subplots()
    
    # Creamos un gráfico de barras para visualizar la varianza explicada.
    # range(len(explained_variance)) genera una posición para cada componente.
    # explained_variance determina la altura de cada barra.
    ax.bar(x=range(len(explained_variance)), height=explained_variance)
    
    # Añadimos las etiquetas de los ejes para identificar la información representada.
    ax.set_xlabel("Componente principal")
    ax.set_ylabel("Proporción de varianza explicada")
    
    # Añadimos un título descriptivo al gráfico.
    ax.set_title("Varianza explicada por cada componente principal")
    
    # Devolvemos la figura y los ejes en forma de tupla.
    # Esto permite mostrar, modificar o guardar el gráfico desde fuera de la función.    
    return fig, ax


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/housing.csv"
    dataset = prepare_data_for_pca(FILE_PATH)
    pca = perform_pca(dataset, 4)
    _, _ = plot_pca_results(pca)
