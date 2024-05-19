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

lista_palavras = ['Flamengo', 'Vasco', 'Gremio','Palmeiras', 'Botafogo', 'Fluminense']

# lista_palavras = ['Botafogo','Bragantino','Fortaleza','Flamengo', 'Corinthians', 'Palmeiras', 'Vasco','Fluminense', 'Gremio', 'Cruzeiro', 'Santos', 'Internacional']
armazena_forca = []
verifica = []
ver = []
chutes_errados = []

def limpa_terminal():
    os.system('cls')


def gera_forca():
    ''' FUNÇÃO RESPONSAVEL POR:
    - ESCOLHER UMA DAS DENTRO DA LISTA lista_palavras PARA SER A PALAVRA SECRETA/FORCA
    - CRIA UMA COPIA DA PALAVRA COM "_" REPRESENTANDO A QUANTIDADE DE LETRAS NA PALAVRA
    '''
    global palavra_forca
    palavra_forca = random.choice(lista_palavras).upper()
    
    for letra in palavra_forca:
        armazena_forca.append(letra)

    for i in armazena_forca:
        verifica.append('_')     

    return palavra_forca


def introducao():
    '''MENSAGEM DE INTRODUÇÃO PARA INICIALIZAR O JOGO'''
    input('Seja Bem Vindo a o Jogo da Forca dos times Brasileiros!\nIniciar... ')


def letra_existe(chute_usuario):
    '''FUNÇÃO RESPONSAVEL POR:
    - INFORMAR QUE O CHUTE É CORRETO
    - ADICIONAR A LETRA NA LISTA verifica QUE ARMAZENA A FORMAÇÃO DA PALAVRA CORRETA E NA MESMA POSIÇÃO EM QUE ESTÁ PRESENTE NA LISTA armazena_forca, DE ACORDO COM OS ACERTOS DO USUARIO
    - REMOVE E SUBSTITUI O CHUTE DO USUARIO DA PALAVRA QUE ARMAZENA FORCA, COM ISSO CASO DETERMINADA LETRA TENHA MAIS DE UMA OCORRENCIA NA PALAVRA, TODOS AS SUAS OCORRENCIAS SERAM ACRESCENTADAS NA LISTA QUE FORMA A PALAVRA CORRETA E REMOVIDAS DA LISTA armazena_forca EM UM ÚNICO CHUTE DO USUARIO
    '''
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
        return verifica_chute(palavra_forca)

def chute_repetido(chute_usuario):
    '''FUNÇÃO RESPONSAVEL POR VERIFICAR CHUTES CERTOS REPETIDOS'''
    limpa_terminal()
    print(f'A LETRA "{chute_usuario}" JÁ FOI INSERIDA!\n')
    return verifica_chute(palavra_forca)

def chute_errado_repetido(chute_usuario):
        '''FUNÇÃO RESPONSAVEL POR VERIFICAR CHUTES ERRADOS REPETIDOS'''
        limpa_terminal()
        print(f'A LETRA "{chute_usuario}" NÃO EXISTE NA PALAVRA E JÁ FOI INFORMADA ANTERIORMENTE!')
        print('INFORME UMA LETRA DIFERENTE!\n')
        return verifica_chute(palavra_forca)


def letra_nao_existe(chute_usuario):
    '''FUNÇÃO RESPONSAVEL POR:
    - SUBTRAIR A TENTATIVA DO USUARIO
    - INFORMA QUE O CHUTE ESTÁ INCORRETO
    '''
    limpa_terminal()
    chutes_errados.append(chute_usuario)
    print('ERROU!')
    print(f'A LETRA "{chute_usuario}" NÃO EXISTE NA PALAVRA!\n')
    return verifica_chute(palavra_forca)

def mensagem_ganhou():
    '''FUNÇÃO RESPONSAVEL POR EXIBIR UMA MENSAGEM POSITIVA CASO O USUARIO ACERTE A PALAVRA'''
    limpa_terminal()
    print(f'PARABÉNS,VOCÊ ACERTOU A PALAVRA "{palavra_forca}"')


def verifica_chute(palavra_forca):
    '''FUNÇÃO RESPONSAVEL POR:
    - VALIDAR O CHUTE DO USUARIO
    - EXECUTAR DETERMINADA FUNÇÃO DE ACORDO COM O CHUTE DO USUARIO
    - A LISTA ver É APENAS PARA ARMAZENAR TODAS AS LETRAS DA palavra_forca, CASO A LISTA verifica SEJA IGUAL A LISTA ver SIGNIFICA QUE O USUARIO ACERTOU A PALAVRA, SE NÃO O PROGRAMA CONTINUARA SENDO EXECUTADO, TODA VEZ QUE A FUNÇÃO FOR EXECUTADA A LISTA ver SERÁ LIMPA COM O METODO .clear PARA EVITAR QUE O OCORRA UM ACUMULO DE LETRAS DA palavra_forca
    - A LISTA ver SERVE APENAS PARA FAZER ESSA VALIDAÇÃO, POIS NELA FICA ARMAZENADO AS LETRAS SEM QUE OCORRA ALTERAÇÃO NA LISTA, ENTÃO QUANDO ESSA LISTA E A verifica FOREM IGUAIS, SIGNIFICA QUE O USUARIO ACERTOU
    '''

    for l in palavra_forca:
        ver.append(l)

    print(ver)
    print(verifica)
    print(armazena_forca)
    print(palavra_forca)

    if verifica == ver:
        return mensagem_ganhou()
        
    ver.clear()
    chute_usuario = input('Digite uma letra: ').capitalize().strip()
        
    if len(chute_usuario) == 1:
        if chute_usuario in armazena_forca:
            letra_existe(chute_usuario)

        elif chute_usuario in verifica:
            chute_repetido(chute_usuario)

        elif chute_usuario in chutes_errados:
            chute_errado_repetido(chute_usuario)

        else:
            letra_nao_existe(chute_usuario)

                    
    elif len(chute_usuario) < 1:
        limpa_terminal()
        print('INFORME UMA LETRA!')
        return verifica_chute(palavra_forca)
                
    else:
        limpa_terminal()
        print('DIGITE AO MENOS UMA LETRA POR VEZ!')
        return verifica_chute(palavra_forca)
    
    return chute_usuario

    

def verifica_tentivas():
    '''FUNÇÃO RESPONSAVEL POR:
    - RECEBER E VALIDAR O NÚMERO DE TENTATIVAS QUE O USUARIO FORNECEU, OCORRERA UM TRATAMENTO DE ERRO CASO O VALOR NÃO SEJA UM NÚMERO
    '''
    global limite
    
    limpa_terminal()
    print('INFORME UM LIMITE DE TENTATIVAS ENTRE 3 E 15!')

    try:
        limite = int(input('Número de Tentativas: '))
    except:
        return verifica_tentivas()


    if limite < 3 or limite > 15:
        return verifica_tentivas()
    
    else:
        verifica_chute(palavra_forca)

    return limite
    

def jogo():
    limpa_terminal()
    gera_forca()
    introducao()
    verifica_tentivas()
    

if __name__ in '__main__':
    jogo()
    
