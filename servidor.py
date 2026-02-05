from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from core.atomo import NucleoAtomico
import uvicorn

app = FastAPI()
nucleo = NucleoAtomico()
cofre_alexandre = 0.0

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("web/index.html", "r") as f:
        return f.read()

@app.get("/api/nano_status")
async def nano_status():
    global cofre_alexandre
    valor = nucleo.calcular_entropia()
    if valor >= 99.98:
        cofre_alexandre += 0.05
    return {"integridade": valor, "saldo": round(cofre_alexandre, 2)}

if __name__ == "__main__":
    print("\n🏛️ REDE INC.io - MODO MINERAÇÃO ATIVO")
    print("🔗 ACESSE: http://127.0.0.1:8000\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)
