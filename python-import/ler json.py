import json

try:
    with open("sensores_Json.json", "r") as arquivos:
        dados = json.load(arquivos)
 
    for item in dados:
        print(f"máquina: {item['maquina']}")
        print(f"temperatura: {item['temperatura']}")
        print(f"status: {item['status']}")
        print("_" * 20)

except FileNotFoundError:
    print("Arquivo não encontrado!")

except Exception as e:
    print(f"erro: {e}")