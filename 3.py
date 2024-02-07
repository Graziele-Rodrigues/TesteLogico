import json

# Função para calcular o menor, maior valor e dias com faturamento acima da média
def calcula_faturamento(faturamento):
    menor_valor = min(faturamento, key=lambda x: x["valor"])["valor"]
    maior_valor = max(faturamento, key=lambda x: x["valor"])["valor"]
    media_mensal = sum(dia["valor"] for dia in faturamento) / len(faturamento)
    dias_acima_media = sum(1 for dia in faturamento if dia["valor"] > media_mensal)
    return menor_valor, maior_valor, dias_acima_media

# Leitura dos dados do arquivo JSON
with open("dados.json", "r") as file:
    dados = json.load(file)

# Chamada da função para calcular as estatísticas
menor_valor, maior_valor, dias_acima_media = calcula_faturamento(dados)

# Impressão dos resultados
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
