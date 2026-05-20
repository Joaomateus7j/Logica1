# ==========================================
# 4. LOOP PRINCIPAL (WHILE) E MENU
# ==========================================
while True:
    print("\n=== SISTEMA FINANCEIRO INTERMEDIÁRIO ===")
    print("1. Adicionar Receita (Entrada)")
    print("2. Adicionar Despesa (Saída)")
    print("3. Ver Extrato e Saldo")
    print("4. Sair do Programa")
    
    opcao = input("Escolha uma opção (1-4): ").strip()

    # Condicionais para direcionar a escolha do usuário para a função correta
    if opcao == "1":
        desc = input("Digite a descrição da receita: ").strip()
        val = float(input("Digite o valor da receita (R$): "))
        adicionar_movimentacao("Receita", desc, val)  # Chama a função
        
    elif opcao == "2":
        desc = input("Digite a descrição da despesa: ").strip()
        val = float(input("Digite o valor da despesa (R$): "))
        adicionar_movimentacao("Despesa", desc, val)  # Chama a função
        
    elif opcao == "3":
        exibir_extrato()  # Chama a função
        
    elif opcao == "4":
        print("Encerrando o sistema financeiro. Bons estudos de lógica!")
        break  # Quebra o loop while e finaliza o programa
        
    else:
        print("❌ Opção inválida. Tente novamente.")