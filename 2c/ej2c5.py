"""
Enunciado:
Desarrolla un conjunto de funciones en Python para manejar y procesar un conjunto de datos de calificaciones que 
potencialmente contiene valores faltantes o no válidos. El conjunto de datos está almacenado en un archivo CSV y
contiene calificaciones en diversas materias para un grupo de estudiantes. El objetivo es limpiar los datos, eliminar
filas con datos faltantes en columnas clave, y aplicar técnicas de imputación para tratar los valores faltantes en
ciertas columnas.

Las funciones a desarrollar son:
1. Leer el archivo CSV: `read_csv(filepath: str)` que lee el archivo CSV desde la ruta especificada y devuelve un 
DataFrame de pandas.
2. Limpiar el DataFrame: `clean_dataframe(df)` que limpia el DataFrame reemplazando valores no válidos ('Null', '-',
'NA', 'na', y espacios en blanco) por `NaN`, y convierte las columnas numéricas a su tipo correspondiente, excepto la
primera columna.
3. Eliminar filas con `NaN` en una columna específica: `dropna_specific_row_in_column(df, column_name: str)` que
elimina las filas que contienen un valor `NaN` en la columna especificada por `column_name`.
4. Rellenar valores faltantes en una columna específica: `fillna_method(df, column_name: str, fill_method='ffill',
fill_value=None, limit=1)` que rellena los valores faltantes en la columna especificada utilizando un método de 
relleno especificado (`ffill` para relleno hacia adelante con un límite de 1, o `mean` para rellenar con el promedio
de la columna).

Parámetros:
- filepath (str): Ruta al archivo CSV que contiene los datos de calificaciones.
- column_name (str): Nombre de la columna en la cual aplicar la eliminación de filas o el relleno de valores 
faltantes.
- fill_method (str): Método de relleno para tratar valores faltantes (`ffill` para relleno hacia adelante, `mean` 
para el promedio).
- fill_value (Optional[float]): Valor específico de relleno a usar si se especifica. Útil solo cuando 
`fill_method` es `mean`.
- limit (int)`: Número máximo de rellenos consecutivos a aplicar cuando se utiliza `ffill`.

Ejemplo de uso:
    df_cleaned = clean_dataframe(df_v2)
    df_drop_na_rows = dropna_specific_row_in_column(df_cleaned, 'Name')
    df_filled_column_ffill = fillna_method(df_drop_na_rows, 'Hindi', fill_method='ffill', limit=1)
    df_filled_column_mean = fillna_method(df_filled_column_ffill, 'Maths', fill_method='mean')


Salida esperada:
- Un DataFrame limpio y procesado donde las filas con valores faltantes en columnas clave han sido eliminadas, y los
valores faltantes en ciertas columnas han sido tratados mediante técnicas de imputación específicas.
"""

from pathlib import Path
import pandas as pd
import numpy as np


def read_csv(filepath):
    return pd.read_csv(filepath)


def clean_dataframe(df):
    # .replace busca los valores indicados (Null, -, NA, na) en el DataFrame
    # y los sustituye por NaN (np.nan)
    df_replace = df.replace(['Null', '-', 'NA', 'na', '   '], np.nan)
    
    # Convertimos todas las columnas excepto la primera a numéricas
    for columna in df_replace.columns[1:]:
        # df_replace[columna] seleccionamos dónde queremos guardar el resultado
        # pd.to_numeric(df_replace[columna]) convierte los valores de esa columna
        df_replace[columna] = pd.to_numeric(df_replace[columna])
        
    return df_replace


def dropna_specific_row_in_column(df, column_name):
    # df.dropna() elimina las filas que contienen valores ausentes (NaN).
    # El parámetro subset permite especificar en qué columna o columnas
    # queremos comprobar si existen valores ausentes.
    # [column_name] convierte el nombre de la columna en una lista,
    # que es el formato que espera el parámetro subset.
    # De esta manera, solo se eliminan las filas que tienen NaN
    # en la columna indicada, aunque existan NaN en otras columnas.
    df_dropna = df.dropna(subset=[column_name])
    return df_dropna


def fillna_method(df, column_name, fill_method="ffill", fill_value=None, limit=1):
    # Write here your code
    if fill_method == "ffill":
        # ffill() rellena los valores NaN utilizando el último valor válido
        # encontrado anteriormente en la columna.
        # limit establece el número máximo de valores NaN consecutivos
        # que se pueden rellena
        df[column_name] = df[column_name].ffill(limit=limit)
        
    elif fill_method == "mean":
        # Comprobamos si el usuario ha proporcionado un valor de relleno.
        if fill_value is not None:
            # Si existe un valor manual, lo utilizamos para sustituir
            # todos los valores NaN de la columna.
            df[column_name] = df[column_name].fillna(value=fill_value)
        else:
            # Si no se proporciona un valor manual, calculamos la media
            # de la columna y la utilizamos para sustituir los valores NaN.
            df[column_name] = df[column_name].fillna(value=df[column_name].mean())
    
    return df

# Para probar el código, descomenta las siguientes líneas y asegúrate de que el path al archivo sea correcto
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/grades_na.csv"
    dataframe = read_csv(FILE_PATH)
    df_cleaned = clean_dataframe(dataframe)
    df_drop_na_rows = dropna_specific_row_in_column(df_cleaned, "Name")
    df_filled_column_ffill = fillna_method(
        df_drop_na_rows, "Hindi", fill_method="ffill", limit=1
    )
    df_filled_column_mean = fillna_method(
        df_filled_column_ffill, "Maths", fill_method="mean"
    )

    print(dataframe.head())
    print(df_filled_column_mean.head())
