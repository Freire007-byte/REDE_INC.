from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Rota para o Painel Visual
@app.get("/")
async def read_index():
    # Isso busca o arquivo na pasta web
    return FileResponse('web/index.html')

# Sua rota de API existente
@app.get("/api/nano_status")
async def nano_status():
    return {"saldo": 100.0, "integridade": 99.98} # Exemplo
