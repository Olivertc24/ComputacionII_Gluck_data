import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import ejecutar_query_sql

st.set_page_config(page_title="Segmentación de Clientes", page_icon="👥", layout="wide")
st.title("👥 Segundo Análisis: Segmentación Demográfica")

st.write("Comprender cómo se distribuye nuestra cartera de clientes actuales es vital para las estrategias de retención.")

query_clientes = """
    SELECT 
        Segment, 
        COUNT(ID) as Total_Clientes,
        AVG(Age) as Edad_Promedio
    FROM customer_data
    GROUP BY Segment
    ORDER BY Total_Clientes DESC;
"""

with st.expander("Ver código SQL"):
    st.code(query_clientes, language="sql")

try:
    df_clientes = ejecutar_query_sql(query_clientes)
    st.dataframe(df_clientes, use_container_width=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    if not df_clientes.empty:
        with col1:
            # Gráfico de proporción de clientes
            fig_pie = px.pie(
                df_clientes, 
                values='Total_Clientes', 
                names='Segment', 
                title='Distribución de Clientes por Segmento',
                hole=0.4, # Lo convierte en un gráfico de anillo (donut chart)
                color_discrete_sequence=px.colors.sequential.Teal
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with col2:
            # Gráfico de edad promedio
            fig_bar = px.bar(
                df_clientes, 
                x='Segment', 
                y='Edad_Promedio', 
                title='Edad Promedio por Segmento',
                text_auto='.1f',
                color='Segment'
            )
            fig_bar.update_traces(textposition='outside')
            st.plotly_chart(fig_bar, use_container_width=True)

    st.info("💡 **Insight esperado:** Identificar visualmente si el segmento 'Churned' (abandonos) tiene una concentración inusual en algún rango de edad específico en comparación con los clientes 'Loyal'.")

except Exception as e:
    st.error(f"Error al cargar datos: {e}")