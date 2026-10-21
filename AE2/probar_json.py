from pathlib import Path
import sys
import json

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from AE2.manejador_json import ManejadorJSON

original = RAIZ / "AE2" / "datos_originales" / "neutral_personas_database.json"
salida = RAIZ / "AE2" / "datos_modificados" / "neutral_personas_database_modificado.json"

if not original.exists():
    raise FileNotFoundError(f"No se encuentra el archivo original: {original}")

manejador = ManejadorJSON(original)
datos = manejador.cargar_datos()

print("Cantidad de registros:", len(datos))
print("\nPrimer registro antes del cambio:")
print(datos[0])

cambio = manejador.modificar_datos()
manejador.guardar_datos(salida)

with salida.open("r", encoding="utf-8") as archivo:
    datos_guardados = json.load(archivo)

with original.open("r", encoding="utf-8") as archivo:
    datos_originales = json.load(archivo)

print("\nCambio realizado:", cambio)
print("Archivo generado:", salida)
print("¿Existe el archivo?", salida.exists())
print("¿El campo reviewed es True?", datos_guardados[0].get("reviewed") is True)
print("¿El original permanece sin el campo reviewed?", "reviewed" not in datos_originales[0])
