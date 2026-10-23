from src.cargador_dataset import HFDatasetLoader

# Identificador del dataset de Hugging Face
dataset_id = "SIH/palmer-penguins"

# Crear el cargador y cargar los datos
cargador = HFDatasetLoader(dataset_id, split="train")
df = cargador.cargar_datos()

# Mostrar los resultados
print("Dataset cargado correctamente.")
print("Dimensiones:", df.shape)
print("\nColumnas:")
print(df.columns.tolist())
print("\nPrimeras cinco filas:")
print(df.head())