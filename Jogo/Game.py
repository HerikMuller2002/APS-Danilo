#Algoritmo : Jogo Termo
#Desenvolvido por : Caio, Herik, Felipe, Leonardo e Daniel

##########################################################
# Import Bibliotecas
##########################################################

# método choice para escolher 'aleatóriamente' uma palavra dentro da lista tema.
from random import choice
# biblioteca 'os' para limpar o terminal.
import os
# biblioteca 'time' para congelar a tela por alguns segundos.
import time

##########################################################
# Classe Terminal
##########################################################

# classe com funções que imprimem mensagens no terminal.
class Terminal():

#=========================================================
    # função para limpar a tela do terminal
    def limpar():
        os.system('cls')

#=========================================================
    # função para imprimir o nome da parte do jogo (tema,idioma...).
    def nome(parte):
        print('')
        # usamos o Place Holder '.format' para printar na string o nome da seção do jogo armazenado na variável 'parte', além disso, centralizamos o nome em um espaço de 50 caracteres e entre vários '=', para fins estéticos.
        print("\033[44m{:=^50}\033[m".format(parte))
        print('')

#=========================================================
    # função para mostrar a tela de carregando.
    def carregando():
        # criando uma variável para repetir o loop
        i = 0
        # loop para mostrar a menssagem 'carregando' várias vezes com diferentes números de '.', para dar a sensação de animação.
        while i < 2:
            # chamando a função para limpar a tela.
            Terminal.limpar()
            # mostrando a mensagem 'carregando' com 1 '.'
            print("\n\033[1;32m{:^50}\033[m".format('Loading.  '))
            # método sleep para a tela congelar por 0,5 segundos.
            time.sleep(0.5)
            # chamando a função para limpar a tela.
            Terminal.limpar()
            # mostrando a mensagem 'carregando' com 2 '.'
            print("\n\033[1;32m{:^50}\033[m".format('Loading.. '))
            # método sleep para a tela congelar por 0,5 segundos.
            time.sleep(0.5)
            # chamando a função para limpar a tela.
            Terminal.limpar()
            # mostrando a mensagem 'carregando' com 3 '.'
            print("\n\033[1;32m{:^50}\033[m".format('Loading...'))
            # método sleep para a tela congelar por 0,5 segundos.
            time.sleep(0.5)
            # somando mais 1 na variável para parar o loop na 2ª vez.
            i += 1
        # limpando o que sobrou dos prints.
        Terminal.limpar()

#=========================================================            
    # função para mostrar as informações selecionadas para orientar o jogador na hora do chute.
    def info(tema,idioma,tentativas,palavra):
        # mostrando idioma selecionado, tema selecionado, tentativas de chute, quantidade de letras.
        print("\033[33mIdioma:\033[m",'\033[1;4;36m {} \033[m'.format(idioma),' ' * 5,"\033[33mTema:\033[m",'\033[1;4;36m {} \033[m'.format(tema),' ' * 5,"\033[33mTentativas:\033[m",'\033[1;4;36m {} \033[m\n'.format(tentativas))
        print("\033[33mA palavra tem\033[m \033[1;4;36m{}\033[m \033[33mLetras\033[m\n".format(len(palavra)))

#=========================================================
    # função para pedir o input do número das opções (tema/idioma).
    def entrada(num):
        # o sistema deve tentar executar estes comandos.
        try:
            # input em -> inteiro
            entrada = int(input('\nDigite o número: '))
            # verificando se o input está no range permitido.
            if entrada in range(1,num+1):
                # caso o input esteja correto, chamamos a função 'carregando' para dar a sensação de continuidade do programa.
                Terminal.carregando()
                # retornando o input do usuário.
                return entrada
            # se o input não estiver dentro do range, então criamos uma excessão/'erro'
            else:
                raise Exception
        # caso o programa encontre um erro/excessão: 
        except:
            # chamamos a função msg_erro.
            Erro.msg_erro("opção inválida")
            # retornando False.
            return False

#=========================================================
    # função para input do chute do usuário.
    def chute():
        # input com o método '.strip()' para retirar possíveis espaços antes e depois da palavra, além do método '.upper()' para tornar todas as letras em maiúsculas, afim de criar um padrão e evitar problemas com a verificação das letras.
        chute = str(input("\nDigite uma palavra: ")).strip().upper()
        # transformando as letras do input em lista. 
        chute = list(chute)
        # retornando o chute já em lista.
        return chute

#=========================================================
    # função para mostrar o resultado da verificação das letras.
    def resultado(lista_resultado):
        print('')
        # print de todos os elemento da lista dos resultados dos chutes.
        for i in lista_resultado:
            print(i)
    
