import streamlit as st

st.set_page_config(page_title="Marco Teórico", page_icon="📚")
st.title("📚 Marco Teórico")

st.write("Esta sección está diseñada como material de apoyo para comprender las métricas utilizadas en los análisis posteriores.")

st.markdown("""
* **Customer Lifetime Value (CLV) y Segmentación:** La base de datos clasifica a los clientes en segmentos clave (*Loyal, New, At-Risk, Churned*). Esto se relaciona con los modelos RFM (Recency, Frequency, Monetary value).
* **Métricas de Web Analytics:**
    * **Bounce Rate (Tasa de Rebote):** Porcentaje de visitantes que abandonan el sitio después de ver una sola página.
    * **Pages per Session:** Indicador de engagement; cuántas páginas navega un usuario en promedio.
* **Métricas de Marketing Digital:**
    * **CTR (Click-Through Rate):** Clics obtenidos divididos por las impresiones. Mide la relevancia del anuncio.
    * **CPM (Cost Per Mille):** Costo por cada mil impresiones del anuncio.
    * **Conversiones:** Acciones valiosas completadas por el usuario (compras, registros).
""")