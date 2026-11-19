"""
Enunciado:
Desarrolla un conjunto de funciones para leer y procesar datos de archivos Excel utilizando Pandas, abordando
distintos escenarios comunes en el análisis de datos. Se proporciona un archivo Excel y se deberán completar las
funciones para leer y formatear los datos.

Las funciones y escenarios a desarrollar son:
    - Leer datos desde una hoja específica: read_excel_sheet(file_path) que lee todos los registros de la hoja Sheet1
    en el archivo Excel y devuelve un DataFrame de Pandas.
    - Leer y limpiar datos de la hoja Sheet2 con encabezados desplazados, filas y columnas adicionales:
    read_excel_custom_sheet(file_path) que lee la hoja, ajusta los encabezados de las columnas y omite las
    filas y columnas sin valor, adicional, evitar las filas al final de la hoja.

Parámetros:
    - file_path (str): Ruta al archivo Excel.

Cada función debe devolver un DataFrame de Pandas, permitiendo a los estudiantes ver el efecto de diferentes modos de
lectura de datos desde un archivo Excel.

Ejemplo:
    df_from_sheet1 = read_excel_sheet(excel_file_path)
    df_from_sheet2 = read_excel_custom_sheet(excel_file_path)

Salida esperada:
    Un DataFrame de Pandas para cada función.
"""

import pandas as pd
from pathlib import Path
import openpyxl


def read_excel_sheet(file_path: str) -> pd.DataFrame:
    # Para leer la hoja Sheet1 la buscamos entre comillas
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    return df



def read_excel_custom_sheet(file_path: str) -> pd.DataFrame:
    # Leemos la hoja Sheet2 del archivo Excel.
    # header=3 indica que la cuarta fila (índice 3) contiene los encabezados.
    # skipfooter=4 omite las cuatro últimas filas del archivo.
    df = pd.read_excel(file_path, sheet_name="Sheet2", header=3, skipfooter=4)
    
    # Definimos una función auxiliar para comprobar si una columna contiene datos
    def is_not_empty_column(col):
        # notna() devuelve True para las celdas que no contienen NaN.
        # any() devuelve True si al menos una celda de la columna contiene datos.
        not_empty_column = col.notna().any()
        # Devuelve True si la columna tiene al menos un valor no vacío.
        return not_empty_column
    
    # Aplicamos la función auxiliar a cada columna del DataFrame (axis=0).
    # El resultado es una Serie de booleanos que indica qué columnas tienen datos.
    columnas_validas = df.apply(is_not_empty_column, axis=0)
    
    # Filtramos el DataFrame utilizando la Serie de booleanos.
    # Solo conservamos las columnas cuyo resultado es True.
    # Utilizamos .loc para seleccionar todas las filas (:) y únicamente las columnas
    # que contienen datos, según los valores booleanos de columnas_validas.
    df = df.loc[:, columnas_validas]
    
    # Devolvemos el DataFrame limpio.
    return df
    
file_path = "data/ej2b4/ramen-ratings.xlsx"
current_dir = Path(__file__).parent
excel_file_path = current_dir / file_path

df_from_sheet1 = read_excel_sheet(excel_file_path)
df_from_sheet2 = read_excel_custom_sheet(excel_file_path)

# Mostrar la cantidad de registros y los nombres de las columnas
print(f"Registros en la hoja 1: {len(df_from_sheet1)}")
print(f"Nombres de columnas en la hoja 1: {df_from_sheet1.columns.tolist()}")
print(f"Registros en la hoja 2: {len(df_from_sheet2)}")
print(f"Nombres de columnas en la hoja 2: {df_from_sheet2.columns.tolist()}")
