# ==========================================
# 3. FUNÇÃO E LOOP FOR
# ==========================================
def exibir_extrato():
    print("\n--- EXTRATO DETALHADO ---")
    
    # Condicional para verificar se a lista está vazia
    if not historico_transacoes:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        # Loop FOR que percorre cada dicionário dentro da lista histórica
        for i, item in enumerate(historico_transacoes, start=1):
            simbolo = "➕" if item["tipo"] == "Receita" else "➖"
            print(f"{i}. {simbolo} {item['descricao']}: R$ {item['valor']:.2f}")
            
    print(f"\nSaldo Atual Corrente: R$ {saldo_atual:.2f}")
    print("-" * 25)