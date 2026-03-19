import json

with open("sensores_json.json", "r") as arquivo:
    dados = json.load(arquivo)

for item in dados:
    temp = item['temperatura']

    if temp is None:
        print(f"{item['maquina']} -> ERRO: Sem leitura")
    elif temp > 90:
        print(f"{item['maquina']} -> ALERTA DE TEMPERATURA")
    else:
        print(f"{item['maquina']} -> OK")