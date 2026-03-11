import streamlit as st
import plotly.io as pio
import plotly.graph_objects as go

# Paleta de Colores Exclusiva "La Noche Estrellada Impresionante"
NEG_NOCHE = "#020812"         # Fondo base ultra oscuro
AZUL_PROFUNDO_SWIRL = "#0A1828" # Base de los remolinos
AZUL_COBALTO_MEDIUM = "#1A4F7A"  # Brillo medio del cielo
AZUL_CELESTE_BRIGHT = "#297FB8"  # Brillo intenso
AMARILLO_LUNA_HOT = "#FDFD96"   # Títulos principales (brillo intenso)
ORO_ESTRELLA = "#F1C40F"       # Acentos y bordes de gráficos
BLANCO_LUNA_SOFT = "#F8F9FA"   # Texto de párrafo (máximo contraste legible)

def aplicar_css_noche_estrellada_impresionante():
    """
    Inyecta CSS avanzado para recrear la textura, movimiento y brillo
    de La Noche Estrellada de Van Gogh en toda la interfaz de Streamlit.
    """
    css_van_gogh_impresionante = f"""
    <style>
    /* 1. Fondo Dinámico con Efecto de Remolino (Swirl) */
    .stApp {{
        background: 
            radial-gradient(circle at 70% 20%, {AZUL_COBALTO_MEDIUM} 0%, transparent 40%),
            radial-gradient(circle at 30% 60%, {AZUL_PROFUNDO_SWIRL} 0%, transparent 50%),
            linear-gradient(135deg, {NEG_NOCHE} 0%, {AZUL_PROFUNDO_SWIRL} 100%);
        background-attachment: fixed;
        color: {BLANCO_LUNA_SOFT};
        font-family: 'Playfair Display', serif; /* Tipografía más artística y dramática */
    }}

    /* 2. Panel Lateral (Sidebar) como el Ciprés Oscuro */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #010409 0%, {NEG_NOCHE} 100%);
        border-right: 1px solid {AZUL_COBALTO_MEDIUM};
    }}
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {{
        color: {AMARILLO_LUNA_HOT} !important;
        text-shadow: 0 0 10px {ORO_ESTRELLA};
    }}

    /* 3. Títulos Principales con Brillo Estelar (Glow) */
    h1, h2 {{
        color: {AMARILLO_LUNA_HOT} !important;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 
            0 0 10px {ORO_ESTRELLA},
            0 0 20px {ORO_ESTRELLA},
            0 0 30px {AMARILLO_LUNA_HOT};
        margin-bottom: 30px !important;
    }}
    
    h3, h4, h5 {{
        color: {ORO_ESTRELLA} !important;
        font-family: 'Lora', serif; /* Subtítulos más elegantes */
        font-weight: 600;
        text-shadow: 0 0 5px rgba(241, 196, 15, 0.5);
    }}

    /* 4. Tarjetas y Contenedores con Efecto de Flotación y Brillo */
    .stDataFrame, .stPlotlyChart, [data-testid="stMetric"], .stMarkdown > div[data-testid="stMarkdownContainer"] {{
        background-color: rgba(10, 24, 40, 0.5) !important; /* Transparente para ver el swirl */
        backdrop-filter: blur(5px); /* Efecto de vidrio esmerilado */
        border-radius: 15px !important;
        border: 1px solid rgba(41, 127, 184, 0.3) !important;
        box-shadow: 0 4px 15px rgba(2, 8, 18, 0.5) !important;
        padding: 20px !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }}
    
    .stDataFrame:hover, .stPlotlyChart:hover, [data-testid="stMetric"]:hover {{
        transform: translateY(-5px); /* Pequeño salto al pasar el mouse */
        box-shadow: 0 8px 25px rgba(41, 127, 184, 0.4) !important;
        border: 1px solid {AZUL_CELESTE_BRIGHT} !important;
    }}

    /* 5. Botones Artísticos */
    .stButton>button {{
        background: linear-gradient(135deg, {AZUL_PROFUNDO_SWIRL} 0%, {AZUL_COBALTO_MEDIUM} 100%);
        color: {BLANCO_LUNA_SOFT};
        border: 1px solid {ORO_ESTRELLA};
        border-radius: 30px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s all ease;
        box-shadow: 0 0 10px rgba(241, 196, 15, 0.2);
    }}
    
    .stButton>button:hover {{
        background: {AMARILLO_LUNA_HOT};
        color: {NEG_NOCHE};
        box-shadow: 0 0 20px {AMARILLO_LUNA_HOT};
        border: 1px solid {BLANCO_LUNA_SOFT};
    }}

    /* 6. Tabs Personalizadas */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: transparent;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: {BLANCO_LUNA_SOFT} !important;
        background-color: rgba(26, 79, 122, 0.3);
        border-radius: 10px 10px 0 0;
        margin-right: 5px;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        background-color: rgba(41, 127, 184, 0.5);
    }}
    .stTabs [data-baseweb="tab-highlight"] {{
        background-color: {ORO_ESTRELLA};
    }}
    
    /* 7. Fuentes de Google */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:wght@400;600&display=swap');
    </style>
    """
    st.markdown(css_van_gogh_impresionante, unsafe_allow_html=True)

def configurar_graficos_plotly_impresionante():
    """
    Crea y establece globalmente una plantilla de Plotly ultra dramática
    donde los gráficos parecen brillar sobre el cielo nocturno.
    """
    plantilla_van_gogh = go.layout.Template()
    
    # Configuración del diseño base para Plotly
    plantilla_van_gogh.layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Totalmente transparente
        plot_bgcolor='rgba(10, 24, 40, 0.3)', # Fondo sutil de los ejes
        font=dict(color=BLANCO_LUNA_SOFT, family="'Lora', serif"),
        title=dict(font=dict(color=AMARILLO_LUNA_HOT, size=24, family="'Playfair Display', serif")),
        
        # Ejes como el viento cobalto
        xaxis=dict(
            gridcolor=rgba(26, 79, 122, 0.3), 
            zerolinecolor=rgba(26, 79, 122, 0.5),
            tickfont=dict(color=AZUL_CELESTE_BRIGHT)
        ),
        yaxis=dict(
            gridcolor=rgba(26, 79, 122, 0.3), 
            zerolinecolor=rgba(26, 79, 122, 0.5),
            tickfont=dict(color=AZUL_CELESTE_BRIGHT)
        ),
        
        # Secuencia de colores: Amarillo Luna -> Oro -> Celeste -> Blanco -> Cobalto
        colorway=[AMARILLO_LUNA_HOT, ORO_ESTRELLA, AZUL_CELESTE_BRIGHT, BLANCO_LUNA_SOFT, AZUL_PROFUNDO_SWIRL]
    )
    
    # Registrar y aplicar la plantilla por defecto
    pio.templates["noche_estrellada_impresionante"] = plantilla_van_gogh
    pio.templates.default = "noche_estrellada_impresionante"
