# REDE INC.io - Módulo de Tesouraria Atómica
# Autor: Arquiteto Alexandre Freire

def processar_taxa_democratica(valor_total):
    """
    Aplica a Regra Imutável de 2% sobre qualquer transação.
    O valor é destinado ao CORACAO_DA_REDE para manutenção da soberania.
    """
    taxa = valor_total * 0.02
    valor_final = valor_total - taxa
    
    return {
        "valor_liquido": round(valor_final, 2),
        "taxa_inc": round(taxa, 2),
        "destino_taxa": "CORACAO_DA_REDE"
    }
