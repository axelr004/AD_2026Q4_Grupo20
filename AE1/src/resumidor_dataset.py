from pathlib import Path


class DatasetSummarizer:
    """Genera un archivo TXT con el resumen de un DataFrame."""

    def __init__(self, df, output_path="reportes/resumen_dataset.txt"):
        """Inicializa el resumidor con los datos y la ruta del reporte."""
        self.df = df
        self.output_path = Path(output_path)

    def generar_resumen(self):
        """Analiza el DataFrame y guarda el resumen en un archivo TXT."""

        # Crear la carpeta de destino si todavía no existe
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        # Escribir el reporte
        with self.output_path.open("w", encoding="utf-8") as archivo:

            # Información general
            archivo.write("RESUMEN DEL DATASET\n")
            archivo.write("=" * 45 + "\n\n")
            archivo.write(f"Cantidad de filas: {self.df.shape[0]}\n")
            archivo.write(f"Cantidad de columnas: {self.df.shape[1]}\n\n")

            # Nombres de las columnas
            archivo.write("NOMBRES DE LAS COLUMNAS\n")
            archivo.write("-" * 45 + "\n")
            for columna in self.df.columns:
                archivo.write(f"- {columna}\n")

            # Tipos de datos
            archivo.write("\nTIPOS DE DATOS\n")
            archivo.write("-" * 45 + "\n")
            archivo.write(self.df.dtypes.to_string())
            archivo.write("\n\n")

            # Valores faltantes
            archivo.write("VALORES FALTANTES POR COLUMNA\n")
            archivo.write("-" * 45 + "\n")
            archivo.write(self.df.isnull().sum().to_string())
            archivo.write("\n\n")

            # Estadísticas descriptivas
            archivo.write("ESTADISTICAS DESCRIPTIVAS\n")
            archivo.write("-" * 45 + "\n")
            archivo.write(self.df.describe(include="all").to_string())
            archivo.write("\n")

        print(f"Resumen guardado en: {self.output_path}")