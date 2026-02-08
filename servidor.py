from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import hashlib, time, random

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/status")
async def status(wallet_id: str):
    # Simulação da Auto-Regeneração: O DNA muda mas a integridade (Lastro) é imutável
    seed = f"{wallet_id}{int(time.time())}"
    quantum_dna = hashlib.sha3_256(seed.encode()).hexdigest()[:24].upper()
    
    return {
        "lastro": 4937.17,
        "dna": quantum_dna,
        "bots": 1000000000 - random.randint(0, 1000),
        "mesh_integrity": "100%",
        "mode": "SELF_HEALING_ACTIVE"
    }

@app.get("/")
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
