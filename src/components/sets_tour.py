"""
MÓDULO 02 — Recorrido Virtual por los Sets Temáticos
JD Group AXM · Sede Armenia, Quindío
"""

import streamlit as st

def render_sets_tour():
    """Renderiza el módulo interactivo de visualización de los sets de la sede física."""
    st.markdown("### 🏢 Recorrido Virtual por los Sets Temáticos de Armenia")
    st.write("Nuestras sedes físicas en el Quindío están equipadas con tecnología de última generación y acabados sensoriales ultra-lujosos.")
    
    tab1, tab2, tab3 = st.tabs(["Set Velvet Luxury 👑", "Set Neón Cyberpunk ⚡", "Set Nórdico Minimalista 🪵"])
    
    with tab1:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image("https://images.unsplash.com/photo-1540518614846-7eded433c457?q=80&w=600", caption="Jacuzzi Privado & Acabados de Terciopelo")
        with col2:
            st.markdown("#### Set Velvet Luxury")
            st.write(
                "Diseñado bajo el arquetipo de **El Amante**. Cuenta con una cama king-size con sábanas de seda, "
                "iluminación cálida domótica regulable, elegante jacuzzi/tina privado, espejos biselados y fondo "
                "de terciopelo negro y oro. Ideal para shows de retrato editorial y transmisiones exclusivas VIP."
            )
            
    with tab2:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image("https://images.unsplash.com/photo-1563089145-599997674d42?q=80&w=600", caption="Iluminación LED RGB Reactiva y Cámaras 4K")
        with col2:
            st.markdown("#### Set Neón Cyberpunk")
            st.write(
                "Inspirado en la tecnología y la estética de vanguardia 2026. Equipado con barras LED RGB direccionables, "
                "paneles acústicos geométricos, pantallas duales de 27 pulgadas, cámara réflex 4K y micrófono de condensador profesional. "
                "Aporta una atmósfera electrizante que atrae tráfico internacional de alto poder adquisitivo."
            )
            
    with tab3:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image("https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=600", caption="Ambiente Orgánico, Sereno y Luz Natural")
        with col2:
            st.markdown("#### Set Nórdico Minimalista")
            st.write(
                "Un ambiente luminoso, limpio y sereno que evoca armonía y elegancia natural. Paredes de madera clara, "
                "plantas decorativas seleccionadas, lencería de lino blanco y abundante luz calibrada de tres puntos. "
                "Ideal para transmisiones relajadas, ASMR, dinámicas casuales y creación de contenido para redes sociales."
            )
