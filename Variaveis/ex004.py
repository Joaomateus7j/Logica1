pessoa1 = input('Qual e o seu nome?')
pessoa1_idade = int(input('Qual e sua idade?'))
pessoa2 = input('Qual e o seu nome?')
pessoa2_idade = int(input('Qual e sua idade?'))

idade = pessoa1_idade + pessoa2_idade
media = idade / 2
print(f'A soma da idades de {pessoa1} e {pessoa2} e de {idade} anos')
print(f'A media de idade entre eles é de {media}')
