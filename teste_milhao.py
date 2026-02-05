import asyncio, httpx, time

URL = "http://localhost:8000/enviar"
TOTAL = 1000000
CONCORRENCIA = 40

async def worker(name, total_por_worker):
    async with httpx.AsyncClient(timeout=None) as client:
        for i in range(total_por_worker):
            # params PRECISA estar recuado (identado) em relação ao for
            params = {
                "sender": "CORACAO_DA_REDE",
                "receiver": f"U{name}_{i}",
                "amount": 1.0,
                "pkey": "mestre"
            }
            try:
                t1 = time.time()
                await client.post(URL, params=params)
                if i % 500 == 0:
                    ms = (time.time() - t1) * 1000
                    print(f"W{name} | {i} txs | {ms:.2f}ms")
            except:
                pass

async def rodar():
    print("🚀 INICIANDO 1 MILHÃO NO SQLITE...")
    inicio = time.time()
    tasks = [worker(i, TOTAL//CONCORRENCIA) for i in range(CONCORRENCIA)]
    await asyncio.gather(*tasks)
    tps = TOTAL / (time.time() - inicio)
    print(f"\n🏆 FINALIZADO! TPS: {tps:.2f}")

if __name__ == "__main__":
    asyncio.run(rodar())
