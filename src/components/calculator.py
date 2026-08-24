"""
MÓDULO 02 — Calculadora Interactiva de Proyecciones Financieras
JD Group AXM · Motor de Cálculo Dinámico en USD y COP
"""

import streamlit as st
from src.services.data_service import calculate_talent_income

def render_calculator(trm: float):
    """Renderiza el simulador de ingresos reactivo con sliders y tarjetas VIP."""
    st.markdown("### 📊 Calculadora Interactiva de Proyección Financiera (USD/COP)")
    st.write(
        "Nuestra estructura financiera está basada en los mayores estándares de transparencia de la industria, "
        "con una escala de comisiones progresiva y sin manipulación del valor de los tokens."
    )
    
    col_ctrl, col_res = st.columns([1, 1])
    
    with col_ctrl:
        st.markdown("##### ⚙️ Configura tu Plan de Transmisión:")
        modalidad = st.selectbox(
            "Modalidad de Trabajo:",
            options=["Sede Temática (Estudio - Armenia)", "Satélite (Desde Casa / Remoto)"],
            key="calc_modalidad"
        )
        
        horas_semana = st.slider(
            "Horas de Transmisión Semanales:",
            min_value=20,
            max_value=48,
            value=36,
            step=4,
            key="calc_horas"
        )
        
        dias_semana = st.slider(
            "Días de Trabajo por Semana:",
            min_value=4,
            max_value=6,
            value=5,
            step=1,
            key="calc_dias"
        )
        
        nivel_experiencia = st.select_slider(
            "Nivel de Desenvolvimiento / Idioma:",
            options=["Nuevo (Sin Experiencia)", "Intermedio (Acompañamiento)", "Avanzado / Bilingüe"],
            value="Intermedio (Acompañamiento)",
            key="calc_nivel"
        )
        
    # Cálculo
    calc = calculate_talent_income(
        horas_semana=horas_semana,
        dias_semana=dias_semana,
        nivel_experiencia=nivel_experiencia,
        modalidad=modalidad,
        trm=trm
    )
    
    with col_res:
        st.markdown(
            f"<div class='vip-card'>"
            f"<h4 style='color: #D4AF37; margin-top: 0;'>Estimación Mensual de Ingresos Netos</h4>"
            f"<p style='font-size: 2.3em; color: #D946EF; margin: 6px 0; font-weight: bold;'>$ {calc['ganancia_neta_mes_usd']:,.2f} USD</p>"
            f"<p style='font-size: 1.45em; color: #F4F4F6; margin: 4px 0;'>≈ $ {calc['ganancia_neta_mes_cop']:,.0f} COP</p>"
            f"<hr style='border-color: #333; margin: 12px 0;' />"
            f"<div style='display: flex; justify-content: space-between; font-size: 0.9em; color: #aaa;'>"
            f"<span>Comisión: <strong style='color: #D4AF37;'>{calc['comision_porcentaje']:.0f}%</strong></span>"
            f"<span>TRM: <strong>1 USD = ${calc['trm_aplicada']:,.0f} COP</strong></span>"
            f"<span>Horas/Mes: <strong>{calc['horas_totales_mes']:.0f} hrs</strong></span>"
            f"</div>"
            f"<p style='font-size: 0.8em; color: #888; margin-top: 15px; font-style: italic;'>"
            f"*Proyección basada en desempeño y regularidad. Liquidaciones quincenales puntuales en los primeros 2 días hábiles."
            f"</p>"
            f"</div>",
            unsafe_allow_html=True
        )
