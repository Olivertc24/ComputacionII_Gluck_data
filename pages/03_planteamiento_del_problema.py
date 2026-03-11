import streamlit as st

st.set_page_config(page_title="Planteamiento del Problema", page_icon="🧩")
st.title("🧩 Planteamiento del Problema")

st.write("""
En el entorno actual del comercio electrónico, las empresas generan vastas cantidades de datos aislados. El equipo de marketing gestiona sus campañas (`campaign_data`), el equipo de producto revisa las ventas (`sales_data`), y el equipo de IT o UX analiza el tráfico (`web_analytics`). 

**El Problema:**
La falta de integración entre estas bases de datos impide tener una visión 360° del negocio. Por ejemplo:
* ¿Sabemos si la campaña con mayor gasto publicitario realmente atrae a los clientes más leales?
* ¿Estamos perdiendo clientes ("Churned") debido a una mala experiencia en la web (alta tasa de rebote) o en un dispositivo específico?

Este proyecto busca centralizar y analizar esta información estructurada en SQLite para transformar datos crudos en *insights* accionables.
""")