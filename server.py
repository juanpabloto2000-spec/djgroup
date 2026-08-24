"""
JD GROUP AXM -- ULTRA-LUXURY WEB APPLICATION SERVER
Servidor HTTP de Alta Velocidad con Endpoints REST API de Persistencia
Armenia, Quindio
"""

import http.server
import socketserver
import os
import json
import webbrowser
import threading

PORT = 8505
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
VAULT_FILE = os.path.join(DATA_DIR, "leads_vault.json")

def ensure_vault_file():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)

class LuxuryAppHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/leads":
            ensure_vault_file()
            try:
                with open(VAULT_FILE, "r", encoding="utf-8") as f:
                    leads = json.load(f)
            except Exception:
                leads = []
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(leads, ensure_ascii=False).encode("utf-8"))
            return
        elif self.path == "/":
            self.path = "/index.html"
            return super().do_GET()
        else:
            return super().do_GET()

    def do_POST(self):
        if self.path == "/api/leads":
            ensure_vault_file()
            content_length = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_length)
            try:
                new_lead = json.loads(post_body.decode("utf-8"))
                with open(VAULT_FILE, "r", encoding="utf-8") as f:
                    leads = json.load(f)
                leads.append(new_lead)
                with open(VAULT_FILE, "w", encoding="utf-8") as f:
                    json.dump(leads, f, indent=2, ensure_ascii=False)
                
                self.send_response(201)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "radicado_id": new_lead.get("radicado_id")}).encode("utf-8"))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
                return
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    ensure_vault_file()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), LuxuryAppHandler) as httpd:
        print(f"============================================================")
        print(f"JD GROUP AXM -- ULTRA-LUXURY WEB PLATFORM ONLINE")
        print(f"Armenia, Quindio | Sensory Luxury & Digital Intimacy")
        print(f"Servidor Activo en: http://localhost:{PORT}")
        print(f"============================================================")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()

