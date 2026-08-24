"""
THE HOUSE — PRIVATE TALENT HOUSE
Plataforma Web Editorial de Alta Costura
Armenia, Quindío
"""

import streamlit as st
import os
import streamlit.components.v1 as components

# 1. Configuración de página
st.set_page_config(
    page_title="THE HOUSE | Private Talent House · Armenia",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Ocultar barras y paddings por defecto de Streamlit
st.markdown("""
<style>
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    div[data-testid="stToolbar"] {visibility: hidden !important;}
    div[data-testid="stDecoration"] {visibility: hidden !important;}
    div[data-testid="stStatusWidget"] {visibility: hidden !important;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
    }
    iframe {
        border: none !important;
        width: 100vw !important;
        height: 100vh !important;
        min-height: 100vh !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Cargar y empaquetar el frontend cinemático
base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, "index.html")
css_path = os.path.join(base_dir, "css", "luxury.css")
js_path = os.path.join(base_dir, "js", "app.js")

try:
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()

    bundled_html = html_content.replace(
        '<link rel="stylesheet" href="css/luxury.css">',
        f"<style>\n{css_content}\n</style>"
    )
    bundled_html = bundled_html.replace(
        '<script src="js/app.js"></script>',
        f"<script>\n{js_content}\n</script>"
    )

    components.html(bundled_html, height=4400, scrolling=True)

except Exception as e:
    st.error(f"Error al cargar los artefactos visuales: {e}")
