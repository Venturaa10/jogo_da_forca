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
tentativas = 0


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

    for i in armazena_forca:
        verifica.append('_')     

    return forca


def introducao():
    '''Mensagem de introdução para inicializar o jogo'''
    input('Seja Bem Vindo a o Jogo da Forca dos times Brasileiros!\nIniciar... ')


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

    else:
        return verifica_chute(forca)
        
def letra_nao_existe():
    
    limpa_terminal()
    input('ERROU!')
    return verifica_chute(forca)

def mensagem_ganhou():
    limpa_terminal()
    print(f'PARABÉNS,VOCÊ ACERTOU A PALAVRA "{forca}"')


def verifica_chute(forca):

    for l in forca:
        ver.append(l)

    print(ver)
    print(verifica)
    print(armazena_forca)
    print(forca)


    if verifica == ver:
        return mensagem_ganhou()
        
    else:
        pass


    ver.clear()
    chute_usuario = input('Digite uma letra: ').capitalize().strip()
        
    if len(chute_usuario) == 1:
        if chute_usuario in armazena_forca:
            letra_existe(chute_usuario)

        else:
            letra_nao_existe()

    elif len(chute_usuario) < 1:
        limpa_terminal()
        print('INFORME UMA LETRA!')
        return verifica_chute(forca)
            
    else:
        limpa_terminal()
        print('DIGITE AO MENOS UMA LETRA POR VEZ!')
        return verifica_chute(forca)
    

    

def verifica_tentivas():
    '''
    Verifica o número de tentativas e se o valor é valido, caso retorne True, o jogo se iniciara
    '''
    limpa_terminal()
    print('INFORME UM LIMITE DE TENTATIVAS ENTRE 3 E 15!')

    try:
        limite = int(input('Número de Tentativas: '))
    except:
        return verifica_tentivas()


    if limite < 3 or limite > 15:
        return verifica_tentivas()
    
    else:
        verifica_chute(forca)

    return limite
    

def jogo():
    limpa_terminal()
    gera_forca()
    introducao()
    verifica_tentivas()
    
print(armazena_forca)
if __name__ in '__main__':
    jogo()
    
