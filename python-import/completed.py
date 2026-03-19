import json
import csv

# Ler JSON
with open("sensores_json.json", "r") as f:
    sensores = json.load(f)

# Ler CSV e transformar em dicionário
producao = {}
with open("producao.csv", "r") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        producao[linha["maquina"]] = int(linha["pecas_produzidas"])

# Variáveis para relatório
total_maquinas = 0
alertas = 0
soma_temp = 0
count_temp = 0

# Processamento
for item in sensores:
    maquina = item["maquina"]
    temp = item["temperatura"]
    prod = producao.get(maquina, 0)

    total_maquinas += 1

    if temp is None:
        status = "ERRO"
    elif temp > 90:
        status = "CRITICO"
        alertas += 1
        soma_temp += temp
        count_temp += 1
    else:
        status = "OK"
        soma_temp += temp
        count_temp += 1

    print(f"{maquina} - Temp: {temp} - Produção: {prod} - {status}")

# Relatório
media_temp = soma_temp / count_temp if count_temp > 0 else 0

print("\n--- RELATÓRIO ---")
print(f"Total de máquinas: {total_maquinas}")
print(f"Máquinas em alerta: {alertas}")
print(f"Média de temperatura: {media_temp:.2f}")