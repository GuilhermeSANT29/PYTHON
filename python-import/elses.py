import csv

dados = []

with open("sensores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        dados.append(linha)

for item in dados:
    maquina = item.get('maquina', 'DESCONHECIDA')
    temp = item.get('temperatura', '').strip()

    if temp == "":
        print(f"{maquina} -> ERRO")
        continue

    try:
        temp_valor = float(temp)
    except ValueError:
        print(f"{maquina} -> DADO INVALIDO")
        continue

    if temp_valor > 90:
        print(f"{maquina} -> ALERTA")
    else:
        print(f"{maquina} -> OK")