import json
from pathlib import Path


class ManejadorJSON:

    def __init__(self, ruta_entrada):
        self.ruta_entrada = Path(ruta_entrada)
        self.datos = None

    def cargar_datos(self):
        with self.ruta_entrada.open("r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)

        return self.datos

    def modificar_datos(self):
        if not isinstance(self.datos, list) or not self.datos:
            raise ValueError(
                "Se necesita una lista JSON con al menos un registro."
            )

        valor_anterior = self.datos[0].get("reviewed", False)
        self.datos[0]["reviewed"] = True

        return valor_anterior, self.datos[0]["reviewed"]

    def guardar_datos(self, ruta_salida):
        if self.datos is None:
            raise ValueError("Primero debes cargar los datos.")

        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        with ruta_salida.open("w", encoding="utf-8") as archivo:
            json.dump(
                self.datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        return ruta_salida
