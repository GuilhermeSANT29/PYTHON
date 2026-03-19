dados = [
    {"maquina": "M1", "temperatura": 75},
    {"maquina": "M2", "temperatura": 95},
    {"maquina": "M3", "temperatura": None}
]

for item in dados:
    temp = item['temperatura']

    if temp is None:
        print(f"{item['maquina']} -> ERRO: Sem leitura")
    elif temp > 90:
        print(f"{item['maquina']} -> ALERTA DE TEMPERATURA")
    else:
        print(f"{item['maquina']} -> OK")