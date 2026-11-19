"""
Enunciado:
Desarrolla un conjunto de funciones para realizar análisis estadístico sobre un conjunto de datos de calificaciones de
estudiantes utilizando Pandas. El objetivo es proporcionar una visión comprensiva del rendimiento de los estudiantes a
través del análisis de sus calificaciones almacenadas en un archivo CSV. Para ello, se compararán dos enfoques de
análisis descriptivo: uno mediante una función personalizada y otro utilizando la función describe de Pandas.

Las funciones a desarrollar son:
- Leer un archivo CSV y convertirlo en un DataFrame:
    read_csv_basic(file_path: str) -> pd.DataFrame
- Realizar una descripción estadística personalizada del DataFrame:
    custom_dataframe_describe(df: pd.DataFrame) -> pd.DataFrame
    Esta función debe calcular la media, mediana, desviación estándar, mínimo, máximo, y los cuartiles del DataFrame
    proporcionado.
- Utilizar la función describe de Pandas para obtener estadísticas descriptivas del DataFrame:
    pandas_dataframe_describe(df: pd.DataFrame) -> pd.DataFrame

Parámetros:
- file_path (str): Ruta del archivo CSV que contiene los datos de calificaciones.
- df (pd.DataFrame): DataFrame de pandas que contiene los datos.

Ejemplo:
    archivo_csv_path = 'data/grades.csv'
    dataframe = read_csv_basic(archivo_csv_path)

    print("Custom DataFrame:")
    print(custom_dataframe_describe(dataframe))

    print("\nDataFrame with Pandas:")
    print(pandas_dataframe_describe(dataframe))

Salida esperada:
- DataFrame que muestra la descripción estadística realizada manualmente de las calificaciones, incluyendo la media,
mediana, desviación estándar, mínimo, máximo, y los cuartiles para cada columna del conjunto de datos.
- DataFrame generado por la función describe de Pandas, que proporciona un resumen estadístico similar al anterior,
facilitando la comparación entre ambos enfoques.
"""

from pathlib import Path
import pandas as pd
import numpy as np


def read_csv_basic(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def custom_dataframe_describe(df: pd.DataFrame) -> pd.DataFrame:
    # Seleccionamos únicamente las columnas numéricas del DataFrame,
    # ya que las estadísticas como la media o la desviación estándar
    # no pueden calcularse sobre columnas de texto.
    # select_dtypes permite seleccionar columnas según su tipo de dato
    # include="number" indica que queremos conservar únicamente las columnas numéricas
    df = df.select_dtypes(include="number")
    
    # Calculamos las estadísticas descriptivas de cada columna
    media = df.mean()
    mediana = df.median()
    ds = df.std()
    minimum = df.min()
    maximum = df.max()
    cuartiles = df.quantile([0.25, 0.50, 0.75])
    
    # Concatenamos las estadísticas verticalmente para formar el DataFrame
    df_resultado = pd.concat(
        [
            # Convertimos cada una de las estadísticas (series) en un DataFrame mediante to_frame()
            # y utilizamos .T para transponerlo, de forma que cada estadística
            # quede representada en una fila y las asignaturas en columnas.
            # Después, rename() cambia el índice 0 por el nombre de la estadística.
            media.to_frame().T.rename(index={0:"mean"}),
            mediana.to_frame().T.rename(index={0: "median"}),
            ds.to_frame().T.rename(index={0: "std"}),
            minimum.to_frame().T.rename(index={0: "min"}),
            # Añadimos directamente el DataFrame de los cuartiles,
            # ya que contiene tres filas correspondientes a 0.25, 0.50 y 0.75.
            cuartiles,
            maximum.to_frame().T.rename(index={0: "max"})
        ],
        # axis=0 indica que los DataFrames se concatenan verticalmente,
        # es decir, uno debajo de otro, manteniendo las asignaturas como columnas.
        axis = 0
    )
    
    # Devolvemos el DataFrame con todas las estadísticas descriptivas.
    return df_resultado


def pandas_dataframe_describe(df: pd.DataFrame) -> pd.DataFrame:
    # Aplicamos describe() para calcular las estadísticas descriptivas del DataFrame
    return df.describe()


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/grades.csv"
    dataframe = read_csv_basic(FILE_PATH)

    print("Custom Describe of the DataFrame:")
    print(custom_dataframe_describe(dataframe), end="\n\n")

    print("Pandas Describe of the DataFrame:")
    print(pandas_dataframe_describe(dataframe))
