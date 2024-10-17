def calcular_rendimento_investimento(valor_inicial, taxa_juros, anos, capitalizacao='anual', aporte_mensal=0):
    """
    Calcula o rendimento de um investimento com base em juros compostos, com ou sem aportes mensais.
    
    :param valor_inicial: Valor inicial do investimento
    :param taxa_juros: Taxa de juros anual em percentual
    :param anos: Período do investimento em anos
    :param capitalizacao: Tipo de capitalização: 'mensal' ou 'anual' (padrão: anual)
    :param aporte_mensal: Valor de aportes mensais (padrão: 0, sem aportes)
    :return: Valor final do investimento
    """
    if capitalizacao == 'mensal':
        taxa_juros_mensal = taxa_juros / 100 / 12
        meses = anos * 12
        valor_final = valor_inicial * (1 + taxa_juros_mensal) ** meses
        
        # Considerando os aportes mensais
        for mes in range(1, meses + 1):
            valor_final += aporte_mensal * (1 + taxa_juros_mensal) ** (meses - mes)

    elif capitalizacao == 'anual':
        taxa_juros_anual = taxa_juros / 100
        valor_final = valor_inicial * (1 + taxa_juros_anual) ** anos
        
        # Considerando os aportes mensais
        for ano in range(1, anos + 1):
            valor_final += aporte_mensal * 12 * (1 + taxa_juros_anual) ** (anos - ano)

    else:
        raise ValueError("A capitalização deve ser 'mensal' ou 'anual'")
    
    return valor_final


# Exemplo de uso
valor_inicial = float(input("Digite o valor inicial do investimento: R$ "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): "))
anos = int(input("Digite o período de investimento (em anos): "))
capitalizacao = input("Digite o tipo de capitalização ('mensal' ou 'anual'): ").strip().lower()
aporte_mensal = float(input("Digite o valor dos aportes mensais (digite 0 se não houver): R$ "))

valor_final = calcular_rendimento_investimento(valor_inicial, taxa_juros, anos, capitalizacao, aporte_mensal)

print(f"Após {anos} anos, o valor final do investimento será de R$ {valor_final:.2f}")
