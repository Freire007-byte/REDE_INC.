import httpx, time, os

def ver_status():
    while True:
        try:
            r = httpx.get("http://localhost:8000/status").json()
            os.system('clear')
            print("🟢 REDE INC.io - MONITOR DE PERFORMANCE")
            print("-" * 40)
            print(f"💰 TESOURARIA: ${r['tesouraria']:,.2f}")
            print(f"📦 BLOCOS:     {r['blocos']}")
            print(f"⚡ TPS EST.:   {r['tps']}")
            print("-" * 40)
            print("Pressione Ctrl+C para sair")
        except:
            print("🔴 Aguardando servidor...")
        time.sleep(0.5)

if __name__ == "__main__":
    ver_status()
