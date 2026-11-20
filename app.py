import streamlit as st

st.set_page_config(
    page_title="Mi primera app",
    page_icon="🚌"
)

st.title("🚌 Dashboard de Transporte")

linea = st.selectbox(
    "Selecciona una línea",
    ["H12", "D20", "V15", "V21"]
)

st.metric(
    "Validaciones",
    "12.345"
)

st.success(f"Línea seleccionada: {linea}")