##########################################################
# Classe Erro
##########################################################

# classe de menssagens de erro.
class Erro:

#=========================================================
    # função para mostrar uma menssagem de erro padrão.
    def error():
        # print
        print("\n\033[7;31m{:^50}\033[m".format('Erro!'))
        # congelando a tela com a menssagem por 1 segundo.
        time.sleep(1)
        # limpando a menssagem de erro da tela.
        Terminal.limpar()

#=========================================================
    # função para imprimir uma menssagem de erro específica, para mostrar ao usuário o que há de errado.
    def msg_erro(erro):
        # limpando o terminal
        Terminal.limpar()
        # verificando o tipo de erro.
        if erro == "opção inválida":
            # chamando a função 'erro' para imprimir uma menssagem genérica antes.
            Erro.error()
            # mostrando a menssagem de erro específica.
            print("\n\033[7;31m{:^50}\033[m".format('Digite uma opção válida!'))
        # verificando o tipo de erro.
        elif erro == "número letras":
            # chamando a função 'erro' para imprimir uma menssagem genérica antes.
            Erro.error()
            # mostrando a menssagem de erro específica.
            print("\n\033[7;31m{:^50}\033[m".format('A palavra NÃO deve exceder o número de letras!'))
        else:
            # se não for identificado um erro específico, então chamamos apenas a função de 'erro' padrão.
            Erro.error()
        # independente da menssagem mostrada, congelamos a tela por 3 segundos, para dar tempo do usuário ler.
        time.sleep(3)
        # limpamos a menssagem da tela.
        Terminal.limpar()

##########################################################
# Classe Configuração
##########################################################

# classe com funções para predefinição do jogo.
class Configuracao:

#=========================================================
    # função para definir o idioma
    def idioma():
        # loop para mostrar as opções e pedir o input
        while True:
            # chamando a função 'nome' para fins estéticos e para informar ao usuário qual parte do jogo ele está.
            Terminal.nome(" Idioma ")
            # mostrando as opções na tela.
            print('\033[1mIdiomas:\n\nPortuguês - 1\nInglês - 2\033[m\n')
            # chamando a função 'entrada' e armazenando o input do usuário.
            idioma = Terminal.entrada(2)
            # verificando se o input é válido.
            if not idioma:
                # se não for, continuamos o loop e pedimos o input novamente.
                continue
            # caso o input for aceito, verificamos qual foi a opção escolhida pelo o usuário.
            else:
                # se o usuário escolheu a opção 1:
                if idioma == 1:
                    # limpamos o terminal
                    Terminal.limpar()
                    # e retornamos o idioma 'português'.
                    return "Português"
                # se o idioma foi aceito pelo programa e não foi 1, então a opção escolhida foi 2.    
                else:
                    # limpamos o terminal
                    Terminal.limpar()
                    # e retornamos o idioma 'inglês'.
                    return "Inglês"

