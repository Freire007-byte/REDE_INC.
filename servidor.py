from fastapi import FastAPI
from fastapi.responses import FileResponse
import time
import os

app = FastAPI()

# Marco Zero da REDE INC (5 de Fev de 2026)
START_TIME = 1738756800 

@app.get("/")
async def read_index():
    return FileResponse('web/index.html')

@app.get("/api/nano_status")
async def nano_status():
    agora = time.time()
    # Mineração constante: 0.01 INC por segundo
    saldo_calculado = (agora - START_TIME) * 0.01 
    # Oscilação da Entropia
    integridade = 99.90 + (time.time() % 0.08)
    
    return {
        "saldo": round(saldo_calculado, 2),
        "integridade": round(integridade, 2)
    }
