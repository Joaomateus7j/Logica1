# ========================================
# CÓDIGO 2 - APROVAR OU REPROVAR ALUNO
# ========================================
print("=" * 50)
print("CÓDIGO 2 - RESULTADO DO ALUNO")
print("=" * 50)

aluno = "Maria"
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"Aluno: {aluno}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média final: {media:.2f}")

if media >= 7:
    print(f"✓ {aluno} foi APROVADO!")
elif media >= 5:
    print(f"⚠️ {aluno} está em RECUPERAÇÃO!")
else:
    print(f"✗ {aluno} foi REPROVADO!")

print()