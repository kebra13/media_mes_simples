import pandas as pd

# Faturamento mensal de cada Estado
sp = 6783643
rj = 3667866
mg = 2922988
es = 2716548
outros = 1984953

# Somando o fat. total
fat_total = sp + rj + mg + es + outros

def calcular_porcentagem(estado, fat_total):
    # Realiza o calculo de porcentagem dado os parametros acima
    porcentagem = estado/fat_total * 100
    return porcentagem

# Utilizo listas dentro de um dicionário para associar os dados
dados = {
    "Estado": ["SP", "RJ", "MG", "ES", 'Outros'],
    "Fat. Mensal": [sp, rj, mg, es, outros],
    "Porcentagem Fat.": [f"{calcular_porcentagem(sp, fat_total):.2f}%", f"{calcular_porcentagem(rj, fat_total):.2f}%",
                         f"{calcular_porcentagem(mg, fat_total):.2f}%", f"{calcular_porcentagem(es, fat_total):.2f}%",
                         f"{calcular_porcentagem(outros, fat_total):.2f}%"]
}

# Funcao DataFrame do módulo pandas para organizar os dados
df = pd.DataFrame(dados)

print(df)