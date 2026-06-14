# Programa que armazena números em uma lista e faz análises

numeros = []

while True:
    valor = int(input("Digite um número (0 para parar): "))

    if valor == 0:
        break

    numeros.append(valor)  # adiciona na lista

print("\n📊 Resultados:")

print(f"Lista de números: {numeros}")
print(f"Quantidade: {len(numeros)}")
print(f"Soma: {sum(numeros)}")

if numeros:  # evita erro se a lista estiver vazia
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
    print(f"Média: {sum(numeros) / len(numeros):.2f}")
else:
    print("Nenhum número foi digitado.")

    idadei1 = 12