import os
import random

# Desafio: Jogo da Forca

# O programa deve seguir as seguintes diretrizes:

# Escolher aleatoriamente uma palavra de uma lista predefinida de palavras.
# Mostrar ao jogador a quantidade de letras na palavra escolhida, substituindo as letras por traços (-).
# Permitir que o jogador insira uma letra por vez.
# Verificar se a letra inserida está presente na palavra. Se estiver, substituir o traço correspondente pela letra.
# Se a letra não estiver presente na palavra, contar como um erro.
# Mostrar ao jogador a palavra parcialmente preenchida, as letras já tentadas e o número de erros.
# Permitir que o jogador continue tentando até adivinhar a palavra ou exceder um número máximo de erros (por exemplo, 6 erros para desenhar a forca completa).
# Dar ao jogador a opção de jogar novamente após o término do jogo.

palavras_forca = ['Flamengo', 'Vasco', 'Gremio','Palmeiras', 'Botafogo', 'Fluminense']

# palavras_forca = ['Botafogo','Bragantino','Fortaleza','Flamengo', 'Corinthians', 'Palmeiras', 'Vasco','Fluminense', 'Gremio', 'Cruzeiro', 'Santos', 'Internacional']
armazena_forca = []
verifica = []
ver = []


def limpa_terminal():
    os.system('cls')


def gera_forca():
    '''
    Seleciona a palavra da forca
    Cria uma copia da palavra com "_" representando a quantidade de letras da palavra
     '''
    global forca
    forca = random.choice(palavras_forca).upper()
    
    for letra in forca:
        armazena_forca.append(letra)

    for v in armazena_forca:
        verifica.append('_')     

    return forca


def introducao():
    '''Mensagem de introdução para inicializar o jogo'''
    input('Seja Bem Vindo a o Jogo da Forca dos times Brasileiros!\nIniciar... ')


 
def armazena_tentativa():
    global chances
    global limite
    chances = 0
    limite = int(input('Número de Tentativas: '))
    return chances, limite

def letra_existe(chute_usuario):
    while chute_usuario in armazena_forca:
        for indice ,letra in enumerate(armazena_forca):
            if letra.capitalize() == chute_usuario.capitalize():
                limpa_terminal()
                print(indice)
                print(letra)
                print('ACERTOU!')
                armazena_forca[indice] = '!'
                verifica[indice] = letra
            
        for l in forca:
            ver.append(l)

    else:
        return verifica_chute(forca)
        
def letra_nao_existe():
        
        limpa_terminal()
        limite - 1
        print('ERROU!')
        print(f'RESTAM {limite} TENTATIVAS!')
        return verifica_chute(forca)



def verifica_chute(forca):
    print(verifica)
    print(armazena_forca)
    print(forca)

    while verifica == ver:
        print(f'PARABÉNS,VOCÊ ACERTOU A FORCA "{forca}"')
        break
    else:
        ver.clear()
        chute_usuario = input('Digite uma letra: ').capitalize()

        if chute_usuario in armazena_forca:
            letra_existe(chute_usuario)

        else:
            letra_nao_existe()

    


def verifica_tentivas():
    '''
    Verificar o número de tentativas e se o valor é valido, caso retorne True, o jogo se iniciara
    '''
    limpa_terminal()
    print('INFORME UM NÚMERO DE 3 A 15!')

    try:
        armazena_tentativa()
    except:
        return verifica_tentivas()

    if limite < 3 or limite > 15:
        return verifica_tentivas()
    
    else:
            verifica_chute(forca)


    

def jogo():
    limpa_terminal()
    gera_forca()
    introducao()
    verifica_tentivas()
    
print(armazena_forca)
if __name__ in '__main__':
    jogo()
    
