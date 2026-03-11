import sqlite3
import pandas as pd
import os

def ejecutar_query_sql(query_sql):
    """
    Ejecutar consultas SQL personalizadas - FUNCIÓN REAL
    Esta función se conecta a la base de datos local SQLite (gluck_data.db)
    ubicada en la raíz del proyecto, ejecuta el query y devuelve los resultados 
    REALES en un DataFrame de Pandas.
    
    Args:
        query_sql (str): Consulta SQL en crudo a ejecutar.
        
    Returns:
        pd.DataFrame: DataFrame con los resultados de la base de datos.
    """
    # Nombre del archivo de la base de datos local
    db_name = "gluck_data.db"
    
    # Validar que el archivo de la base de datos exista
    if not os.path.exists(db_name):
        raise FileNotFoundError(f"No se encontró el archivo de base de datos '{db_name}' en la raíz del proyecto.")
        
    try:
        # 1. Establecer la conexión con el archivo SQLite local
        conn = sqlite3.connect(db_name)
        
        # 2. Usar Pandas para ejecutar el query y cargar los datos directamente
        df_resultado = pd.read_sql_query(query_sql, conn)
        
        # 3. Cerrar la conexión para liberar recursos (buena práctica)
        conn.close()
        
        return df_resultado
        
    except sqlite3.Error as e:
        print(f"Error de SQLite ejecutando query: {e}")
        raise Exception(f"Error en la consulta SQL local: {str(e)}")
    except Exception as e:
        print(f"Error inesperado al procesar datos: {e}")
        raise Exception(f"Ha ocurrido un error al procesar los datos locales: {str(e)}")
