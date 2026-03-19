import csv

try:
    with open("sensores_com_erro.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(f"Máquina: {linha['maquina']}")
            print(f"Produção: {linha['pecas_produzidas']}")
            print("-" * 20)

except Exception as e:
    print(f"Erro: {e}")