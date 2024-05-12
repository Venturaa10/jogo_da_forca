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

palavras_forca = ['Flamengo', 'Corinthians', 'Palmeiras', 'Vasco','Fluminense', 'Gremio', 'Cruzeiro', 'Santos', 'Internacional']
chances = 5
armazena_forca = []
verifica = []


input('Seja Bem Vindo a o Jogo da Forca dos times Brasileiros!\nIniciar... ')

forca = random.choice(palavras_forca).upper()
print(forca)


for letra in forca:
    armazena_forca.append(letra)

for v in armazena_forca:
    verifica.append('_')

while chances > 0:
    for i in range(0,chances):
        print(verifica)
        chute_usuario = input('Digite uma letra: ').upper()

        if chute_usuario in armazena_forca:
            posicao_letra = armazena_forca.index(chute_usuario) + 1
            print(posicao_letra)
            
            for under in verifica:
                verifica[posicao_letra - 1] = chute_usuario
                
            print('ACERTOU')

        else:
            chances = chances - 1
            print(f'ERROU, RESTAM {chances} de 5')

else:
    print('FIM DE JOGO! VOCÊ PERDEU')


print(armazena_forca)
# if __name__ in '__main__':
