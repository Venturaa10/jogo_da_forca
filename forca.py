import os
import random
os.system('cls')

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

palavras_forca = ['Flamengo', 'Corinthians', 'Palmeiras', 'Vasco','Fluminense', 'Gremio', 'Cruzeiro', 'Sao Paulo', 'Santos', 'Internacional']

armazena_escolha = []

def introducao():
    input('Seja Bem Vindo a o Jogo da Forca dos times Brasileiros!\nIniciar... ')

if __name__ in '__main__':
    pass