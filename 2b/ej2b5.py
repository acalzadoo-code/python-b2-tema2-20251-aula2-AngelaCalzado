"""
Enunciado:

Desarrolla un conjunto de funciones para extraer y analizar datos de población de países desde una tabla HTML en
Wikipedia. Estas funciones deben ser capaces de leer tablas HTML con atributos específicos en la página y filtrar para
encontrar datos en una tabla específica basada en un texto de coincidencia.

Implementa las siguientes funciones:
    - read_population_data(url, match_text=None): Función para leer todas las tablas HTML de una página web con
    atributos específicos y, opcionalmente, que contengan un texto de coincidencia, devolviendo una lista de DataFrames.
    - get_table_by_string_match(tables, match_text): Función para extraer una tabla específica de la lista de DataFrames
    que contenga el parámetro match_text.
    - count_tables(tables): Función para contar el número de tablas HTML en la página web.

Parámetros:
    - url (str): URL de la página de Wikipedia con la tabla de población de países para read_population_data.
    - match_text (str, opcional): Texto para identificar la tabla específica que se quiere extraer en
    read_population_data y get_table_by_string_match.
    - tables (List[pd.DataFrame]): Lista de DataFrames que representan las tablas HTML leídas de la página web en
    count_tables.

Funcionamiento y Atributos:
    - La función read_population_data utiliza el parámetro attrs para especificar los atributos HTML que deben tener las
    tablas a leer. En este caso, estamos buscando tablas con la clase wikitable, que es común para las tablas
    estandarizadas en Wikipedia.
    - El parámetro na_values se utiliza para identificar qué cadenas de texto deben ser interpretadas como valores
    NA/NaN (Not Available/Not a Number). Por ejemplo, los guiones o la palabra 'None' se consideran indicadores de datos
    no disponibles.
    - Si se proporciona el parámetro match_text a read_population_data, solo se leerán las tablas que contengan ese
    texto específico, haciendo uso del parámetro match de la función pd.read_html.

Ejemplo:
    tables = read_population_data(url)
    selected_table = get_table_by_string_match(tables, "Spain")
    if selected_table is not None:
        print(selected_table)
    else:
        print("No se encontró la tabla con el texto proporcionado.")

Salida esperada:
    - El número de tablas HTML encontradas en la página con los atributos especificados.
    - Un DataFrame de Pandas con los datos de la tabla que coincide con el texto proporcionado, si existe.
"""

import pandas as pd
import typing as t
import requests
from io import StringIO


def read_population_data(url: str, match_text: str = None) -> t.List[pd.DataFrame]:
    # Definimos una cabecera User-Agent para identificarnos como un navegador web
    # y evitar que Wikipedia bloquee la petición HTTP realizada desde Python.
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Descargamos el contenido HTML de la página mediante requests.
    # Utilizamos requests en lugar de pasar directamente la URL a pd.read_html()
    # porque Wikipedia puede bloquear las peticiones directas de Pandas con un error 403.
    response = requests.get(url, headers=headers)
    
    # StringIO convierte el contenido HTML descargado en un objeto similar a un archivo,
    # que puede ser interpretado por pd.read_html().
    # Usamos response.text en lugar de url porque ya hemos descargado el HTML
    # y queremos analizar ese contenido, no realizar una nueva petición a la página.
    if match_text is None:
        # Si no se proporciona un texto de búsqueda, leemos todas las tablas
        # que tengan la clase HTML "wikitable".
        tables = pd.read_html(StringIO(response.text), attrs={"class": "wikitable"}, na_values=["-", "None"])
    else:
        # Si se proporciona match_text, filtramos las tablas para obtener
        # únicamente aquellas que contienen el texto indicado.
        tables = pd.read_html(StringIO(response.text), attrs={"class": "wikitable"}, match=match_text, na_values=["-", "None"])
    
    # Devuelve la lista de dataframes
    return tables


def get_table_by_string_match(
    tables: t.List[pd.DataFrame], match_text: str
) -> t.Union[pd.DataFrame, None]:
    # Recorre uno a uno los df de la lista
    for table in tables:
        # Convierte el contenido del df en una cadena de texto
        table_string= table.to_string()
        # Comprueba si el texto buscado aparece dentro de esa cadena
        if match_text in table_string:
            # Devuelve el primer df que contiene el texto y termina la función
            return table
    # Si no hay coincidencias devuelve none
    return None


def count_tables(tables: t.List[pd.DataFrame]) -> int:
    # Contamos el número de df que hay en la lista
    count = len(tables)
    return count


# Para probar el código, descomenta las siguientes líneas
# url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
# tables = read_population_)data(url)
# print(f"Número de tablas en la página: {count_tables(tables)}")
# selected_table = get_table_by_string_match(tables, "Spain")

# if selected_table is not None:
#     print(f"Registros en la tabla: {len(selected_table)}")
#     print(f"Nombres de columnas: {selected_table.columns.tolist()}")
#     print(selected_table)
# else:
#     print("No se encontró la tabla con el texto proporcionado.")
