import os
import random

# Desafio: Jogo da Forca

# O programa deve seguir as seguintes diretrizes:

# Escolher aleatoriamente uma palavra de uma lista predefinida de palavras. (FEITO)
# Mostrar ao jogador a quantidade de letras na palavra escolhida, substituindo as letras por traços (-). (FEITO)
# Permitir que o jogador insira uma letra por vez. (FEITO)
# Verificar se a letra inserida está presente na palavra. Se estiver, substituir o traço correspondente pela letra. (FEITO)
# Se a letra não estiver presente na palavra, contar como um erro. (FEITO)
# Mostrar ao jogador a palavra parcialmente preenchida, as letras já tentadas e o número de erros. (FEITO)
# Permitir que o jogador continue tentando até adivinhar a palavra ou exceder um número máximo de erros (por exemplo, 6 erros para desenhar a forca completa). (FEITO)
# Dar ao jogador a opção de jogar novamente após o término do jogo. (FALTA IMPLEMENTAR)

lista_palavras = ['Botafogo','Bragantino','Fortaleza','Flamengo', 'Corinthians', 'Palmeiras', 'Vasco','Fluminense', 'Gremio', 'Cruzeiro', 'Santos', 'Internacional']
armazena_forca = []
verifica = []
ver = []
chutes_errados = []
TENTATIVAS = 0

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


def jogo():
    limpa_terminal()
    gera_forca()
    titulo_introducao()
    verifica_tentivas()
    

def titulo_introducao():
    '''MENSAGEM DE INTRODUÇÃO PARA INICIALIZAR O JOGO'''
    input('𝚂𝚎𝚓𝚊 𝙱𝚎𝚖 𝚅𝚒𝚗𝚍𝚘 𝚊 𝚘 𝙹𝚘𝚐𝚘 𝚍𝚊 𝙵𝚘𝚛𝚌𝚊 𝚍𝚘𝚜 𝚝𝚒𝚖𝚎𝚜 𝙱𝚛𝚊𝚜𝚒𝚕𝚎𝚒𝚛𝚘𝚜!\n "ENTER" para Iniciar... ')

def titulo_jogo():
    '''TENHO QUE IMPLEMENTAR ESSE TITULO DA MANEIRA CORRETA!
    REFATORAR CÓDIGO!
    '''
    print('𝑱𝑶𝑮𝑶 𝑫𝑨 𝑭𝑶𝑹𝑪𝑨 𝑫𝑶𝑺 𝑻𝑰𝑴𝑬𝑺 𝑩𝑹𝑨𝑺𝑰𝑳𝑬𝑰𝑹𝑶𝑺!')

def verifica_tentivas():
    '''FUNÇÃO RESPONSAVEL POR:
    - RECEBER E VALIDAR O NÚMERO DE TENTATIVAS QUE O USUARIO FORNECEU, OCORRERA UM TRATAMENTO DE ERRO CASO O VALOR NÃO SEJA UM NÚMERO
    '''
    exibe_niveis()
    
    try:
        nivel = int(input('INFORME A DIFICULDADE: '))
    except:
        limpa_terminal()
        print('INFORME UMA OPÇÃO!')
        return verifica_tentivas()

    if nivel == 1:
        tentativas = 15
        total_tentativas = 15
        texto = 'FÁCIL'
        limpa_terminal()
        recebe_chute(palavra_forca, texto, tentativas, total_tentativas)
        
    elif nivel == 2:
        tentativas = 10
        total_tentativas = 10
        texto = 'INTERMEDIARIO'
        limpa_terminal()
        recebe_chute(palavra_forca, texto, tentativas, total_tentativas)

    elif nivel == 3:
        tentativas = 5
        total_tentativas = 5
        texto = 'DIFÍCIL'
        limpa_terminal()
        recebe_chute(palavra_forca, texto, tentativas, total_tentativas)

    else:
        limpa_terminal()
        print('ESSA OPÇÃO NÃO EXISTE!\n')
        verifica_tentivas()


    return nivel, tentativas, total_tentativas
    

def recebe_chute(palavra_forca, texto, tentativas, total_tentativas):
    '''FUNÇÃO RESPONSAVEL POR:
    - VALIDAR O CHUTE DO USUARIO
    - EXECUTAR DETERMINADA FUNÇÃO DE ACORDO COM O CHUTE DO USUARIO
    - A LISTA ver É APENAS PARA ARMAZENAR TODAS AS LETRAS DA palavra_forca, CASO A LISTA verifica SEJA IGUAL A LISTA ver SIGNIFICA QUE O USUARIO ACERTOU A PALAVRA, SE NÃO O PROGRAMA CONTINUARA SENDO EXECUTADO, TODA VEZ QUE A FUNÇÃO FOR EXECUTADA A LISTA ver SERÁ LIMPA COM O METODO .clear PARA EVITAR QUE O OCORRA UM ACUMULO DE LETRAS DA palavra_forca
    - A LISTA ver SERVE APENAS PARA FAZER ESSA VALIDAÇÃO, POIS NELA FICA ARMAZENADO AS LETRAS SEM QUE OCORRA ALTERAÇÃO NA LISTA, ENTÃO QUANDO ESSA LISTA E A verifica FOREM IGUAIS, SIGNIFICA QUE O USUARIO ACERTOU
    '''
    exibe_tentativas(tentativas, total_tentativas)
    dificuldade_escolhida(texto)

    print(verifica)

    for l in palavra_forca:
        ver.append(l)

    if verifica == ver:
        return mensagem_ganhou()
    elif tentativas == 0:
        return mensagem_perdeu(total_tentativas, palavra_forca)
    else:
        pass
    
    for chute in range(0, tentativas):
        ver.clear()
        
        try:
            chute_usuario = input('Digite uma letra: ').capitalize().strip()
        except:
            limpa_terminal()
            print('Essa informação não é valida\n')
            return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)

        if len(chute_usuario) == 1:
            verifica_letra_chute(chute_usuario,texto,tentativas,total_tentativas)
                            
        elif len(chute_usuario) < 1:
            limpa_terminal()
            print('INFORME UMA LETRA!')
            return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)
                        
        else:
            limpa_terminal()
            print('DIGITE AO MENOS UMA LETRA POR VEZ!')
            return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)
        
        return chute_usuario
        

