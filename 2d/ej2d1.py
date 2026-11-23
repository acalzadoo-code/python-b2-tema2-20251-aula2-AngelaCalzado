"""
Enunciado:
Desarrolla un conjunto de funciones para analizar datos estadísticos de un conjunto de calificaciones utilizando
`scipy.stats`. Se proporciona un archivo CSV con calificaciones de estudiantes y se deberán completar las funciones
para calcular diferentes momentos estadísticos de las calificaciones.

Las funciones y estadísticas a desarrollar son:
    - Calcular el primer momento (media): calculate_mean(file_path) que lee un archivo CSV y calcula la media de las
    calificaciones.
    - Calcular el segundo momento (varianza): calculate_variance(file_path) que calcula la varianza de las
    calificaciones para entender su dispersión.
    - Calcular el tercer momento (asimetría): calculate_skewness(file_path) para evaluar la asimetría de la
    distribución de las calificaciones.
    - Calcular el cuarto momento (curtosis): calculate_kurtosis(file_path) para medir la forma de la distribución de
    las calificaciones, en particular su picudez.

Parámetros:
    file_path (str): Ruta del archivo CSV que contiene las calificaciones.

Cada función debe devolver el valor del momento estadístico calculado, permitiendo a los estudiantes comprender la
distribución de las calificaciones.

Ejemplo:
    mean = calculate_mean(calificaciones_csv_path)
    variance = calculate_variance(calificaciones_csv_path)
    skewness = calculate_skewness(calificaciones_csv_path)
    kurtosis = calculate_kurtosis(calificaciones_csv_path)

Salida esperada:
    Los valores de la media, varianza, asimetría y curtosis de las calificaciones.
"""

from pathlib import Path
import pandas as pd
from scipy import stats


def calculate_mean(file_path: str) -> float:
    # Leemos la base de datos y la guardamos en una variable
    df = pd.read_csv(file_path)
    # Accedemos a la columna calificaciones del df (en este caso la única que hay)
    calificaciones = df["Calificaciones"]
    # Calculamos la media utilizando stats.tmean(columna_df)
    media = stats.tmean(calificaciones)
    return media


def calculate_variance(file_path: str) -> float:
    # Leemos la base de datos y la guardamos en una variable
    df = pd.read_csv(file_path)
    # Accedemos a la columna calificaciones del df (en este caso la única que hay)
    calificaciones = df["Calificaciones"]
    # Calculamos la varianza utilizando stats.tvar(columna_df)
    # stats.tvar() calcula la varianza muestral por defecto (ddof=1)
    # Para calcular la varianza poblacional habría que poner ddof=0.
    varianza = stats.tvar(calificaciones)
    return varianza


def calculate_skewness(file_path: str) -> float:
    # La asimetría nos indica si una distribución está equilibrada 
    # o si presenta una cola más larga hacia alguno de sus extremos.
    # Leemos la base de datos y la guardamos en una variable
    df = pd.read_csv(file_path)
    # Accedemos a la columna calificaciones del df (en este caso la única que hay)
    calificaciones = df["Calificaciones"]
    # Calculamos la asimetría utilizando stats.skew(columna_df)
    # Por defecto bias = True, que calcula la asimetría sin corregir el sesgo estadístico.
    # Si pusiéramos false aplica una corrección para obtener una estimación insesgada de la asimetría poblacional
    asimetria = stats.skew(calificaciones)
    return asimetria


def calculate_kurtosis(file_path: str) -> float:
    # La curtosis es una medida relacionada con la forma de la distribución y, 
    # tradicionalmente, se explica en términos de su apuntamiento.
    # Leptocúrtica: curtosis positiva (exceso de curtosis).
    # Mesocúrtica: curtosis igual a cero (distribución normal de referencia).
    # Platicúrtica: curtosis negativa (exceso de curtosis).
    
    # Leemos la base de datos y la guardamos en una variable
    df = pd.read_csv(file_path)
    # Accedemos a la columna calificaciones del df (en este caso la única que hay)
    calificaciones = df["Calificaciones"]
    # Calculamos la curtosis utilizando stats.kurtosis(columna_df)
    # Por defecto fisher = True, devuelve el exceso de curtosis
    # Si pusiéramos False devuelve la curtosis de Pearson
    curtosis = stats.kurtosis(calificaciones)
    return curtosis

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / 'data/calificaciones.csv'
    mean = calculate_mean(FILE_PATH)
    variance = calculate_variance(FILE_PATH)
    skewness = calculate_skewness(FILE_PATH)
    kurtosis = calculate_kurtosis(FILE_PATH)

    # Mostrar los resultados calculados
    print(f'Media: {mean}, Varianza: {variance}, Asimetría: {skewness}, Curtosis: {kurtosis}')
