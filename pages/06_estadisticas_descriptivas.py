import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import ejecutar_query_sql

st.set_page_config(page_title="Estadísticas Descriptivas", page_icon="📈", layout="wide")
st.title("📈 Estadísticas Descriptivas")

st.write("""
Antes de profundizar en análisis cruzados, es fundamental entender la naturaleza de nuestros datos. 
Aquí presentamos las medidas de tendencia central, dispersión y forma de las distribuciones para nuestras tablas principales.
""")

# Intentamos cargar los datos de las 4 tablas principales
try:
    df_sales = ejecutar_query_sql("SELECT * FROM sales_data")
    df_customers = ejecutar_query_sql("SELECT * FROM customer_data")
    df_web = ejecutar_query_sql("SELECT * FROM web_analytics")
    df_campaigns = ejecutar_query_sql("SELECT * FROM campaign_data")
    
    # Creamos pestañas para organizar la información visualmente
    tab1, tab2, tab3, tab4 = st.tabs(["🛍️ Ventas", "👥 Clientes", "🌐 Web Analytics", "📢 Campañas"])
    
    # --- PESTAÑA 1: VENTAS ---
    with tab1:
        st.markdown("### Resumen Estadístico de Ventas")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write("**Métricas Numéricas**")
            # Seleccionamos solo las columnas numéricas relevantes para describe()
            st.dataframe(df_sales[['Unit Revenue', 'Units Sold']].describe().T, use_container_width=True)
            
        with col2:
            st.write("**Distribución del Ingreso Unitario (Unit Revenue)**")
            fig_sales = px.box(
                df_sales, 
                x="Category", 
                y="Unit Revenue", 
                color="Category",
                title="Dispersión de Precios por Categoría",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig_sales, use_container_width=True)

    # --- PESTAÑA 2: CLIENTES ---
    with tab2:
        st.markdown("### Resumen Estadístico de Clientes")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write("**Métricas Numéricas**")
            st.dataframe(df_customers[['Age']].describe().T, use_container_width=True)
            
        with col2:
            st.write("**Distribución de Edades**")
            fig_age = px.histogram(
                df_customers, 
                x="Age", 
                nbins=20, 
                title="Frecuencia de Edades de los Clientes",
                marginal="box", # Agrega un boxplot en la parte superior
                color_discrete_sequence=["#F6D55C"] # Usamos el amarillo de Van Gogh
            )
            st.plotly_chart(fig_age, use_container_width=True)

    # --- PESTAÑA 3: WEB ANALYTICS ---
    with tab3:
        st.markdown("### Resumen Estadístico de Tráfico Web")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write("**Métricas Numéricas**")
            st.dataframe(df_web[['Duration (sec)', 'Bounce Rate', 'Pages per Session']].describe().T, use_container_width=True)
            
        with col2:
            st.write("**Distribución de Tasa de Rebote**")
            fig_bounce = px.histogram(
                df_web, 
                x="Bounce Rate", 
                color="Device Type",
                barmode="overlay",
                title="Tasa de Rebote según Dispositivo",
                opacity=0.7
            )
            st.plotly_chart(fig_bounce, use_container_width=True)

    # --- PESTAÑA 4: CAMPAÑAS ---
    with tab4:
        st.markdown("### Resumen Estadístico de Marketing")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.write("**Métricas Numéricas**")
            st.dataframe(df_campaigns[['CTR', 'CPM', 'Spend', 'Conversions', 'Impressions']].describe().T, use_container_width=True)
            
        with col2:
            st.write("**Dispersión de Inversión (Spend)**")
            fig_spend = px.box(
                df_campaigns, 
                x="Medium", 
                y="Spend", 
                color="Medium",
                title="Rango de Inversión por Medio Publicitario"
            )
            st.plotly_chart(fig_spend, use_container_width=True)

except Exception as e:
    st.error(f"Error al cargar las estadísticas: {e}")
    st.info("Asegúrate de que el archivo gluck_data.db esté en la raíz del proyecto y tenga los datos correctos.")