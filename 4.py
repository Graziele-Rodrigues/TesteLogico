import json

# Definindo o faturamento mensal por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculando o total do faturamento mensal
total_faturamento = sum(faturamento_estados.values())

# Calculando o percentual de representação de cada estado
percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_estados.items()}

# Armazenando os dados em um arquivo JSON
with open("percentuais_faturamento.json", "w") as file:
    json.dump(percentuais, file, indent=4)

print("Percentuais de representação de cada estado no faturamento mensal foram armazenados no arquivo 'percentuais_faturamento.json'.")
