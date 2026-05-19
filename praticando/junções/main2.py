texto = input('Digite uma palavra: ')

vogais = 0

for letra in texto:

    if letra in 'aeiou':
        vogais += 1

print(f'Total de vogais: {vogais}')