#=========================================================
    # função para definir o tema
    def tema(idioma):
        # loop para mostrar as opções e pedir o input
        while True:
            # chamando a função 'nome' para fins estéticos e para informar ao usuário qual parte do jogo ele está.
            Terminal.nome(" Tema ")
             # mostrando as opções na tela.
            print('\033[1mTemas:\n\nAnimais - 1\nAlimentos - 2\nLugares - 3\033[m\n')
            # chamando a função 'entrada' e armazenando o input do usuário.
            tema = Terminal.entrada(3)
            # verificando se o input é válido.
            if not tema:
                # se não for... continuamos o loop e pedimos o input novamente.
                continue
            # caso o input for aceito, verificamos qual foi a opção escolhida pelo o usuário.
            else:
                # criamos uma variável para armazenar no index[0] -> a lista com as palavras do tema escolhido, para ser sorteado uma delas posteriormente. No index[1] -> o nome do tema, para ser mostrado posteriormente.
                tema_escolhido = [[],'']
                # primeiro, verificamos qual idioma o usuário escolheu, para que seja retirado o tema dentro do idioma certo.
                if idioma == "Português":
                    # verificamos o tema escolhido.
                    if tema == 1:
                        # abrindo o arquivo txt do tema escolhido, dentro da pasta temas.
                        arquivo = open('Jogo\\Temas\\portugues\\Animais.txt','r')
                        # abrindo em modo leitura e criando uma lista com as palavras do arquivo txt.
                        tema_escolhido[0] = arquivo.read().split()
                        # definindo o index[1] com o nome do tema para que seja mostrado posteriormente. 
                        tema_escolhido[1] = "Animais"
                        # depois de usar, fechamos o arquivo para evitar problemas.
                        arquivo.close()
                        # limpando o terminal.
                        Terminal.limpar()
                    # verificamos o tema escolhido.
                    elif tema == 2:
                        # abrindo o arquivo txt do tema escolhido, dentro da pasta temas.
                        arquivo = open('Jogo\\Temas\\portugues\\Alimentos.txt','r')
                        # abrindo em modo leitura e criando uma lista com as palavras do arquivo txt.
                        tema_escolhido[0] = arquivo.read().split()
                        # definindo o index[1] com o nome do tema para que seja mostrado posteriormente. 
                        tema_escolhido[1] = "Alimentos"
                        # depois de usar, fechamos o arquivo para evitar problemas.
                        arquivo.close()
                        # limpando o terminal.
                        Terminal.limpar()
                    # verificamos o tema escolhido.
                    else:
                        # abrindo o arquivo txt do tema escolhido, dentro da pasta temas.
                        arquivo = open('Jogo\\Temas\\portugues\\Lugares.txt','r')
                        # abrindo em modo leitura e criando uma lista com as palavras do arquivo txt.
                        tema_escolhido[0] = arquivo.read().split()
                        # definindo o index[1] com o nome do tema para que seja mostrado posteriormente. 
                        tema_escolhido[1] = "Lugares"
                        # depois de usar, fechamos o arquivo para evitar problemas.
                        arquivo.close()
                        # limpando o terminal.
                        Terminal.limpar()
                # se o idioma foi inglês:
                else:
                    # verificamos o tema escolhido.
                    if tema == 1:
                        # abrindo o arquivo txt do tema escolhido, dentro da pasta temas.
                        arquivo = open('Jogo\\Temas\\ingles\\Animais.txt','r')
                        # abrindo em modo leitura e criando uma lista com as palavras do arquivo txt.
                        tema_escolhido[0] = arquivo.read().split()
                        # definindo o index[1] com o nome do tema para que seja mostrado posteriormente. 
                        tema_escolhido[1] = "Animais"
                        # depois de usar, fechamos o arquivo para evitar problemas.
                        arquivo.close()
                        # limpando o terminal.
                        Terminal.limpar()
                    # verificamos o tema escolhido  .  
                    elif tema == 2:
                        # abrindo o arquivo txt do tema escolhido, dentro da pasta temas.
                        arquivo = open('Jogo\\Temas\\ingles\\Alimentos.txt','r')
                        # abrindo em modo leitura e criando uma lista com as palavras do arquivo txt.
                        tema_escolhido[0] = arquivo.read().split()
                        # definindo o index[1] com o nome do tema para que seja mostrado posteriormente.
                        tema_escolhido[1] = "Alimentos"
                        # depois de usar, fechamos o arquivo para evitar problemas.
                        arquivo.close()
                        # limpando o terminal.
                        Terminal.limpar()
                    # verificamos o tema escolhido.
                    else:
                        # abrindo o arquivo txt do tema escolhido, dentro da pasta temas.
                        arquivo = open('Jogo\\Temas\\ingles\\Lugares.txt','r')
                        # abrindo em modo leitura e criando uma lista com as palavras do arquivo txt.
                        tema_escolhido[0] = arquivo.read().split()
                        # definindo o index[1] com o nome do tema para que seja mostrado posteriormente.
                        tema_escolhido[1] = "Lugares"
                        # depois de usar, fechamos o arquivo para evitar problemas.
                        arquivo.close()
                        # limpando o terminal.
                        Terminal.limpar()
                # retornando a lista criada com as palavras e com o nome do tema.
                return tema_escolhido

##########################################################
# Classe Jogo
##########################################################

# classe para o funcionamento do jogo
class Jogo:

