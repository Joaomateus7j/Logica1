# Sistema de Recomendações de Filmes.

nome = input('Poderia dizer o seu nome? ')
genero_de_filme = input('Qual o gênero de filme favorito seu entre (Ação, Comedia, Drama):' ).lower()

if genero_de_filme == 'ação':
    print(f"{nome}, eu recomendo assistir 'John Wick'!")
elif genero_de_filme == 'comédia':
    print(f"{nome}, você vai rir muito com 'Gente Grande'!")
elif genero_de_filme == 'drama':
    print(f"{nome}, um ótimo drama é 'Oppenheimer'!")
else:
    print(f"Poxa {nome}, não conheço esse gênero ainda.")