"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """


    # Leer el archivo TSV
    df = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Calcular la suma de 'c2' por cada letra en 'c1'
    suma_por_letra = df.groupby('c1')['c2'].sum().sort_index()

    return suma_por_letra