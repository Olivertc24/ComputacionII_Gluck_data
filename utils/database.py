import sqlite3
import pandas as pd
import os

def ejecutar_query_sql(query_sql):
    """
    Ejecutar consultas SQL personalizadas - FUNCIÓN REAL
    Esta función se conecta a la base de datos local SQLite (gluck_data.db),
    ejecuta el query y devuelve los resultados REALES en un DataFrame.
    
    Args:
        query_sql (str): Consulta SQL a ejecutar.
        
    Returns:
        pd.DataFrame: DataFrame con los resultados de la base de datos.
    """
    # Nombre del archivo de la base de datos
    db_name = "gluck_data.db"
    
    # Validar que el archivo exista en el directorio raíz
    if not os.path.exists(db_name):
        raise FileNotFoundError(f"No se encontró la base de datos '{db_name}'. Asegúrate de que esté en la raíz del proyecto.")
        
    try:
        # 1. Establecer la conexión con SQLite
        conn = sqlite3.connect(db_name)
        
        # 2. Ejecutar el query y cargar los resultados directamente en Pandas
        df_resultado = pd.read_sql_query(query_sql, conn)
        
        # 3. Cerrar la conexión
        conn.close()
        
        return df_resultado
        
    except sqlite3.Error as e:
        print(f"Error de base de datos ejecutando query: {e}")
        raise Exception(f"Error en la consulta SQL: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise Exception(f"Ha ocurrido un error al procesar los datos: {str(e)}")