def verifica_letra_chute(chute_usuario,texto,tentativas,total_tentativas):            
    if chute_usuario in armazena_forca:
        letra_existe(chute_usuario, texto, tentativas, total_tentativas)
    
    elif chute_usuario in verifica:
        chute_repetido(chute_usuario, texto, tentativas, total_tentativas)

    elif chute_usuario in chutes_errados:
        chute_errado_repetido(chute_usuario, texto, tentativas, total_tentativas)

    else:
        letra_nao_existe(chute_usuario, texto, tentativas, total_tentativas)



def letra_existe(chute_usuario, texto, tentativas, total_tentativas):
    '''FUNÇÃO RESPONSAVEL POR:
    - INFORMAR QUE O CHUTE É CORRETO
    - ADICIONAR A LETRA NA LISTA verifica QUE ARMAZENA A FORMAÇÃO DA PALAVRA CORRETA E NA MESMA POSIÇÃO EM QUE ESTÁ PRESENTE NA LISTA armazena_forca, DE ACORDO COM OS ACERTOS DO USUARIO
    - REMOVE E SUBSTITUI O CHUTE DO USUARIO DA PALAVRA QUE ARMAZENA FORCA, COM ISSO CASO DETERMINADA LETRA TENHA MAIS DE UMA OCORRENCIA NA PALAVRA, TODOS AS SUAS OCORRENCIAS SERAM ACRESCENTADAS NA LISTA QUE FORMA A PALAVRA CORRETA E REMOVIDAS DA LISTA armazena_forca EM UM ÚNICO CHUTE DO USUARIO
    '''
    while chute_usuario in armazena_forca:
        for indice ,letra in enumerate(armazena_forca):
            if letra.capitalize() == chute_usuario.capitalize():
                limpa_terminal()
                print('ACERTOU!\n')
                armazena_forca[indice] = '!'
                verifica[indice] = letra

    else:
        return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def chute_repetido(chute_usuario, texto, tentativas, total_tentativas):
    '''FUNÇÃO RESPONSAVEL POR VERIFICAR CHUTES CERTOS REPETIDOS'''
    limpa_terminal()
    print(f'A LETRA "{chute_usuario}" JÁ FOI INSERIDA!\n')
    return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def chute_errado_repetido(chute_usuario, texto, tentativas, total_tentativas):
    '''FUNÇÃO RESPONSAVEL POR VERIFICAR CHUTES ERRADOS REPETIDOS'''
    limpa_terminal()
    tentativas -= 1
    print(f'A LETRA "{chute_usuario}" NÃO EXISTE NA PALAVRA E JÁ FOI INFORMADA ANTERIORMENTE!')
    print('INFORME UMA LETRA DIFERENTE!\n')
        
    return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def letra_nao_existe(chute_usuario, texto, tentativas, total_tentativas):
    '''FUNÇÃO RESPONSAVEL POR:
    - SUBTRAIR A TENTATIVA DO USUARIO
    - INFORMA QUE O CHUTE ESTÁ INCORRETO
    '''
    limpa_terminal()
    tentativas -= 1
    chutes_errados.append(chute_usuario)
    print('ERROU!')
    print(f'A LETRA "{chute_usuario}" NÃO EXISTE NA PALAVRA!\n')
    return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def exibe_tentativas(tentativas, total_tentativas):
    print(f'RESTAM {tentativas} TENTATIVAS DE {total_tentativas}!')


def exibe_niveis():
    '''FUNÇÃO RESPONSAVEL APENAS POR EXIBIR OS NIVIES DE DIFICULDADES'''
    print("""
            DIFICULDADES
            1 - FÁCIL --> 15 Chances
            2 - INTERMEDIARIO --> 10 Chances
            3 - DIFÍCIL --> 5 Chances
            """)


def dificuldade_escolhida(texto):
    print(f'DIFICULDADE: {texto}\n')
        

def mensagem_ganhou():
    '''FUNÇÃO RESPONSAVEL POR EXIBIR UMA MENSAGEM POSITIVA CASO O USUARIO ACERTE A PALAVRA'''
    limpa_terminal()
    print(f'PARABÉNS,VOCÊ ACERTOU A PALAVRA "{palavra_forca}"')


def mensagem_perdeu(total_tentativas, palavra_forca):
    limpa_terminal()
    print('FIM DE JOGO, VOCÊ PERDEU :( ')
    print(f'VOCÊ USOU TODAS AS SUAS {total_tentativas} TENTATIVAS ANTES DE DESCOBRIR A PALAVRA FORCA!')
    print(f'A PALAVRA FORCA ERA "{palavra_forca}"')


if __name__ in '__main__':
    jogo()
    
