def calcular_rendimento_investimento(valor_inicial, taxa_juros, anos, capitalizacao='anual'):
    """
    Calcula o rendimento de um investimento com base em juros compostos.
    
    :param valor_inicial: Valor inicial do investimento
    :param taxa_juros: Taxa de juros anual em percentual
    :param anos: Período do investimento em anos
    :param capitalizacao: Tipo de capitalização: 'mensal' ou 'anual' (padrão: anual)
    :return: Valor final do investimento
    """
    if capitalizacao == 'mensal':
        taxa_juros_mensal = taxa_juros / 100 / 12
        meses = anos * 12
        valor_final = valor_inicial * (1 + taxa_juros_mensal) ** meses
    elif capitalizacao == 'anual':
        taxa_juros_anual = taxa_juros / 100
        valor_final = valor_inicial * (1 + taxa_juros_anual) ** anos
    else:
        raise ValueError("A capitalização deve ser 'mensal' ou 'anual'")
    
    return valor_final


# Exemplo de uso
valor_inicial = float(input("Digite o valor inicial do investimento: R$ "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): "))
anos = int(input("Digite o período de investimento (em anos): "))
capitalizacao = input("Digite o tipo de capitalização ('mensal' ou 'anual'): ").strip().lower()

valor_final = calcular_rendimento_investimento(valor_inicial, taxa_juros, anos, capitalizacao)

print(f"Após {anos} anos, o valor final do investimento será de R$ {valor_final:.2f}")
