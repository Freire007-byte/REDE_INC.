import time

# Data de início da REDE INC (5 de Fevereiro de 2026)
START_TIME = 1738756800 

@app.get("/api/nano_status")
async def nano_status():
    agora = time.time()
    # Ganha 0.01 INC por segundo desde o início
    saldo_atual = (agora - START_TIME) * 0.01 
    # A integridade oscila levemente para simular a entropia
    integridade = 99.90 + (time.time() % 0.09) 
    
    return {
        "saldo": round(saldo_atual, 2),
        "integridade": round(integridade, 2)
    }
