#Algoritmo : Jogo Termo
#Data : 18/10/2022
#Desenvolvido por : Caio e amigos

# Import
from classeidioma import Idiomas
import random

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
        print('\n',idioma_escolhido)
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
        quant_palavras = int(input('\nQual será a quantidade de palavras?(1 - 4): '))
        if quant_palavras > 4 or quant_palavras < 1:
            print('Erro!\nDigite um número de 1 a 4!')
            continue
        else:
            break
    except Exception:
        print('Erro!\nDigite um número de 1 a 4!')

#Processamento do jogo
palavra_secreta = random.choice(tema_escolhido)
palavra_secreta = list(palavra_secreta)

chute = str(input("\nDigite uma palavra: "))
chute = list(chute)
lista_resultado = chute

for i in range(0,len(chute)):
    if chute[i] == palavra_secreta[i]:
        lista_resultado[i] = "\033[32m{}\033[m".format(chute[i])
    if chute[i] != palavra_secreta[i] and chute[i] in palavra_secreta:
        lista_resultado[i] = "\033[33m{}\033[m".format(chute[i])
    if chute[i] != palavra_secreta[i] and chute[i] not in palavra_secreta:
        lista_resultado[i] = "\033[1m{}\033[m".format(chute[i])

resultado = ''.join(lista_resultado)
print(resultado,'\n')
print(palavra_secreta)    