#=========================================================
    # função para mostrar a introdução/regras do jogo.
    def intro_game():
        # loop para perguntar ao usuário se ele deseja jogar.
        while True:
            # limpando o terminal.
            Terminal.limpar()
            # chamando a função 'nome' para fins estéticos e para informar ao usuário qual parte do jogo ele está.
            Terminal.nome(" Termo Game ")
            # imprimindo as regras do jogo.
            print("\nSobre o jogo:\n\nO jogo consiste em adivinhar a palavra secreta definida pelo idioma e tema escolhidos pelo jogador!")
            print("\n","="*50,"\n")
            print("\nRegras:\n\n- O jogador deve escrever uma palavra qualquer, de no máximo o limite de letras da palavra secreta (Será informado na tela).\n- Será retornada a palavra inserida pelo jogador com as letras analisadas e coloridas, servindo como dicas de quão perto o jogador está da palavra secreta.\n- O jogador tem no máximo 6 tentativas!  -->  Se não acertar até as tentativas acabarem, então ele perde! se o jogador acertar a palavra secreta antes das tentativas acabarem, então ele ganha!\n")
            print("\n","="*50,"\n")
            print("\nCores:\n\n\033[32mVerde\033[m - significa que a letra está na palavra secreta E na posição certa!\n\033[33mAmarelo\033[m - significa que a letra está na palavra secreta MAS em outra posição!\n\033[30mCinza\033[m - significa que a letra NÃO está na palavra secreta!\n")
            print("\n","="*50,"\n")
            # try e except para pedir o input do usuário - (se ele quer jogar ou não).
            try:
                # input
                jogar = str(input("Deseja Jogar? (S/N): ")).upper()
                # se o input for 's'/'S' !!(não faz diferença qual 's' o usuário digite pois no input possui o método 'upper()' que torna maiúsculo qualquer letra)!!
                if jogar == "S":
                    # retorna verdadeiro e da continuidade no programa.
                    return True
                # se o input for 'n'/'N':
                elif jogar == "N":
                    # retorna falso e encerra o programa.
                    return False
                # se o input não for nenhumas das alternativas esperadas:
                else:
                    # criamos uma exceção/erro
                    raise Exception
            # se haver alguma exceção:
            except:
                # chamamos a função 'erro' e imprimimos uma menssagem de erro na tela.
                Erro.msg_erro("opção inválida")
                # continuamos o loop para pedir o input novamente.
                continue

#=========================================================
    # função para escolher uma palavra aleatória do tema
    def palavra(tema):
        # usamos o método 'choice' para escolher um elemento/palavra aleatório de uma lista(tema), usamos também o método '.upper()' para deixar todas as letras em um padrão maiúsculo.
        palavra = choice(tema).upper()
        # criamos uma lista com as letras da palavra 'sorteada'.
        palavra = list(palavra)
        # retornamos a lista com as letras.
        return palavra
    
#=========================================================
    def verificar(chute,palavra):
        # Criando uma lista para guardar as letras coloridas verificadas.       
        lista_resultado = []
        # try e except para caso algum erro apareça.
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
        # se um erro/exceção acontecer:
        except:
            # chamamos a função 'msg_erro'.
            Erro.msg_erro("número letras")
            # retornamos falso para que não seja printado na tela a variável resultado com erro.
            return False

#=========================================================
    # função para verificar se o jogador ganhou ou perdeu.
    def status(tentativas,palavra,chute):
        # transformando a palavra 'secreta'que está em lista em stringdenovo para que seja mostrada na tela.
        a = ''.join(palavra)
        # Verificando se o jogador perdeu pelo número de tentativas.
        if tentativas >= 7:
            # limpando o terminal.
            Terminal.limpar()
            # print perdeu
            print("\n\033[31mVocê Perdeu!\033[m\n")
            # mostrando a palavra certa.
            print("\033[33mA palavra era:\033[33m",'\033[1;4;36m {} \033[m\n'.format(a))
            # congelando pro 3 segundos os prints.
            time.sleep(3)
            # retornando True para que o programa seja finalizado.
            return True
        # Verificando se o jogador ganhou.
        elif chute == palavra:
            # limpando o terminal.
            Terminal.limpar()
            # print acertou
            print("\n\033[32mVocê acertou!\033[m\n")
            # mostrando a palavra para o usuário ter certeza.
            print("\033[33mA palavra era:\033[33m",'\033[1;4;36m {} \033[m\n'.format(a))
            # congelando pro 3 segundos os prints.
            time.sleep(3)
            # retornando verdadeiro para que o programa seja finalizado.
            return True
        else:
            # caso o usuário não ganhou nem perdeu, retorna Falso para que o programa continue rodando. 
            return False

#=========================================================
    # Função para o usuário decidir se quer jogar novamente, sem a nescessidade de sair do terminal e executar o programa novamente.
    def novamente():
        # loop para o input da resposta.
        while True:
            # try e except para caso algum erro apareça.
            try:
                # limpando o terminal.
                Terminal.limpar()
                # input da resposta do usuário.
                jogar = str(input("Deseja jogar novamente (S/N): ")).strip().upper()
                # se a resposta fo 'sim':
                if jogar == "S":
                    # chamamos a classe start novamente para que o jogo recomece.
                    Start()
                # se a resposta for 'não', paramos o programa.
                elif jogar == "N":
                    return False
                # se o input não for nenhumas das alternativas esperadas:
                else:
                    # criamos uma exceção.
                    raise Exception
            # se um erro/exceção acontecer:
            except:
                # chamamos a função 'msg_erro'.
                Erro.msg_erro("opção inválida")
                # continuamos o loop do input.
                continue

#=========================================================
    # função para o usuário começar a jogar e dar seus 'chutes'.
    def jogar(tema,idioma):
        # chamando a função 'palavra' para sortear uma plavra aleatória do idioma e tema escolhido, e armazenando-a na variável -> palavra.
        palavra = Jogo.palavra(tema[0])
        # definindo as tentativas no início como 0.
        tentativas = 0
        # criando uma lista para armazenar todas as verificações dos chutes já dados, para mostrar na tela a verificação dos chutes anteriores também.
        lista_resultado = []
        # limpando o terminal.
        Terminal.limpar()
        # loop para os inputs dos chutes.
        while True:
            # chamando a função 'nome' para fins estéticos e para informar ao usuário qual parte do jogo ele está.
            Terminal.nome(" Termo Game ")
            # chamando a função 'info' para mostrar as informações importantes na tela, para o usuário basear seu chute.
            Terminal.info(tema[1],idioma,tentativas,palavra)
            # verificando o tamanho da lista dos resultados dos chutes, caso a lista estiver vazia, significa que é o 1º chute do usuário, e não deverá mostrar nada desta lista na tela.
            if len(lista_resultado) > 0:
                # se não, chamamos a função 'resultado' para mostrar os resultados anteriores na tela.
                Terminal.resultado(lista_resultado)
            # input do chute.
            chute = Terminal.chute()
            # chamando a função 'verificar' e armazenando o resultado da verificação das letras na variável -> resultado.
            resultado = Jogo.verificar(chute,palavra)
            # caso a verificação tenha dado erro/exceção, será retornado falso. Caso tenha sido retornado falso descartamos essa verificação.
            if not resultado:
                # continuamos o loop e pedimos o input novamente.
                continue
            # se a verificação deu certo continuamos o programa:
            else:    
                # guardamos a variável resultado na lista criada, para que esse resultado seja guardado e mostrado na tela nos outros chutes também.
                lista_resultado.append(resultado)
                # aumentamos uma tentativa.
                tentativas += 1
            # chamando a função 'status' para verificar se o jogador ganhou/perdeu ou se o jogo deve continuar.
            status = Jogo.status(tentativas,palavra,chute)
            # se o retorno do status dor verdadeiro o programa acaba. 
            if status:
                # chamamos a função 'novamente' para perguntar ao jogador se ele quer jogar denovo.
                novamente = Jogo.novamente()
                # se o usuário não quiser jogar novamente:
                if not novamente:
                    # mostramos a tela de loading
                    Terminal.carregando()
                    # print de menssagem 'tenha um bom dia!'
                    print("\033[33m{:^50}\033[m".format("Tenha um bom dia!"))
                    # congelando a menssagem por 2 segundos na tela.
                    time.sleep(2)
                    #limpando o terminal.
                    Terminal.limpar()
                    # parando o loop e encerrando o programa.
                    break
            # limpando o terminal.
            Terminal.limpar()   

##########################################################
# Classe Start
##########################################################

# classe para iniciar o jogo.
class Start:

#=========================================================
    # função auto executavel para chamar as funções do jogo.
    def __init__(self):
        # 1º chamando a função da introdução.
        jogar = Jogo.intro_game()
        # verificamos se o usuário quer jogar ou não:
        # se a resposta foi sim, chamamos as funções para o jogo rodar.
        if jogar:
            # mostramos a tela de loading para dar uma 'imersão'.
            Terminal.carregando()
            # chamamos a função idioma. 
            idioma = Configuracao.idioma()
            # chamamos a função tema. 
            tema = Configuracao.tema(idioma)
            # e por fim a função 'jogar' para pedir o input do chute e fazer as verificações.
            Jogo.jogar(tema,idioma)
        # se a resposta foi não encerramos o programa.
        else:
            # mostramos a tela de loading para dar uma 'imersão'.
            Terminal.carregando()
            # print de menssagem 'tenha um bom dia!' 
            print("\033[33m{:^50}\033[m".format("Tenha um bom dia!"))
             # congelando a menssagem por 2 segundos na tela.
            time.sleep(2)
            # limpando terminal.
            Terminal.limpar()

##########################################################
# Iniciar o jogo
##########################################################

# chamando a classe 'Start' para iniciar o jogo.
Start()