
from datasets import load_dataset
import pandas as pd


class HFDatasetLoader:
    """Carga un dataset de Hugging Face y lo convierte en un DataFrame."""

    def __init__(self, dataset_id, split="train"):
        self.dataset_id = dataset_id
        self.split = split

    def cargar_datos(self):
        """Carga los datos y devuelve un DataFrame de pandas."""
        dataset = load_dataset( self.dataset_id, split=self.split )

        df = dataset.to_pandas()
        return df
