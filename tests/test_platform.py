"""
SUITE DE PRUEBAS UNITARIAS Y DE INTEGRACIÓN (QUALITY GATES G1 - G10)
JD Group AXM · Verificación Automatizada del Sistema
"""

import unittest
import os
from src.services.data_service import get_current_trm, calculate_talent_income, DEFAULT_TRM_COP
from src.services.lead_service import save_lead, get_all_leads

class TestJDGroupPlatform(unittest.TestCase):

    def test_trm_service_resilience(self):
        """Verifica que el servicio de TRM retorne un valor numérico positivo válido."""
        trm = get_current_trm()
        self.assertIsInstance(trm, float)
        self.assertGreater(trm, 2000.0, "La TRM debe ser coherente con el tipo de cambio COP/USD")

    def test_income_calculator_sede_low(self):
        """Verifica la escala base del 50% en Sede Temática con producción < 400 USD brutos."""
        # 20 horas * 60 tokens/hr * 0.05 = 60 USD brutos (< 400 USD) -> 50%
        calc_low = calculate_talent_income(
            horas_semana=20,
            dias_semana=4,
            nivel_experiencia="Nuevo (Sin Experiencia)",
            modalidad="Sede Temática (Estudio - Armenia)",
            trm=4100.0
        )
        self.assertEqual(calc_low["comision_porcentaje"], 50.0)
        self.assertAlmostEqual(calc_low["ganancia_neta_semana_usd"], calc_low["ganancia_bruta_semana_usd"] * 0.5)

    def test_income_calculator_sede_high(self):
        """Verifica la escala avanzada del 60% en Sede Temática con producción >= 400 USD brutos."""
        # 48 horas * 200 tokens/hr * 0.05 = 480 USD brutos (> 400 USD) -> 60%
        calc_high = calculate_talent_income(
            horas_semana=48,
            dias_semana=6,
            nivel_experiencia="Avanzado / Bilingüe",
            modalidad="Sede Temática (Estudio - Armenia)",
            trm=4100.0
        )
        self.assertEqual(calc_high["comision_porcentaje"], 60.0)
        self.assertAlmostEqual(calc_high["ganancia_neta_semana_usd"], calc_high["ganancia_bruta_semana_usd"] * 0.6)

    def test_income_calculator_satelite(self):
        """Verifica la escala de comisiones en Modalidad Satélite (80% a 95%)."""
        calc_sat = calculate_talent_income(
            horas_semana=36,
            dias_semana=5,
            nivel_experiencia="Intermedio (Acompañamiento)",
            modalidad="Satélite (Desde Casa / Remoto)",
            trm=4100.0
        )
        self.assertIn(calc_sat["comision_porcentaje"], [80.0, 85.0, 90.0, 95.0])
        self.assertGreater(calc_sat["ganancia_neta_mes_cop"], 0)

    def test_lead_vault_persistence(self):
        """Verifica el guardado y recuperación de un lead en la bóveda segura."""
        record = save_lead(
            nombre="Test Aspirante QA",
            whatsapp="+573009998877",
            edad=22,
            ciudad="Armenia",
            modalidad="Sede Física (Armenia)",
            horario="Tarde (2 PM - 10 PM)",
            comentarios="Prueba automatizada de QA",
            habeas_data=True
        )
        self.assertTrue(record["radicado_id"].startswith("AXM-"))
        self.assertTrue(record["habeas_data_autorizado"])
        
        all_leads = get_all_leads()
        self.assertTrue(any(l["radicado_id"] == record["radicado_id"] for l in all_leads))

if __name__ == "__main__":
    unittest.main()
