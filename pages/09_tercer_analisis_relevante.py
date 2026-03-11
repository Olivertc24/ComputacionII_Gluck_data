import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import ejecutar_query_sql

st.set_page_config(page_title="Analítica Web", page_icon="🌐", layout="wide")
st.title("🌐 Tercer Análisis: Comportamiento de Tráfico Web")

st.write("Análisis de la calidad del tráfico entrante según la fuente de adquisición y el dispositivo utilizado.")

# Consulta agrupando por dispositivo y fuente de tráfico
query_web = """
    SELECT 
        "Device Type", 
        Source, 
        AVG("Bounce Rate") as Tasa_Rebote_Promedio,
        AVG("Pages per Session") as Paginas_Promedio,
        AVG("Duration (sec)") as Duracion_Promedio
    FROM web_analytics
    GROUP BY "Device Type", Source
    ORDER BY Tasa_Rebote_Promedio ASC;
"""

with st.expander("Ver código SQL"):
    st.code(query_web, language="sql")

try:
    df_web = ejecutar_query_sql(query_web)
    
    st.markdown("### Resumen de Métricas de Navegación")
    st.dataframe(df_web, use_container_width=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    if not df_web.empty:
        with col1:
            # Gráfico de dispersión: Tasa de Rebote vs Páginas por sesión
            fig_scatter = px.scatter(
                df_web, 
                x='Tasa_Rebote_Promedio', 
                y='Paginas_Promedio', 
                color='Source',
                symbol='Device Type',
                size='Duracion_Promedio',
                title='Calidad del Tráfico: Rebote vs Engagement',
                labels={
                    'Tasa_Rebote_Promedio': 'Tasa de Rebote Promedio',
                    'Paginas_Promedio': 'Páginas por Sesión'
                },
                size_max=20
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        with col2:
            # Gráfico de barras: Duración de la sesión por dispositivo
            fig_bar = px.bar(
                df_web, 
                x='Device Type', 
                y='Duracion_Promedio', 
                color='Source',
                barmode='stack',
                title='Duración Promedio de Sesión (segundos) por Dispositivo',
                labels={
                    'Duracion_Promedio': 'Duración Promedio (seg)',
                    'Device Type': 'Tipo de Dispositivo'
                },
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    st.info("💡 **Insight esperado:** Observar si el tráfico 'Organic' o 'Direct' retiene al usuario más tiempo (burbujas más grandes y ubicadas arriba a la izquierda en el gráfico de dispersión). Un **Bounce Rate** alto en dispositivos 'Mobile' podría ser un claro indicador de que nuestra interfaz web necesita optimización.")

except Exception as e:
    st.error(f"Error al cargar datos: {e}")