from random import randint
from colorama import Fore, Style
from operator import attrgetter
import os
import time


class No:

    def __init__(self, cor):
        self.cor = cor
        self.prox = None


class Jogador:
    nome = ''
    pontuacao = 0


class Genius:

    def __init__(self):
        self.primeiro = None

    def gerarCor(self):
        nodo = No(randint(1, 4))
        if self.primeiro == None:  # se a lista eh vazia, o processo eh o mesmo de inserir no inicio
            self.primeiro = nodo
        else:
            atual = self.primeiro
            while atual.prox != None:  # senao, percorre-se a lista ate chegar ao final
                atual = atual.prox  # e fazemos o ultimo elemento apontar para nodo em vez de para Null
            atual.prox = nodo

    def mostraSequencia(self, dificuldade):
        os.system('cls')
        atual = self.primeiro
        while atual != None:
            if atual.cor == 1:
                corTexto = Fore.RED
            elif atual.cor == 2:
                corTexto = Fore.GREEN
            elif atual.cor == 3:
                corTexto = Fore.BLUE
            elif atual.cor == 4:
                corTexto = Fore.YELLOW
            atual = atual.prox
            print(
                corTexto + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100 + '\n' + '#' * 100)
            time.sleep(dificuldade)
            os.system('cls')
        print(Style.RESET_ALL)

    def mostraResposta(self, respostaJogador):
        atual = self.primeiro
        respostaCorreta = ''
        respostaErrada = ''
        while atual != None:
            respostaCorreta = respostaCorreta + str(atual.cor) + ' - '
            atual = atual.prox
        for resp in respostaJogador:
            respostaErrada = respostaErrada + str(resp) + ' - '
        print('Você errou!\n')
        print(f'Resposta correta: {respostaCorreta[:-2]}')
        print(f'Sua resposta foi: {respostaErrada[:-2]}')

    def recebeResposta(self, jogador, dificuldade):
        os.system('cls')
        atual = self.primeiro
        respostaJogador = []
        print('-=-=-=-=-=-Cores-=-=-=-=-=-')
        print(
            Fore.RED + '[1] Vermelho\n' + Fore.GREEN + '[2] Verde\n' + Fore.BLUE + '[3] Azul\n' + Fore.YELLOW + '[4] Amarelo' + Style.RESET_ALL)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n')
        while atual != None:
            resposta = int(input('Insira sua resposta: '))
            respostaJogador.append(resposta)
            if atual.cor != resposta:
                os.system('cls')
                self.mostraResposta(respostaJogador)
                print(f'\nSua pontuação foi de {jogador.pontuacao:.0f}')
                jogador.nome = input(f'\nInforme o seu nome: ')
                os.system('cls')
                return 0

            jogador.pontuacao += 1 / dificuldade
            atual = atual.prox
        return 1


def ordenaRanking(ranking):  # bubble sort, ordena CRESCENTE
    if len(ranking) == 0:
        print('Lista Vazia!')
    else:
        for i in range(len(ranking)):
            for j in range(len(ranking) - 1):
                if ranking[j].pontuacao < ranking[j + 1].pontuacao:
                    ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]


def iniciaJogo(ranking, dificuldade):
    genius = Genius()
    jogador = Jogador()
    continua = 1
    while continua != 0:
        genius.gerarCor()
        genius.mostraSequencia(dificuldade)
        continua = genius.recebeResposta(jogador, dificuldade)

    if len(ranking) < 5:
        ranking.append(jogador)
    else:
        ultimoJogador = min(ranking, key=attrgetter('pontuacao'))
        if jogador.pontuacao > ultimoJogador.pontuacao:
            ranking[ranking.index(ultimoJogador)] = jogador

    ordenaRanking(ranking)
    os.system('cls')


def mostraRanking(ranking):
    os.system('cls')
    posicao = 1
    for jogador in ranking:
        print(f'-=-=-=-=-=-=-{posicao}-=-=-=-=-=-=-')
        print(f'Nome: {jogador.nome}')
        print(f'Pontuacao: {jogador.pontuacao:.0f}\n')
        posicao += 1
    input()
    os.system('cls')


def selecionaDificuldade():
    os.system('cls')
    print('-=-=-=-=-=-Dificuldades-=-=-=-=-=-')
    print('[1] Normal')
    print('[2] Difícil')
    print('[3] Insano')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-')
    dificuldade = int(input('Digite a dificuldade desejada: '))
    if dificuldade == 1:
        dificuldade = 1
    elif dificuldade == 2:
        dificuldade = 0.5
    elif dificuldade == 3:
        dificuldade = 0.25
    else:
        print('\nOpção Inválida')
        dificuldade = 1
        input()
    os.system('cls')
    return dificuldade


ranking = []
opcao = 1
dificuldade = 1
while (opcao != 0):
    os.system('cls')
    print('-=-=-=-=-=-=-=-=-=-')
    print('1 - Novo Jogo')
    print('2 - Ranking')
    print("3 - Dificuldade")
    # print("4 - Regras")
    # print("5 - Modo daltônico")
    print('0 - sair')
    print('-=-=-=-=-=-=-=-=-=-')
    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        iniciaJogo(ranking, dificuldade)
    elif (opcao == 2):
        mostraRanking(ranking)
    elif (opcao == 3):
        dificuldade = selecionaDificuldade()
    elif (opcao == 0):
        break

print(' /\/\             /\/\ ')
print('(=´T´) Até mais! (`T`=)')