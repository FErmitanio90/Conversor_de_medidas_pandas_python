import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.56  


# Leer el archivo Excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna con la conversión de cm a pulgadas

df["Pulgadas"] = df["Centímetros"].apply(cm_a_pulgadas)

# Guardar el nuevo archivo Excel con las conversiones
df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print(
    "Conversión completada y guardada en 'muebles_medidas_convertidas.xlsx'"
    )
