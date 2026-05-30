def calcular_rentabilidade(custo, venda):
    if custo <= 0:
        raise ValueError("Custo deve ser maior que zero")

    return ((venda - custo) / custo) * 100