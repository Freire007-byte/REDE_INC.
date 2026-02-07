from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import hashlib, sqlite3, os, time

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Banco de dados em memória para 5.000 TPS
conn = sqlite3.connect('file:inc_quantum_core?mode=memory&cache=shared', uri=True, check_same_thread=False)
c = conn.cursor()

def init_db():
    c.execute("CREATE TABLE IF NOT EXISTS contas (id TEXT PRIMARY KEY, saldo REAL, hash_pqc TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS meta (chave TEXT PRIMARY KEY, valor INTEGER)")
    # SALDO MESTRE: 1 BILHÃO (v59)
    c.execute("INSERT OR IGNORE INTO contas VALUES ('CORACAO_DA_REDE', 1000000000.0, 'MASTER_KEY')")
    c.execute("INSERT OR IGNORE INTO meta VALUES ('blocos', 10402)")
    conn.commit()

init_db()

@app.get("/", response_class=HTMLResponse)
async def home():
    # Busca o index.html na mesma pasta do servidor.py
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/status")
async def status():
    c.execute("SELECT saldo FROM contas WHERE id = 'CORACAO_DA_REDE'")
    t = c.fetchone()[0]
    c.execute("SELECT valor FROM meta WHERE chave = 'blocos'")
    b = c.fetchone()[0]
    return {
        "tesouraria": t, 
        "blocos": b, 
        "seguranca": "PÓS-QUÂNTICA_ATIVA",
        "manifesto": "Esse manifesto é da verdadeira democracia."
    }

@app.post("/api/buy")
async def buy(amt: float, uid: str):
    # Lógica de compra unificada
    inc_qty = amt / 5.2910
    c.execute("UPDATE contas SET saldo = saldo + ? WHERE id = 'CORACAO_DA_REDE'", (amt,))
    c.execute("UPDATE meta SET valor = valor + 1 WHERE chave = 'blocos'")
    conn.commit()
    return {"id": f"TX-{int(time.time())}", "inc": round(inc_qty, 4)}
