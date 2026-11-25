"""
Enunciado:
Desarrolla un conjunto de funciones para realizar una clasificación de especies de flores Iris utilizando el algoritmo
Support Vector Machine (SVM) de la biblioteca sklearn. El archivo CSV 'iris_dataset.csv' contiene los datos relevantes
para este análisis, incluyendo características como el largo y ancho del sépalo y pétalo, y la especie de la flor Iris
como objetivo de clasificación.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data(file_path: str)` que lee el archivo CSV, divide los datos en características (X)
y objetivo (y), y realiza un split de entrenamiento y prueba con una proporción de 80/20.
2. Realizar la clasificación con SVM: `perform_svm_classification(X_train, y_train, X_test, y_test)` que entrena un
modelo SVM con los datos de entrenamiento y evalúa su rendimiento con los datos de prueba, devolviendo las métricas
de precisión y un reporte de clasificación.
3. Entrenar el clasificador SVM: train_svm_classifier(X_train, y_train) toma las características y las etiquetas de
entrenamiento como entradas, entrena un clasificador de vectores de soporte (SVM) usando un kernel lineal, y devuelve
el clasificador entrenado.
4. Predecir especies: predict_species(clf, features, feature_names) recibe un clasificador SVM entrenado, un conjunto
de características numéricas y sus nombres correspondientes. Crea un DataFrame con estas características, realiza una
predicción usando el clasificador, y devuelve el nombre de la especie predicha basándose en el índice de la predicción.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset Iris.
    X_train, X_test, y_train, y_test: Datos divididos para entrenamiento y pruebas.

Ejemplo de uso:
    X_train, X_test, y_train, y_test = prepare_data('iris_dataset.csv')
    accuracy, classification_report = perform_svm_classification(X_train, y_train, X_test, y_test)

Salida esperada:
    La precisión del modelo SVM en el conjunto de prueba y un reporte de clasificación que incluye precision, recall
    y f1-score para cada clase.
"""

from pathlib import Path
from typing import List, Tuple, Union
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


def prepare_data(file_path: str) -> Tuple:
    # Leer archivo CSV
    df = pd.read_csv(file_path)
    
    # Separar x e y
    # df.drop(columns = ["nombre_columna"]) sirve para seleccionar 
    # todas las columnas del df menos la que tú indicas
    x_caracteristicas = df.drop(columns=["target"])
    y_objetivo = df["target"]
    
    # Dividir los datos: 80% entrenamiento, prueba 20%
    # train_test_split(X, y, test_size=..., random_state=...)
    return train_test_split(x_caracteristicas, y_objetivo, test_size=0.2, random_state=80)
    

def perform_svm_classification(X_test, y_test, clf) -> Tuple[float, str]:
    # Utilizar clf para predecir las etiquetas de X_test
    y_pred = clf.predict(X_test)
    
    # Utilizar accuracy_score() para calcular qué proporción de predicciones ha sido correcta
    # accuracy_score(etiquetas_reales, etiquetas_predichas)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generamos un reporte con classification_report(etiquetas_reales, etiquetas_predichas) que incluye:
    # Precision: cuántas eran realmente de esa especie
    # Recall: de todas las muestras que eran de una especie, cúantas ha identificado
    # F1-score: combina precision y recall
    # Support: número de muestras reales de cada especie
    report = classification_report(y_test, y_pred)
    
    return accuracy, report
    
    
def train_svm_classifier(X_train, y_train) -> SVC:
    # Crear un clasificador SVM con kernel lineal
    clf = SVC(kernel="linear")
    
    # Entrenar el clasificador con los datos de entrenamiento
    clf.fit(X_train, y_train)
    
    # Devolver el clasificador entrenado
    return clf


def predict_species(clf: SVC, features: List[float], feature_names: List[str]) -> str:
    # Construir un nuevo conjunto de datos: pd.DataFrame(datos, columns=nombres_columnas)
    # Encerrar features entre corchetes para que pandas interprete los cuatro valores
    # como una única fila (una muestra) con cuatro columnas.
    df = pd.DataFrame([features], columns=feature_names)
    
    # Realizar la predicción
    prediction = clf.predict(df)
    
    # Devolver el nombre de la especie, no el índice
    especie = target_names[prediction[0]]
    
    return especie


target_names = {0: "Iris Setosa", 1: "Iris Versicolor", 2: "Iris Virginica"}

# Para probar el código, descomenta este código
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    file_path = current_dir / 'data/iris_dataset.csv'
    X_train, X_test, y_train, y_test = prepare_data(file_path)
    clf = train_svm_classifier(X_train, y_train)

    # Precisión y reporte del modelo
    accuracy, report = perform_svm_classification(X_test, y_test, clf)
    print(f'Precisión del modelo: {accuracy}')
    print('Reporte de clasificación:')
    print(report)

    # Realizar una predicción con un nuevo conjunto de características
    feature_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    features = [5.1, 3.5, 1.4, 0.2]  # Ejemplo de características
    species = predict_species(clf, features, feature_names)
    print(f'La especie predicha es: {species}')
