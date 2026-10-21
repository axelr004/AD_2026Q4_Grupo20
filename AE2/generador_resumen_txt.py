from pathlib import Path
from datetime import datetime


class GeneradorResumenTXT:
    """Genera un informe del procesamiento de archivos CSV y JSON."""

    def __init__(self, ruta_salida="AE2/reportes/resumen.txt"):
        self.ruta_salida = Path(ruta_salida)

    def generar_resumen(
        self,
        url_csv,
        url_json,
        archivo_csv_original,
        archivo_json_original,
        archivo_csv_modificado,
        archivo_json_modificado,
        cantidad_csv,
        cantidad_json,
        cambio_csv,
        cambio_json
    ):
        """Crea un TXT con las fuentes, modificaciones y resultados."""

        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        contenido = f"""
RESUMEN DEL PROCESAMIENTO DE ARCHIVOS - ACTIVIDAD 2
==================================================

Fecha de generación: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

1. FUENTES DE DATOS
-------------------
Dataset CSV: {url_csv}
Dataset JSON: {url_json}

2. ARCHIVOS ORIGINALES
----------------------
CSV: {archivo_csv_original}
JSON: {archivo_json_original}

3. MODIFICACIONES REALIZADAS
----------------------------
CSV: Se modificó el nombre del primer registro.
Cambio realizado: {cambio_csv[0]} -> {cambio_csv[1]}

JSON: Se agregó el campo 'reviewed' al primer registro.
Cambio realizado: {cambio_json[0]} -> {cambio_json[1]}

4. ARCHIVOS GENERADOS
---------------------
CSV modificado: {archivo_csv_modificado}
JSON modificado: {archivo_json_modificado}

5. CLASES Y MÉTODOS UTILIZADOS
------------------------------
ManejadorCSV:
- cargar_datos()
- modificar_datos()
- guardar_datos()

ManejadorJSON:
- cargar_datos()
- modificar_datos()
- guardar_datos()

GeneradorResumenTXT:
- generar_resumen()

6. REGISTROS PROCESADOS
-----------------------
Registros de datos CSV (sin encabezado): {cantidad_csv}
Registros JSON: {cantidad_json}

7. RESULTADO
------------
Los archivos originales se conservaron.
Las modificaciones se guardaron en archivos separados.
Este informe documenta las fuentes, el procesamiento y los resultados.
"""

        with self.ruta_salida.open("w", encoding="utf-8") as archivo:
            archivo.write(contenido.strip() + "\n")

        return self.ruta_salida
