"""
MÓDULO 03 — Lead Ingestion & Vault Service
JD Group AXM · Gestión Segura y Cifrada de Postulaciones
"""

import os
import json
import uuid
import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
VAULT_FILE = os.path.join(DATA_DIR, "leads_vault.json")

def ensure_data_directory():
    """Garantiza la existencia del directorio seguro de datos."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)

def save_lead(
    nombre: str,
    whatsapp: str,
    edad: int,
    ciudad: str,
    modalidad: str,
    horario: str,
    comentarios: str,
    habeas_data: bool
) -> dict:
    """
    Registra una nueva postulación de talento en la bóveda local con código de radicado único.
    """
    ensure_data_directory()
    
    radicado_id = f"AXM-{uuid.uuid4().hex[:6].upper()}"
    timestamp = datetime.datetime.now().isoformat()
    
    lead_record = {
        "radicado_id": radicado_id,
        "timestamp": timestamp,
        "nombre": nombre.strip(),
        "whatsapp": whatsapp.strip(),
        "edad": edad,
        "ciudad": ciudad,
        "modalidad": modalidad,
        "horario": horario,
        "comentarios": comentarios.strip(),
        "habeas_data_autorizado": habeas_data,
        "estado_gestion": "RECIBIDO_PENDIENTE_CONTACTO"
    }
    
    try:
        with open(VAULT_FILE, "r", encoding="utf-8") as f:
            leads = json.load(f)
    except Exception:
        leads = []
        
    leads.append(lead_record)
    
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)
        
    return lead_record

def get_all_leads() -> list:
    """Recupera la lista de postulaciones registradas en la bóveda."""
    ensure_data_directory()
    try:
        with open(VAULT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []
