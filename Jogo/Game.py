#Algoritmo : Jogo Termo
#Desenvolvido por : Caio, Herik, Felipe, Leonardo e Daniel

##########################################################
# Import
##########################################################

from random import choice
import os
import time

##########################################################
# Classes
##########################################################

class Terminal():

    def entrada(num):
        while True:
            try:
                entrada = int(input('\nDigite o número: '))
                if entrada in range(1,num+1):
                    Terminal.carregando()
                    return entrada
                else:
                    raise Exception
            except:
                Erro.msg_erro("opção inválida")
                return False
    
    def chute():
        chute = str(input("\nDigite uma palavra: ")).strip().upper()
        chute = list(chute)
        return chute
    
    def resultado(lista_resultado):
        print('')
        for i in lista_resultado:
            if i != False:
                print(i)
    
    def nome(parte):
        print('')
        print("\033[44m{:=^50}\033[m".format(parte))
        print('')

    def carregando():
        Terminal.limpar()
        i = 0
        while i < 2:
            Terminal.limpar()
            print("\n\033[1;32m{:^50}\033[m".format('Loading.  '))
            time.sleep(0.5)
            Terminal.limpar()
            print("\n\033[1;32m{:^50}\033[m".format('Loading.. '))
            time.sleep(0.5)
            Terminal.limpar()
            print("\n\033[1;32m{:^50}\033[m".format('Loading...'))
            time.sleep(0.5)
            i += 1
        Terminal.limpar()
    
    def limpar():
        os.system('cls')

    def info(tema,idioma,tentativas,palavra):
        print("\033[33mIdioma:\033[m",'\033[1;4;36m {} \033[m'.format(idioma),' ' * 5,"\033[33mTema:\033[m",'\033[1;4;36m {} \033[m'.format(tema),' ' * 5,"\033[33mTentativas:\033[m",'\033[1;4;36m {} \033[m\n'.format(tentativas))
        print("\033[33mA palavra tem\033[m \033[1;4;36m{}\033[m \033[33mLetras\033[m\n".format(len(palavra)))



class Erro:

    def error():
        print("\n\033[7;31m{:^50}\033[m".format('Erro!'))
        time.sleep(1)
        Terminal.limpar()

    def msg_erro(erro):
        Terminal.limpar()
        if erro == "opção inválida":
            Erro.error()
            print("\n\033[7;31m{:^50}\033[m".format('Digite uma opção válida!'))
        elif erro == "número letras":
            Erro.error()
            print("\n\033[7;31m{:^50}\033[m".format('A palavra NÃO deve exceder o número de letras!'))
        else:
            Erro.error()
        time.sleep(3)
        Terminal.limpar()



class Introducao:

    def intro_game():
        while True:
            Terminal.limpar()
            Terminal.nome(" Termo Game ")
            print("\nSobre o jogo:\n\nO jogo consiste em adivinhar a palavra secreta definida pelo idioma e tema escolhidos pelo jogador!")
            print("\n","="*50,"\n")
            print("\nRegras:\n\n- O jogador deve escrever uma palavra qualquer, de no máximo o limite de letras da palavra secreta (Será informado na tela).\n- Será retornada a palavra inserida pelo jogador com as letras analisadas e coloridas, servindo como dicas de quão perto o jogador está da palavra secreta.\n- O jogador tem no máximo 6 tentativas!  -->  Se não acertar até as tentativas acabarem, então ele perde! se o jogador acertar a palavra secreta antes das tentativas acabarem, então ele ganha!\n")
            print("\n","="*50,"\n")
            print("\nCores:\n\n\033[32mVerde\033[m - significa que a letra está na palavra secreta E na posição certa!\n\033[33mAmarelo\033[m - significa que a letra está na palavra secreta MAS em outra posição!\n\033[30mCinza\033[m - significa que a letra NÃO está na palavra secreta!\n")
            print("\n","="*50,"\n")
            try:
                jogar = str(input("Deseja Jogar? (S/N): ")).upper()
                if jogar == "S":
                    return True
                elif jogar == "N":
                    return False
                else:
                    raise Exception
            except:
                Erro.msg_erro("opção inválida")



class Configuracao:

    def idioma():
        while True:
            Terminal.nome(" Idioma ")
            print('\033[1mIdiomas:\n\nPortuguês - 1\nInglês - 2\033[m\n')
            idioma = Terminal.entrada(2)
            if not idioma:
                continue
            elif idioma == 1:
                Terminal.limpar()
                return "Português"
            else:
                Terminal.limpar()
                return "Inglês"

    

    def tema(idioma):
        while True:
            Terminal.nome(" Tema ")
            print('\033[1mTemas:\n\nAnimais - 1\nAlimentos - 2\nLugares - 3\033[m\n')
            tema = Terminal.entrada(3)
            if not tema:
                continue
            else:
                tema_escolhido = [[],'']
                if idioma == "Português":
                    if tema == 1:
                        arquivo = open('Jogo\\Temas\\portugues\\Animais.txt','r')
                        tema_escolhido[0] = arquivo.read().split()
                        tema_escolhido[1] = "Animais"
                        arquivo.close()
                        Terminal.limpar()
                    elif tema == 2:
                        arquivo = open('Jogo\\Temas\\portugues\\Alimentos.txt','r')
                        tema_escolhido[0] = arquivo.read().split()
                        tema_escolhido[1] = "Alimentos"
                        arquivo.close()
                        Terminal.limpar()
                    else:
                        arquivo = open('Jogo\\Temas\\portugues\\Lugares.txt','r')
                        tema_escolhido[0] = arquivo.read().split()
                        tema_escolhido[1] = "Lugares"
                        arquivo.close()
                        Terminal.limpar()
                else:
                    if tema == 1:
                        arquivo = open('Jogo\\Temas\\ingles\\Animais.txt','r')
                        tema_escolhido[0] = arquivo.read().split()
                        tema_escolhido[1] = "Animais"
                        arquivo.close()
                        Terminal.limpar()
                    elif tema == 2:
                        arquivo = open('Jogo\\Temas\\ingles\\Alimentos.txt','r')
                        tema_escolhido[0] = arquivo.read().split()
                        tema_escolhido[1] = "Alimentos"
                        arquivo.close()
                        Terminal.limpar()
                    else:
                        arquivo = open('Jogo\\Temas\\ingles\\Lugares.txt','r')
                        tema_escolhido[0] = arquivo.read().split()
                        tema_escolhido[1] = "Lugares"
                        arquivo.close()
                        Terminal.limpar()
                return tema_escolhido



