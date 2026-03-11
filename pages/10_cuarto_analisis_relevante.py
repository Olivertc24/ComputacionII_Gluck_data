import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import ejecutar_query_sql

st.set_page_config(page_title="Rendimiento de Campañas", page_icon="📢", layout="wide")
st.title("📢 Cuarto Análisis: Eficiencia en Marketing")

st.write("Evaluación del gasto publicitario frente a las conversiones reales generadas por cada medio, calculando el Costo Por Conversión (CPA).")

query_marketing = """
    SELECT 
        Medium, 
        SUM(Spend) as Gasto_Total, 
        SUM(Conversions) as Conversiones_Totales,
        SUM(Impressions) as Impresiones_Totales,
        (SUM(Spend) / NULLIF(SUM(Conversions), 0)) as Costo_Por_Conversion
    FROM campaign_data
    GROUP BY Medium
    ORDER BY Costo_Por_Conversion ASC;
"""

with st.expander("Ver código SQL"):
    st.code(query_marketing, language="sql")

try:
    df_marketing = ejecutar_query_sql(query_marketing)
    
    # Rellenar valores nulos (por si hubo división por cero)
    df_marketing['Costo_Por_Conversion'] = df_marketing['Costo_Por_Conversion'].fillna(0)
    
    st.markdown("### Resumen de Inversión y Resultados")
    st.dataframe(df_marketing, use_container_width=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    if not df_marketing.empty:
        with col1:
            # Gráfico de barras: Costo por Conversión por Medio
            # Ordenamos para que el más eficiente (menor costo) esté de primero
            df_marketing_sorted = df_marketing.sort_values('Costo_Por_Conversion')
            fig_cpa = px.bar(
                df_marketing_sorted, 
                x='Medium', 
                y='Costo_Por_Conversion', 
                title='Costo Por Conversión (Eficiencia) por Medio',
                text_auto='.2f',
                labels={'Costo_Por_Conversion': 'Costo por Conversión ($)', 'Medium': 'Medio Publicitario'},
                color='Costo_Por_Conversion',
                color_continuous_scale='RdYlGn_r' # Verde para bajo costo, Rojo para alto
            )
            fig_cpa.update_traces(textposition='outside')
            st.plotly_chart(fig_cpa, use_container_width=True)
            
        with col2:
            # Gráfico de burbujas: Gasto vs Conversiones
            fig_bubble = px.scatter(
                df_marketing, 
                x='Gasto_Total', 
                y='Conversiones_Totales', 
                size='Impresiones_Totales',
                color='Medium',
                title='Inversión vs. Conversiones (Tamaño = Impresiones)',
                labels={
                    'Gasto_Total': 'Gasto Total ($)',
                    'Conversiones_Totales': 'Conversiones Totales'
                },
                size_max=40
            )
            st.plotly_chart(fig_bubble, use_container_width=True)

    st.success("🎯 **Insight esperado:** Los medios ubicados más arriba y a la izquierda en el gráfico de burbujas son los más rentables. Las barras verdes en el gráfico de CPA indican dónde debemos enfocar el presupuesto del próximo trimestre.")

except Exception as e:
    st.error(f"Error al cargar datos: {e}")