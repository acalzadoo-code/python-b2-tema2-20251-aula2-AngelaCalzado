"""
Enunciado:
Desarrolla un conjunto de funciones para leer y procesar datos de archivos JSON utilizando Pandas, abordando distintos
escenarios comunes en el análisis de datos mediante Pandas y la función 'read_json()'. Se proporciona un archivo JSON y
se deberán completar las funciones para leer y formatear los datos.

Las funciones y escenarios a desarrollar son:

    - Leer datos desde un archivo JSON básico: read_json_basic(file_path) que lee un archivo JSON sencillo y devuelve un
     DataFrame de Pandas.
    - Leer JSON con orientación específica: read_json_with_orientation(file_path, orient) que lee un archivo JSON con
    una orientación específica (por ejemplo, 'split', 'records', 'index', 'table').
    - Leer JSON y normalizar datos: read_json_and_normalize(file_path, record_path) que lee un archivo JSON y normaliza
    datos anidados utilizando el parámetro 'record_path'.

Parámetros:
    file_path (str): Ruta del archivo JSON.
    orient (str): Orientación de los datos en el JSON (para read_json_with_orientation).
    record_path (list[str]): Ruta de los registros para normalizar datos (para read_json_and_normalize).

Cada función debe devolver un DataFrame de Pandas, permitiendo a los estudiantes ver el efecto de diferentes modos de
lectura de archivos JSON.

Ejemplo:
    json_basic_path = 'data/ramen-ratings.json'
    json_orient_path = 'data/ramen-ratings-orient.json'
    json_table_oriented_path = 'data/ramen-ratings-table-oriented.json'
    json_normalize_path = 'data/ramen-ratings-nested.json'

    df_basic = read_json_basic(json_basic_path)
    df_orient = read_json_with_orientation(json_orient_path, orient='records')
    df_table_oriented = read_json_with_orientation(json_table_oriented_path, orient='table')
    df_normalized = read_json_and_normalize(json_normalize_path, record_path=['data'])

    # Mostrar los primeros registros de cada DataFrame
    print(df_basic.head(), df_orient.head(), df_table_oriented.head(), df_normalized.head())

Salida esperada:
    Un DataFrame de Pandas para cada función.
"""

import pandas as pd
import typing as t
from pathlib import Path
import json


def read_json_basic(file_path: str) -> pd.DataFrame:
    # Leemos y guardamos el json en una variable
    # El archivo utiliza el formato JSON Lines (JSONL), donde cada línea contiene
    # un objeto JSON independiente. Por eso usamos lines=True, para indicar a Pandas
    # que debe interpretar cada línea como un registro separado.
    df = pd.read_json(file_path, lines=True)
    return df


def read_json_with_orientation(file_path: str, orient: str) -> pd.DataFrame:
    # Con orient indicamos cómo queremos representar los datos
    df = pd.read_json(file_path, orient=orient)
    return df

def read_json_and_normalize(file_path: str, record_path: t.List[str]) -> pd.DataFrame:
    # Abrimos y cargamos el JSON para obtener su estructura original de Python.
    # json_normalize necesita recibir el contenido (diccionarios/listas), no la ruta del archivo
    # ni un DataFrame previamente creado con read_json().
    # Abre el archivo en modo lectura ("r") y con codificación UTF-8.
    with open(file_path, "r", encoding="utf-8") as file:
        # Carga el contenido JSON y lo convierte en estructuras de Python.
        contenido_json = json.load(file)
    # Transforma los registros anidados indicados por record_path en un DataFrame.
    df = pd.json_normalize(contenido_json, record_path=record_path)
    return df

# Para probar el código, descomenta las siguientes líneas
current_dir = Path(__file__).parent
json_basic_path = current_dir / "data/ej2b2/ramen-ratings.json"
json_orient_path = current_dir / "data/ej2b2/ramen-ratings-records.json"
json_table_oriented_path = current_dir / "data/ej2b2/ramen-ratings-table.json"
json_normalize_path = current_dir / "data/ej2b2/ramen-ratings-nested.json"

df_basic = read_json_basic(json_basic_path)
df_orient = read_json_with_orientation(json_orient_path, orient="records")
df_table_oriented = read_json_with_orientation(json_table_oriented_path, orient="table")
df_normalized = read_json_and_normalize(json_normalize_path, record_path=["data"])

# Mostrar los primeros registros de cada DataFrame
print(df_basic.head(), df_orient.head(), df_table_oriented.head(), df_normalized.head())
