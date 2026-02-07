from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3, os, time

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

DB_PATH = "inc_quantum_core.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Tabela de Contas Reais
    c.execute("CREATE TABLE IF NOT EXISTS accounts (wallet_id TEXT PRIMARY KEY, balance REAL, last_sync INTEGER)")
    # Saldo Inicial da Tesouraria
    c.execute("INSERT OR IGNORE INTO accounts VALUES ('CORACAO_DA_REDE', 1000000000.0, ?)", (int(time.time()),))
    conn.commit()
    conn.close()

init_db()

@app.get("/status")
async def status(wallet_id: str = "CORACAO_DA_REDE"):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Se a carteira não existe, cria com saldo zero
    c.execute("INSERT OR IGNORE INTO accounts VALUES (?, 0.0, ?)", (wallet_id, int(time.time())))
    conn.commit()
    
    c.execute("SELECT balance FROM accounts WHERE wallet_id = ?", (wallet_id,))
    user_bal = c.fetchone()[0]
    
    c.execute("SELECT balance FROM accounts WHERE wallet_id = 'CORACAO_DA_REDE'")
    treasury_bal = c.fetchone()[0]
    
    conn.close()
    return {
        "user_balance": user_bal,
        "treasury": treasury_bal,
        "status": "CONECTADO",
        "pqc": "LATTICE_ACTIVE"
    }

@app.post("/api/faucet")
async def faucet(wallet_id: str):
    # Função para teste: dá 10 INC para a nova carteira
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance = balance + 10 WHERE wallet_id = ?", (wallet_id,))
    c.execute("UPDATE accounts SET balance = balance - 10 WHERE wallet_id = 'CORACAO_DA_REDE'")
    conn.commit()
    conn.close()
    return {"status": "success"}
