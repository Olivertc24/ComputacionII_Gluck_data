# 🌌 Portafolio de Análisis de Datos Omnicanal: E-commerce & Marketing

¡Bienvenido a mi portafolio interactivo! Este proyecto es una aplicación web construida con **Python** y **Streamlit** que analiza una base de datos de retail omnicanal (`gluck_data.db`). 

Además de exhibir habilidades analíticas avanzadas, la arquitectura modular de este repositorio está diseñada para servir como material de estudio práctico para iniciantes en la programación y la ciencia de datos.

## 🚀 Características Principales

* **Integración SQL nativa:** Módulo de conexión robusto utilizando `sqlite3` para consultas en crudo, demostrando buenas prácticas de extracción de datos.
* **Análisis de Ventas y Retención:** Cruce de datos demográficos y transaccionales para entender el comportamiento y segmentación de los clientes (Loyal, At-Risk, Churned, New).
* **Marketing Analytics:** Cálculo dinámico del Costo de Adquisición (CPA) y eficiencia de campañas publicitarias.
* **Visualización de Datos Interactiva:** Gráficos avanzados creados con `plotly.express`.
* **Diseño UI/UX Personalizado:** Tema visual inmersivo inspirado en la paleta de colores de *"La Noche Estrellada"* de Van Gogh, configurado a nivel global en Streamlit.

## 📁 Estructura del Directorio

El proyecto sigue una arquitectura modular y escalable (Separation of Concerns):

├── .devcontainer/          # Configuración del entorno de desarrollo (Docker/VS Code)
├── .streamlit/             # Configuración del tema oscuro nativo (config.toml)
├── pages/                  # Archivos multipágina de Streamlit (Análisis paso a paso)
├── utils/                  # Módulos auxiliares
│   ├── aesthetics.py       # Funciones CSS y paleta de colores de Plotly
│   └── database.py         # Motor de conexión y ejecución SQL con Pandas
├── app.py                  # Punto de entrada principal de la aplicación
├── gluck_data.db           # Base de datos local (SQLite)
└── requirements.txt        # Dependencias del proyecto

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto en tu máquina local, asegúrate de tener Python 3.9 o superior instalado.

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   cd nombre-del-repo
   ```

2. **Crea un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```
3. **Instala las dependencias:**
    ```bash
    pip install streamlit pandas plotly
    ```

## 💻 Uso

Para levantar la aplicación web en tu navegador local, ejecuta el siguiente comando en la raíz del proyecto:

    ```bash
    streamlit run app.py
    ```

Esto abrirá automáticamente una pestaña en tu navegador (usualmente en http://localhost:8501) donde podrás interactuar con los datos y el simulador de consultas SQL.
