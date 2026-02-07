from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Estado Global em Memória (Otimizado para Vercel Serverless)
rede_estado = {
    "tesouraria": 75283.03,
    "blocos": 128,
    "status": "OPERACIONAL_PQC"
}

@app.get("/status")
async def status():
    return {
        "tesouraria": round(rede_estado["tesouraria"], 2),
        "blocos": rede_estado["blocos"],
        "status": rede_estado["status"]
    }

@app.post("/enviar")
async def enviar(destinatario: str, valor: float):
    # Lógica de processamento imediato
    if valor > 0:
        rede_estado["tesouraria"] -= valor
        rede_estado["blocos"] += 1
        return {"status": "sucesso_ledger"}
    return {"status": "valor_invalido"}
