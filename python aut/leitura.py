# ─── Leitura ────
def leitura(prompt: str = "Digite um valor: ") -> int:
    """Solicita e retorna um número inteiro digitado pelo usuário (validação)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")


# ─── Classificação ────
def classificar_valor(valor: int) -> str:
    """Classifica o valor como 'Baixo', 'Normal' ou 'Alto'."""
    if valor < 20:
        return "Baixo"
    if valor <= 30:
        return "Normal"
    return "Alto"


# ─── Exibição ───
def exibir_classificacao(classificacao: str) -> None:
    """Exibe no terminal a classificação obtida."""
    print(f"Classificação: {classificacao}")


# ─── Envio ────
def enviar() -> bool:
    """Simula o envio dos dados e confirma com 'OK'."""
    print("Enviando... OK")
    return True


# ─── Programa Principal ───
def executar() -> None:
    """Etapas: leitura, classificação, exibição e envio."""
    valor = leitura()
    classificacao = classificar_valor(valor)
    exibir_classificacao(classificacao)
    if enviar():
        print("Concluído.")


# Ponto de entrada do programa
if __name__ == "__main__":
    executar()