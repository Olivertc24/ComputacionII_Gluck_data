import streamlit as st
from utils.aesthetics import aplicar_css_noche_estrellada, configurar_graficos_plotly

st.set_page_config(page_title="Portafolio de Análisis", layout="wide")

# Aplicar el tema artístico
aplicar_css_noche_estrellada_impresionante()
configurar_graficos_plotly_impresionante()

st.title("📊 Portafolio de Análisis y Ciencia de Datos")

# Configuración inicial de la página (debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="Portafolio de Análisis de Datos",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Portafolio de Análisis y Ciencia de Datos")

st.write("""
¡Bienvenido! Utiliza el menú lateral izquierdo para navegar a través de las diferentes secciones de este proyecto.

Este portafolio aborda desde el planteamiento teórico hasta el análisis en profundidad de métricas de ventas, perfiles de clientes y campañas de marketing.
""")

st.info("👈 Selecciona una página en el panel de navegación para comenzar.")
