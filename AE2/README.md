# Actividad 2: Manejo de archivos CSV, JSON y TXT

## Objetivo

Leer, modificar y guardar archivos CSV y JSON mediante clases de Python.
Generar un informe TXT que documente las fuentes de datos, las modificaciones
realizadas y los resultados del procesamiento.

## Fuentes de datos

- CSV: https://huggingface.co/datasets/zhugetd/HeightData
- JSON: https://huggingface.co/datasets/loge2146/evocorps-neutral-personas

## Estructura

- `datos_originales/`: archivos originales.
- `datos_modificados/`: archivos procesados.
- `reportes/`: informe de resultados en TXT.
- `manejador_csv.py`: lectura, modificación y escritura de CSV.
- `manejador_json.py`: lectura, modificación y escritura de JSON.
- `generador_resumen_txt.py`: generación del informe TXT.
- `actividad_unidad_1_ae2.ipynb`: notebook que integra la actividad.

## Requisitos

Python 3 y las bibliotecas estándar `csv`, `json`, `pathlib` y `datetime`.

## Ejecución

1. Abrir `actividad_unidad_1_ae2.ipynb` en Jupyter o GitHub Codespaces.
2. Ejecutar las celdas en orden, desde el principio hasta el final.
3. Verificar que se creen los archivos modificados en `datos_modificados/`.
4. Verificar que se genere el informe en `reportes/resumen.txt`.

## Modificaciones realizadas

- CSV: se agrega la marca `(revisado)` al nombre del primer registro.
- JSON: se agrega el campo `reviewed: true` al primer registro.

Los archivos originales se conservan sin modificaciones.

## Resultado

El notebook permite demostrar la lectura, transformación y escritura de
los datos, y documentar el proceso mediante un informe TXT.
