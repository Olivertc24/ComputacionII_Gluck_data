import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import ejecutar_query_sql

st.set_page_config(page_title="Análisis de Ventas", page_icon="🛍️", layout="wide")
st.title("🛍️ Primer Análisis: Rendimiento de Ventas")

st.write("Evaluación del volumen de ventas y los ingresos generados por cada categoría de producto y canal de distribución.")

query_ventas = """
    SELECT 
        Category, 
        Channel, 
        SUM("Units Sold") as Total_Unidades,
        SUM("Unit Revenue" * "Units Sold") as Ingreso_Total
    FROM sales_data
    GROUP BY Category, Channel
    ORDER BY Ingreso_Total DESC;
"""

with st.expander("Ver código SQL"):
    st.code(query_ventas, language="sql")

try:
    df_ventas = ejecutar_query_sql(query_ventas)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Datos Crudos")
        st.dataframe(df_ventas, use_container_width=True)
        
    with col2:
        st.subheader("Ingresos por Categoría y Canal")
        if not df_ventas.empty:
            # Gráfico interactivo con Plotly
            fig = px.bar(
                df_ventas, 
                x='Category', 
                y='Ingreso_Total', 
                color='Channel',
                barmode='group',
                title="Distribución de Ingresos",
                labels={'Ingreso_Total': 'Ingreso Total ($)', 'Category': 'Categoría'},
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
            
except Exception as e:
    st.warning("Asegúrate de conectar la base de datos para ver los resultados reales.")