class Jogo:

    def palavra(tema):
        palavra = choice(tema).upper()
        palavra = list(palavra)
        return palavra
    


    def verificar(chute,palavra):
        # Criando uma lista para guardar as letras coloridas verificadas.       
        lista_resultado = []
        try:
            # loop for para adicionar '*' na lista 'vazia' criada, e deixar a lista com o mesmo tamanho que o chute do usário, para posteriormente ser feita as substituições dos '*' pelas letras coloridas verificadas, pelo index.
            for i in chute:
                lista_resultado.append('*')
            # Loop for para verificar e comparar as letras do chute com os da palavra_secreta(sorteada), usando o index.
            for i in range(0,len(chute)):
                # Se a letra na posição [i] do chute estiver na palavra E estiver na posição certa em relação a palavra_seecreta, entao colorimos ela de verde.
                if chute[i] == palavra[i]:
                    # substituindo os '*' na posição [i] da lista_resultado pelas letras já coloridas.
                    lista_resultado[i] = "\033[32m{}\033[m".format(chute[i])
                # Se a letra na posição [i] do chute estiver na palavra MAS NÃO estiver na posição certa em relação a palavra_seecreta, entao colorimos ela de amarelo.
                if chute[i] != palavra[i] and chute[i] in palavra:
                    # substituindo os '*' na posição [i] da lista_resultado pelas letras já coloridas.
                    lista_resultado[i] = "\033[33m{}\033[m".format(chute[i])
                # Se a letra na posição [i] do chute NÃO estiver na palavra, entao colorimos ela de cinza.
                if chute[i] != palavra[i] and chute[i] not in palavra:
                    # substituindo os '*' na posição [i] da lista_resultado pelas letras já coloridas.
                    lista_resultado[i] = "\033[2;49;90m{}\033[m".format(chute[i])
                # Transformando a lista_resultado com as letras já coloridas e verificadas, em uma string para mostrar na tela.        
                resultado = ''.join(lista_resultado)
            # retornando a variável strig com as letras já coloridas e verificadas para posteriormente printar na tela.
            return resultado
        except:
            Erro.msg_erro("número letras")
            return False


    
    def status(tentativas,palavra,chute):
        a = ''.join(palavra)
        if tentativas >= 7:
            Terminal.limpar()
            print("\n\033[31mVocê Perdeu!\033[m\n")
            print("\033[33mA palavra era:\033[33m",'\033[1;4;36m {} \033[m\n'.format(a))
            time.sleep(3)
            return True
        elif chute == palavra:
            Terminal.limpar()
            print("\n\033[32mVocê acertou!\033[m\n")
            print("\033[33mA palavra era:\033[33m",'\033[1;4;36m {} \033[m\n'.format(a))
            time.sleep(3)
            return True
        else:
            return False



    def novamente():
        while True:
            try:
                Terminal.limpar()
                jogar = str(input("Deseja jogar novamente (S/N): ")).strip().upper()
                if jogar == "S":
                    Start()
                elif jogar == "N":
                    return False
                else:
                    raise Exception
            except:
                Erro.msg_erro("opção inválida")



    def jogar(tema,idioma):
        palavra = Jogo.palavra(tema[0])
        tentativas = 0
        lista_resultado = []
        Terminal.limpar()
        while True:
            Terminal.nome(" Termo Game ")
            Terminal.info(tema[1],idioma,tentativas,palavra)
            if len(lista_resultado) > 0:
                Terminal.resultado(lista_resultado)
            chute = Terminal.chute()
            resultado = Jogo.verificar(chute,palavra)
            lista_resultado.append(resultado)
            if not resultado:
                continue
            else:    
                tentativas += 1
            status = Jogo.status(tentativas,palavra,chute)
            if status:
                novamente = Jogo.novamente()
                if not novamente:
                    Terminal.carregando()
                    print("\033[33m{:^50}\033[m".format("Tenha um bom dia!"))
                    time.sleep(2)
                    Terminal.limpar()
                    break
            Terminal.limpar()   



class Start:

    def __init__(self):
        jogar = Introducao.intro_game()
        if jogar:
            Terminal.carregando()
            idioma = Configuracao.idioma()
            tema = Configuracao.tema(idioma)
            Jogo.jogar(tema,idioma)
        else:
            Terminal.carregando()
            print("\033[33m{:^50}\033[m".format("Tenha um bom dia!"))
            time.sleep(2)
            Terminal.limpar()



##########################################################
# Jogo
##########################################################

Start()