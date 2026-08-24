"""
MÓDULO 04 (M04) — Dynamic Data Services & Asset Engine
JD Group AXM · Servicios de TRM y Datos Financieros
"""

import requests

DEFAULT_TRM_COP = 4100.0
TOKEN_VALUE_USD = 0.05

def get_current_trm() -> float:
    """
    Obtiene la Tasa Representativa del Mercado (USD/COP).
    Posee mecanismo de fallback seguro para garantizar disponibilidad constante.
    """
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=2.0)
        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates", {})
            cop_rate = rates.get("COP")
            if cop_rate and isinstance(cop_rate, (int, float)):
                return float(cop_rate)
    except Exception:
        pass
    return DEFAULT_TRM_COP

def calculate_talent_income(
    horas_semana: int,
    dias_semana: int,
    nivel_experiencia: str,
    modalidad: str,
    trm: float
) -> dict:
    """
    Calcula las proyecciones de ingresos brutos y netos basados en las reglas de negocio de JD Group AXM:
    - Sede Temática (Armenia): 50% base, escala al 60% superando 400 USD brutos semanales.
    - Satélite Remoto: Escala progresiva del 80% al 95%.
    """
    # Tokens generados promedio por hora según nivel de desenvolvimiento e idiomas
    base_tokens_hora = 60.0
    if nivel_experiencia == "Intermedio (Acompañamiento)":
        base_tokens_hora = 120.0
    elif nivel_experiencia == "Avanzado / Bilingüe":
        base_tokens_hora = 200.0
        
    ganancia_bruta_semana = horas_semana * base_tokens_hora * TOKEN_VALUE_USD
    
    if modalidad == "Sede Temática (Estudio - Armenia)":
        comision_porcentaje = 50.0 if ganancia_bruta_semana < 400.0 else 60.0
    else:  # Modalidad Satélite
        if ganancia_bruta_semana < 300.0:
            comision_porcentaje = 80.0
        elif ganancia_bruta_semana < 600.0:
            comision_porcentaje = 85.0
        elif ganancia_bruta_semana < 1000.0:
            comision_porcentaje = 90.0
        else:
            comision_porcentaje = 95.0
            
    ganancia_neta_semana_usd = ganancia_bruta_semana * (comision_porcentaje / 100.0)
    ganancia_neta_mes_usd = ganancia_neta_semana_usd * 4.33
    ganancia_neta_mes_cop = ganancia_neta_mes_usd * trm
    horas_totales_mes = horas_semana * 4.33
    
    return {
        "ganancia_bruta_semana_usd": ganancia_bruta_semana,
        "comision_porcentaje": comision_porcentaje,
        "ganancia_neta_semana_usd": ganancia_neta_semana_usd,
        "ganancia_neta_mes_usd": ganancia_neta_mes_usd,
        "ganancia_neta_mes_cop": ganancia_neta_mes_cop,
        "horas_totales_mes": horas_totales_mes,
        "trm_aplicada": trm
    }
