"""
MÓDULO 00 (M00) — Core Design System & Tokens
JD Group AXM · Sensory Luxury & Digital Intimacy
"""

import streamlit as st

# Tokens Cromáticos Nucleares
COLOR_NEGRO_CARBON = "#0A0A0C"
COLOR_ORO_CHAMPAN = "#C5A059"
COLOR_ORO_BRILLANTE = "#D4AF37"
COLOR_NEON_MAGENTA = "#D946EF"
COLOR_BLANCO_HUMO = "#F4F4F6"
COLOR_PURPURA_ELECTRICO = "#8B5CF6"
COLOR_CARD_BG = "#121216"
COLOR_BORDER_MUTED = "#33333C"

CUSTOM_CSS = f"""
<style>
    /* 1. Fondo Global y Tipografía Base */
    .stApp {{
        background-color: {COLOR_NEGRO_CARBON} !important;
        color: {COLOR_BLANCO_HUMO} !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }}
    
    /* 2. Encabezados de Lujo */
    h1, h2, h3 {{
        color: {COLOR_ORO_BRILLANTE} !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }}
    h4, h5, h6 {{
        color: {COLOR_ORO_CHAMPAN} !important;
        font-weight: 600 !important;
    }}
    
    /* 3. Textos con Efecto Neón */
    .neon-text {{
        color: {COLOR_NEON_MAGENTA} !important;
        text-shadow: 0 0 10px rgba(217, 70, 239, 0.5), 0 0 20px rgba(217, 70, 239, 0.3) !important;
    }}
    
    /* 4. Botones Principales con Gradiente Oro */
    div.stButton > button {{
        background: linear-gradient(135deg, {COLOR_ORO_BRILLANTE} 0%, {COLOR_ORO_CHAMPAN} 100%) !important;
        color: {COLOR_NEGRO_CARBON} !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100%;
    }}
    div.stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 22px rgba(212, 175, 55, 0.55) !important;
        color: {COLOR_BLANCO_HUMO} !important;
    }}
    
    /* 5. Tarjeta VIP Glass/Dark */
    .vip-card {{
        background-color: {COLOR_CARD_BG};
        border: 1px solid {COLOR_ORO_CHAMPAN};
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
    }}
    
    /* 6. Banner de Seguridad y Geobloqueo */
    .security-banner {{
        background: linear-gradient(90deg, rgba(139, 92, 246, 0.15) 0%, rgba(219, 39, 119, 0.1) 100%);
        border-left: 5px solid {COLOR_PURPURA_ELECTRICO};
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 20px;
    }}
    
    /* 7. Contenedores de Inputs y Selectores */
    .stSelectbox, .stSlider, .stTextInput, .stTextArea, .stNumberInput {{
        background-color: {COLOR_CARD_BG} !important;
        border-radius: 8px !important;
        border: 1px solid {COLOR_BORDER_MUTED} !important;
        padding: 6px !important;
    }}
    
    /* 8. Separadores estilizados */
    hr {{
        border-color: {COLOR_BORDER_MUTED} !important;
        margin: 24px 0 !important;
    }}
</style>
"""

def inject_theme():
    """Inyecta el sistema de diseño y tokens CSS en la sesión de Streamlit."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
