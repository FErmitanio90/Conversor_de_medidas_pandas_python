import pandas as pd

# Crear el DataFrame con los nombres de las piezas y sus medidas en cm
data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral"],
    "Centímetros": [40, 120, 60, 30, 180] 
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel("muebles_medidas.xlsx", index=False, engine="openpyxl")

print("Archivo 'muebles_medidas.xlsx' creado exitosamente.")
