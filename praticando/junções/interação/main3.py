# ==========================================
# 2. FUNÇÃO E CONDICIONAIS
# ==========================================
def adicionar_movimentacao(tipo, descricao, valor):
    global saldo_atual  # Permite alterar a variável que criamos lá no topo
    
    # Condicional para validar se o valor é positivo
    if valor <= 0:
        print("❌ Erro: O valor deve ser maior que zero!")
        return

    # Condicional para decidir o cálculo baseado no tipo de transação
    if tipo == "Receita":
        saldo_atual += valor
    elif tipo == "Despesa":
        if valor > saldo_atual:
            print("⚠️ Alerta: Esta despesa vai deixar seu saldo negativo!")
        saldo_atual -= valor

    # Criando uma estrutura de dicionário para agrupar os dados
    transacao = {
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor
    }
    
    # Adicionando o dicionário dentro da nossa lista histórica
    historico_transacoes.append(transacao)
    print(f"✅ {tipo} de R$ {valor:.2f} registrada com sucesso!")