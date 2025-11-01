''' docker run -d \
  --name postgres-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=miclave \
  -e POSTGRES_DB=mibase \
  -p 5432:5432 \
  postgres:latest
'''
#pip install psycopg2-binary
import psycopg2

# Parámetros de conexión
host = "localhost"        # o la IP del servidor
port = "5432"             # puerto por defecto
database = "jaguarete"
user = "postgres"
password = "unida123"

try:
    # Crear la conexión
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    )

    # Crear cursor para ejecutar consultas
    cursor = conn.cursor()
    print("✅ Conexión exitosa a PostgreSQL")

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM cliente LIMIT 5;")

    # Mostrar resultados
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("❌ Error al conectar:", e)

finally:
    if 'conn' in locals():
        conn.close()