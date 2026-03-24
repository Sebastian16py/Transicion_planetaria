echo "Descargando datos..."
wget "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,pl_bmasse+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+pl_bmasse+IS+NOT+NULL&amp;format=csv" -O datos_crudos.csv

echo "Construyendo base de datos..."
python3 constructor_db.py

echo "Generando gráfica..."
python3 analisis_visual.py

echo "Pipeline completado"
