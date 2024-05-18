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


palavras_forca = ['Flamengo', 'Corinthians', 'Palmeiras', 'Vasco','Fluminense', 'Gremio', 'Cruzeiro', 'Santos', 'Internacional']
armazena_forca = []
verifica = []


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

def verifica_chute(limite, chances, forca):
    print(verifica)
    print(forca)

    while limite != 0:
        chute_usuario = input('Digite uma letra: ').upper()

        if len(chute_usuario) > 1:
            limpa_terminal()
            print('DIGITE UMA LETRA POR VEZ!')
            return verifica_chute(limite, chances, forca)
        
        else:
            pass
        
        if chute_usuario in armazena_forca:
            limpa_terminal()
            posicao_letra = armazena_forca.index(chute_usuario) + 1
            print(posicao_letra)
            print('ACERTOU')
                    
            for under in verifica:
                verifica[posicao_letra - 1] = chute_usuario 

            if armazena_forca == verifica:
                print('VOCÊ GANHOU!')
                break
            else: 
                return verifica_chute(limite, chances, forca)
    
                
                
        else:
            '''Tenho que arrumar essa mensagem para exibir a quantidade correta, conforme o usuario for errando a letra, o calculo no momento está incorreto'''
            limpa_terminal()

            print(f'ERROU! RESTAM {limite} DE {chances} TENTATIVAS')
            return verifica_chute(limite, chances, forca)
       

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
            verifica_chute(limite, chances, forca)


    

def jogo():
    limpa_terminal()
    gera_forca()
    introducao()
    verifica_tentivas()
    
print(armazena_forca)
if __name__ in '__main__':
    jogo()
    