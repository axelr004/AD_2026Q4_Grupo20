from datasets import load_dataset
from src.resumidor_dataset import DatasetSummarizer

# Cargar el dataset de Hugging Face
dataset = load_dataset("SIH/palmer-penguins", split="train")
df = dataset.to_pandas()

# Generar el reporte
resumidor = DatasetSummarizer(
    df,
    output_path="reportes/resumen_dataset.txt"
)

resumidor.generar_resumen()

# Mostrar el reporte en la terminal
with open("reportes/resumen_dataset.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())
