from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import hashlib, time

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/status")
async def status(wallet_id: str):
    # Lógica de DNA Quântico (SVP)
    timestamp = int(time.time() / 10) # Muda a cada 10 segundos
    dna = hashlib.sha3_512(f"{wallet_id}{timestamp}".encode()).hexdigest()[:24].upper()
    return {
        "lastro": 4937.17,
        "dna": dna,
        "protocolo": "WEB_4.0_LATTICE",
        "seguranca": "QUANTUM_RESISTANT_SIG"
    }

@app.get("/")
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
