import streamlit as st
import pandas as pd
from utils.database import ejecutar_query_sql

st.set_page_config(page_title="Ejecución de Consultas", page_icon="💻")
st.title("💻 Consultas SQL Interactivas")

st.write("Ingresa tu código SQL para consultar la base de datos de manera interactiva.")

query = st.text_area("Escribe tu consulta SQL aquí:", "SELECT * FROM customer_data LIMIT 5;")

if st.button("Ejecutar Query"):
    with st.spinner("Ejecutando consulta..."):
        try:
            # Aquí se invoca tu función modular
            df_resultado = ejecutar_query_sql(query)
            st.success("Consulta ejecutada con éxito.")
            st.dataframe(df_resultado)
        except Exception as e:
            st.error(f"Error: {e}")