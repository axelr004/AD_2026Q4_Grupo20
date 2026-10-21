import csv
from pathlib import Path


class ManejadorCSV:
    """Lee, modifica y guarda archivos CSV."""

    def __init__(self, ruta_entrada):
        self.ruta_entrada = Path(ruta_entrada)
        self.datos = []

    def cargar_datos(self):
        """Lee el CSV y conserva su encabezado."""
        with self.ruta_entrada.open(
            "r", encoding="utf-8-sig", newline=""
        ) as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)

        if not filas:
            raise ValueError("El archivo CSV está vacío.")

        self.encabezados = filas[0]
        self.datos = filas[1:]
        return self.encabezados, self.datos

    def modificar_datos(self):
        """Actualiza el nombre del primer registro."""
        if not self.datos:
            raise ValueError("Primero debes cargar los datos.")

        indice_nombre = self.encabezados.index("name")
        nombre_anterior = self.datos[0][indice_nombre]
        self.datos[0][indice_nombre] = nombre_anterior + " (revisado)"

        return nombre_anterior, self.datos[0][indice_nombre]

    def guardar_datos(self, ruta_salida):
        """Guarda los datos modificados en un nuevo CSV."""
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        with ruta_salida.open(
            "w", encoding="utf-8", newline=""
        ) as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)

        return ruta_salida
