import streamlit as st

st.set_page_config(page_title="Bases Legales", page_icon="⚖️")
st.title("⚖️ Bases Legales y Ética de Datos")

st.write("""
Dado que nuestra base de datos (`customer_data`) contiene información demográfica (Edad, Género) y de ubicación a nivel de ciudad/provincia en Argentina, el tratamiento de estos datos debe enmarcarse en normativas de privacidad.

### Consideraciones principales:
1. **Ley de Protección de los Datos Personales (Ley 25.326 - Argentina):** Garantiza el derecho al honor y a la intimidad de las personas, estableciendo que los datos deben ser ciertos, adecuados y pertinentes.
2. **Anonimización:** En este portafolio, los datos de los clientes están representados mediante un `ID` único (ej. datos bigint seudonimizados), sin exponer nombres, correos electrónicos ni documentos de identidad, cumpliendo con los estándares de disociación de la información.
3. **Consentimiento:** En un entorno real, la recolección de métricas web (`web_analytics`) y datos de marketing requieren la aceptación de políticas de cookies y términos de servicio por parte del usuario.
""")