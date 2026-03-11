import streamlit as st
import plotly.io as pio
import plotly.graph_objects as go

# Paleta de colores inspirada en "La Noche Estrellada"
AZUL_PROFUNDO = "#0A1828"     # Cielo nocturno de fondo
AZUL_COBALTO = "#173F5F"      # Tonos de los remolinos y el pueblo
CELESTE = "#20639B"           # Brillos en el cielo
AMARILLO_ESTRELLA = "#F6D55C" # Estrellas, luna y acentos principales
ORO_CALIDO = "#ED553B"        # Toques cálidos secundarios
BLANCO_LUNA = "#F8FAFC"       # Texto principal para alto contraste

def aplicar_css_noche_estrellada():
    """
    Inyecta CSS personalizado en Streamlit para modificar el fondo, 
    las tipografías y los elementos interactivos con el tema de Van Gogh.
    """
    css_van_gogh = f"""
    <style>
    /* Fondo principal de la aplicación */
    .stApp {{
        background-color: {AZUL_PROFUNDO};
        color: {BLANCO_LUNA};
    }}
    
    /* Fondo del menú lateral (Sidebar) */
    [data-testid="stSidebar"] {{
        background-color: {AZUL_COBALTO};
    }}
    
    /* Estilo de títulos y encabezados */
    h1, h2, h3, h4, h5, h6 {{
        color: {AMARILLO_ESTRELLA} !important;
        font-family: 'Georgia', serif; /* Tipografía más clásica y artística */
    }}
    
    /* Botones interactivos */
    .stButton>button {{
        background-color: {CELESTE};
        color: {BLANCO_LUNA};
        border: 1px solid {AMARILLO_ESTRELLA};
        border-radius: 8px;
        transition: 0.3s;
    }}
    
    .stButton>button:hover {{
        background-color: {AMARILLO_ESTRELLA};
        color: {AZUL_PROFUNDO};
        border: 1px solid {BLANCO_LUNA};
    }}
    
    /* Color de las métricas numéricas */
    [data-testid="stMetricValue"] {{
        color: {AMARILLO_ESTRELLA} !important;
    }}
    </style>
    """
    st.markdown(css_van_gogh, unsafe_allow_html=True)

def configurar_graficos_plotly():
    """
    Crea y establece globalmente una plantilla de Plotly 
    que armoniza con el fondo de Streamlit.
    """
    plantilla_van_gogh = go.layout.Template()
    
    # Configuración del diseño base para Plotly
    plantilla_van_gogh.layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Transparente para fusionarse con Streamlit
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=BLANCO_LUNA),
        title=dict(font=dict(color=AMARILLO_ESTRELLA, size=20)),
        xaxis=dict(
            gridcolor=AZUL_COBALTO, 
            zerolinecolor=AZUL_COBALTO,
            tickfont=dict(color=CELESTE)
        ),
        yaxis=dict(
            gridcolor=AZUL_COBALTO, 
            zerolinecolor=AZUL_COBALTO,
            tickfont=dict(color=CELESTE)
        ),
        # Secuencia de colores para las barras, líneas y burbujas
        colorway=[AMARILLO_ESTRELLA, CELESTE, ORO_CALIDO, BLANCO_LUNA, AZUL_COBALTO]
    )
    
    # Registrar y aplicar la plantilla por defecto
    pio.templates["noche_estrellada"] = plantilla_van_gogh
    pio.templates.default = "noche_estrellada"