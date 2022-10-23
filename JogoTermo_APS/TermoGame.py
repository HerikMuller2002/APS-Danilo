from classeidioma import Idiomas
from random import choice
#Algoritmo : Jogo Termo
#Data : 18/10/2022
#Desenvolvido por : Caio e amigos

# Escolhendo o idioma
while True:
    print('Idiomas:\n\nPortuguês - 1\nInglês - 2\n')
    idioma = str(input('Digite o número referente a língua: '))
    lista_resposta = ['1','2']
    if idioma not in lista_resposta:
        print('\nDigite um número válido!\n')
        continue
    else:
        idioma_escolhido = Idiomas.lingua(idioma)
        print('\n',idioma_escolhido,'\n')
        break

# Definindo tema
while True:
    try:
        print('\nTema 1 - 1\nTema 2 - 2\nTema 3 - 3\n')
        tema = int(input('Digite o número do tema: '))
        if tema > 3 or tema < 1:
            print('Erro!\nDigite um número de 1 a 3!')
            continue
        else:
            tema_escolhido = open('Temas/BancoPalavras.txt', 'r').read().split()
            break
    except Exception:
        print('Erro!\nDigite um número de 1 a 3!')

# Predefinindo o jogo
while True:
    try:
        quant_palavras = int(input('Qual será a quantidade de palavras?(1 - 4): '))
        if quant_palavras > 4 or quant_palavras < 1:
            print('Erro!\nDigite um número de 1 a 4!')
            continue
        else:
            break
    except Exception:
        print('Erro!\nDigite um número de 1 a 4!')

#Processamento do jogo
palavra_sorteada = choice(tema_escolhido).split()
palavra_secreta = []
for i in palavra_sorteada:
    palavra_secreta.append('_')