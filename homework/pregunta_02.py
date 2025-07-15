"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """

    # Leer el archivo TSV (separado por tabulaciones)
    df = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Obtener el número de columnas
    num_columnas = df.shape[1]

    return num_columnas