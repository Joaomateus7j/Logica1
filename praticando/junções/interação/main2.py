# ==========================================
# 1. VARIÁVEIS E COLEÇÕES (Armazenamento)
# ==========================================
# Variáveis simples e uma lista de dicionários para guardar as transações
saldo_atual = 0.0
historico_transacoes = []  # Coleção que armazenará cada movimentação

# ==========================================
# 4. FUNÇÕES (Modularização da Lógica)
# ==========================================
def adicionar_movimentacao(tipo, descricao, valor):
    """
    Recebe os dados, atualiza o saldo global e guarda no histórico.
    Usa a palavra-chave 'global' para modificar as variáveis de fora da função.
    """
    global saldo_atual
    
    # Validação lógica simples
    if valor <= 0:
        print("❌ Erro: O valor deve ser maior que zero!")
        return