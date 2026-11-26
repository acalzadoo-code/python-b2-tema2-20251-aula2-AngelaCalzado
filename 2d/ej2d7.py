"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de clustering utilizando
`sklearn.cluster.KMeans` en el conjunto de datos de crédito alemán. Este conjunto de datos contiene varias
características financieras y personales de los solicitantes de crédito, y el objetivo es agrupar a los solicitantes
en k clusters basados en sus características para identificar patrones y perfiles de riesgo.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_clustering(file_path: str)` que lee el archivo CSV y prepara los datos para
   el clustering, realizando cualquier limpieza o preprocesamiento necesario.
2. Realizar el clustering con KMeans: `perform_kmeans_clustering(data, n_clusters: int)` que aplica el algoritmo KMeans
   a los datos preparados, utilizando un número específico de clusters.
3. Visualizar los resultados: `visualize_clusters(data, labels, is_testing_execution)` que visualiza los resultados del
   clustering, idealmente utilizando una reducción de dimensionalidad para representar los datos en 2D o 3D si es
   posible.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de crédito alemán.
    n_clusters (int): Número de clusters a utilizar en el análisis KMeans.

Ejemplo:
    data = prepare_data_for_clustering('./data/german_credit_data.csv')
    labels = perform_kmeans_clustering(data, 5)
    visualize_clusters(data, labels, is_testing_execution)

Salida esperada:
    Una visualización de los clusters formados por el análisis KMeans, mostrando cómo se agrupan los solicitantes de
    crédito según sus características.
"""

from pathlib import Path
from typing import Tuple
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def prepare_data_for_clustering(file_path: str) -> pd.DataFrame:
    # Leer el csv
    df = pd.read_csv(file_path)
    
    # Eliminar la primera columna de índices del csv
    df = df.drop(columns=["Unnamed: 0"])
    
    # Sustituir los valores ausentes por "Unknown"
    df = df.fillna("Unknown")
    
    # Convertir las variables categóricas en numéricas
    text_column = df.select_dtypes(include="str").columns
    converted = pd.get_dummies(df, columns=text_column, dtype= int)
    
    # Utilizar StandardScaler para evitar darle más peso a los valores más grandes
    metodo = StandardScaler()
    # Aplicamos fit_transform() para calcular la media y la desviación estándar
    # de cada columna y estandarizar los datos.
    # Multiplicamos por un factor de corrección para adaptar la desviación
    # estándar poblacional utilizada por StandardScaler (ddof=0) a la
    # desviación estándar muestral que calcula pandas por defecto (ddof=1).
    # De esta forma, al comprobar la desviación estándar con pandas, obtenemos 1.
    res = metodo.fit_transform(converted) * np.sqrt((len(converted) - 1) / len(converted))
    
    # res devuelve un array de NumPy, pero nosotros necesitamos un df
    return pd.DataFrame(res, columns=converted.columns)


def perform_kmeans_clustering(data: np.ndarray, n_clusters: int) -> np.ndarray:
    # Crear el objeto KMeans
    k_means = KMeans(n_clusters=n_clusters)
    
    # Ajustar el modelo a los datos y obtener las etiquetas de los clusters.
    return k_means.fit_predict(data)


def visualize_clusters(
    data: np.ndarray, labels: np.ndarray, is_testing_execution: bool = False
) -> Tuple[np.ndarray, plt.Figure, plt.Axes]:
    # Creamos un objeto PCA indicando que queremos obtener dos componentes principales.
    pca = PCA(n_components=2)
    
    # Transformar los datos
    data_reduced = pca.fit_transform(data)
    
    # Crear figura y ejes
    fig, ax = plt.subplots()
    
    # Extraer X(PC1) e Y(PC2)
    # Seleccionamos todas las filas de la primera columna
    x_pc1 = data_reduced[:, 0]
    # Seleccionamos todas las filas de la segunda columna
    y_pc2 = data_reduced[:, 1]
    
    # Representar los clusters
    # El parámetro c permite asignar colores según los valores de la etiqueta
    ax.scatter(x_pc1, y_pc2, c=labels)
    
    # Añadir nombres a los ejes
    ax.set_xlabel("Componente principal 1 (PC1)")
    ax.set_ylabel("Componente principal 2 (PC2)")
    ax.set_title("Clustering de solicitantes de crédito mediante KMeans")
    
    # Comprobamos si NO estamos ejecutando los tests.
    # Si is_testing_execution es False, mostramos el gráfico en pantalla
    # mediante plt.show().
    if not is_testing_execution:
        plt.show()

    # Devolvemos siempre los objetos fig y ax, independientemente de si
    # hemos mostrado el gráfico o no.
    # Esto permite acceder posteriormente a la figura y a sus ejes,
    # además de facilitar su comprobación mediante los tests.
    return data_reduced, fig, ax


# Para probar el código, desconmenta las siguientes líneas
if __name__ == '__main__':
    current_dir = Path(__file__).parent
    file_path = current_dir / 'data/german_credit_data.csv'
    data = prepare_data_for_clustering(file_path)
    labels = perform_kmeans_clustering(data, 5)
    data_reduced, fig, ax = visualize_clusters(data, labels, False)
