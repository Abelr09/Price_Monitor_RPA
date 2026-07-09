lista_productos = {productos_finales}
import pandas as pd
from datetime import datetime
import os

# Crear DataFrame
df = pd.DataFrame(lista_productos)
df.columns = ['Nombre del Producto', 'Precio (Gs.)', 'URL']

# Crear carpeta si no existe
os.makedirs("C:/rocketbot_exports", exist_ok=True)

# Nombre del archivo con fecha
nombre_archivo = f"productos_nissei_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
ruta_completa = f"C:/rocketbot_exports/{nombre_archivo}"

# Guardar Excel
df.to_excel(ruta_completa, index=False, sheet_name='Productos')

# Guardar variables para usar después
SetVar("ruta_excel", ruta_completa)
SetVar("nombre_archivo_excel", nombre_archivo)

print(f"Excel creado: {nombre_archivo}")
print(f"Total productos: {len(lista_productos)}")