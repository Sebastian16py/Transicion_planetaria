import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

# Conectar con la base de datos
conn = sqlite3.connect('datos_mision.db')

# columnas a extraer de la tabla limpia
QUERY = 'SELECT pl_rade, pl_bmasse FROM Exoplanetas'
df = pd.read_sql_query(QUERY, conn)

conn.close()

# Calculamos la densidad
df['densidad'] = df['pl_bmasse'] / (4/3 * np.pi * (df['pl_rade']**3))

# Comparacion de densidad relativa
df_rocosos = df[df['densidad']>1]
df_transitorios = df[(df['densidad']>0.5) & (df['densidad']<=1)]
df_gaseosos = df[df['densidad']<=0.5]

# Graficamos
plt.figure(figsize=(8,5))

plt.scatter(df_rocosos['pl_rade'], df_rocosos['pl_bmasse'], label='Rocosos (ρ > 1)', alpha=0.7)
plt.scatter(df_transitorios['pl_rade'], df_transitorios['pl_bmasse'], label ='Transicion (0.5 < ρ ≤ 1)')
<<<<<<< HEAD
plt.scatter(df_gaseosos['pl_rade'], df_gaseosos['pl_bmasse'], label='Gaseosos (ρ ≤0.5)', alpha=0.7)
=======
plt.scatter(df_gaseosos['pl_rade'], df_gaseosos['pl_bmasse'], label='Gaseosos (ρ ≤ 0.5)', alpha=0.7)
>>>>>>> 5f53be4 (correccion)

plt.xlabel('Radio [Radios terrestres]')
plt.ylabel('Masa[Masas terrestres]')

plt.axvline(x=1.6, linestyle='--', label='Transición en radio')
plt.axvspan(1.5,2.0, alpha=0.1)

plt.title('Relacion Masa vs Radio de exoplanetas con densidad ')
plt.legend()
plt.grid()

# Escalas
plt.xscale('log')
plt.yscale('log')

plt.savefig('resultado.png')
print('Grafica generada de manera correcta')
