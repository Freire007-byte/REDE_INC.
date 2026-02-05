import random

class NucleoAtomico:
    def __init__(self):
        self.integridade_malha = 99.98

    def calcular_entropia(self):
        variacao = random.uniform(-0.05, 0.05)
        self.integridade_malha = round(max(95.0, min(100.0, self.integridade_malha + variacao)), 2)
        return self.integridade_malha