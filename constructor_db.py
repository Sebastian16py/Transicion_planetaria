import pandas as pd
import sqlite3

# Leer los datos
df = pd.read_csv('datos_crudos.csv')

# Limpiar los datos
df = df.dropna(subset=['pl_rade','pl_bmasse'])

# Conectar con una base de datos local
conn = sqlite3.connect('datos_mision.db')

df.to_sql('Exoplanetas', conn, if_exists='replace', index=False)
conn.close()
print('Exoplanetas filtrados a datos_mision.db exitosamente')
