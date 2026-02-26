from typing import Tuple

def calculator(valor: float, vip: bool) -> Tuple[float, float]:
    """
    Calcula desconto e valor final.
    Retorna (desconto, valor_final).
    Regras:
    - VIP e valor >= 100: 20%
    - Não VIP e valor >= 100: 10%
    - Caso contrário: 0
    """
    if vip and valor >= 100:
        desconto = valor * 0.2
    elif valor >= 100:
        desconto = valor * 0.1
    else:
        desconto = 0.0
    return desconto, valor - desconto

def ler_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número (ex.: 150.0).")

def ler_vip(prompt: str) -> bool:
    resposta = input(prompt).strip().lower()
    return resposta in ("sim", "s", "yes", "y")

def main():
    valor = ler_float("digite o valor da compra: ")
    vip = ler_vip("cliente VIP? (sim/nao): ")
    desconto, valor_final = calculator(valor, vip)
    print(f"desconto: R$ {desconto:.2f}")
    print(f"valor final: R$ {valor_final:.2f}")

if __name__ == "__main__":
    main()