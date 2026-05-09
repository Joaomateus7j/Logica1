alunos = [("Ana", 8.5), ("Bruno", 4.2), ("Carla", 7.0), ("Diego", 3.8), ("Eva", 9.1)]
aprovados = 0

for nome, nota in alunos:
    if nota >= 5:
        print(f"✅ {nome} aprovado(a) com {nota}")
        aprovados += 1
    else:
        print(f"❌ {nome} reprovado(a) com {nota}")

print(f"\nTotal de aprovados: {aprovados}/{len(alunos)}")