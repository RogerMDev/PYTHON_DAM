import pandas as pd
import mysql.connector  # Para MySQL (opcional)

def csv_to_sql(csv_file, db_type="sqlite", table_name="datos", db_name="database.db"):
    # Leer el CSV con Pandas
    df = pd.read_csv(csv_file)

    if db_type == "sqlite":
        # Conectar con SQLite
        conn = sqlite3.connect(db_name)
    elif db_type == "mysql":
        # Conectar con MySQL (ajusta los datos de conexión)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mi_base_de_datos"
        )
    else:
        raise ValueError("Base de datos no soportada. Usa 'sqlite' o 'mysql'.")

    # Insertar los datos en la tabla (crea la tabla si no existe)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"✅ Datos insertados en la tabla '{table_name}' en {db_type.upper()}")

    # Cerrar conexión
    conn.close()

# ⚡️ USO: Convertir un archivo CSV en SQL
csv_to_sql("estudiantes.csv", db_type="sqlite", table_name="usuarios", db_name="mi_base.db")  # Para SQLite
# csv_to_sql("datos.csv", db_type="mysql", table_name="usuarios")  # Para MySQL
