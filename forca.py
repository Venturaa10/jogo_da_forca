import os
import random

# Desafio: Jogo da Forca

lista_palavras = ['ABC','America', 'Atletico', 'Avai', 'Bahia', 'Brusque', 'Botafogo', 'Bragantino', 'Ceara', 'Chapecoense', 'Confianca', 'Corinthians', 'Coritiba', 'Criciuma', 'Cruzeiro', 'CSA', 'CRB', 'Figueirense', 'Flamengo', 'Fluminense', 'Fortaleza', 'Ferroviario', 'Goias', 'Gremio', 'Guarani', 'Internacional', 'Ituano', 'Joinville', 'Juventude', 'Londrina', 'Mirassol','Nautico', 'Oeste', 'Operario', 'Palmeiras', 'Parana', 'Paysandu', 'Remo', 'Santos', 'Sergipe', 'Tombense', 'Vasco', 'Vitoria', 'Ypiranga']
armazena_forca = []
verifica = []
ver = []
chutes_errados = []
TENTATIVAS = 0

def limpa_terminal():
    os.system('cls')


def gera_forca():
    ''' Função responsável por:
    - Escolher uma das palavras dentro da lista lista_palavras para ser a palavra secreta/forca.
    - Criar uma cópia da palavra com "_" representando a quantidade de letras na palavra.
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
    '''Mensagem de introdução para inicializar o jogo.'''
    print('⚽⚽⚽  𝚂𝚎𝚓𝚊 𝙱𝚎𝚖 𝚅𝚒𝚗𝚍𝚘 𝚊 𝚘 𝙹𝚘𝚐𝚘 𝚍𝚊 𝙵𝚘𝚛𝚌𝚊 𝚍𝚘𝚜 𝚝𝚒𝚖𝚎𝚜 𝙱𝚛𝚊𝚜𝚒𝚕𝚎𝚒𝚛𝚘𝚜!  ⚽⚽⚽\n')
    input('"ENTER" para Iniciar... ')
    limpa_terminal()

def titulo_jogo():
    '''Exibi titulo personalizado
    '''
    limpa_terminal()
    print('⚽⚽⚽  𝕁𝕆𝔾𝕆 𝔻𝔸 𝔽𝕆ℝℂ𝔸 𝔻𝕆𝕊 𝕋𝕀𝕄𝔼𝕊 𝔹ℝ𝔸𝕊𝕀𝕃𝔼𝕀ℝ𝕆𝕊  ⚽⚽⚽!\n')

def verifica_tentivas():
    '''Função responsável por:
    Receber e validar o número de tentativas que o usuário forneceu. Ocorre um tratamento de erro caso o valor não seja um número.
    '''
    exibe_niveis()
    
    try:
        nivel = int(input('INFORME A DIFICULDADE: '))
    except:
        limpa_terminal()
        print('INFORME UMA OPÇÃO!\n')
        return verifica_tentivas()

    if nivel == 1:
        tentativas = 15
        total_tentativas = 15
        texto = 'FÁCIL'
        limpa_terminal()
        titulo_jogo()
        recebe_chute(palavra_forca, texto, tentativas, total_tentativas)
        
    elif nivel == 2:
        tentativas = 10
        total_tentativas = 10
        texto = 'INTERMEDIARIO'
        limpa_terminal()
        titulo_jogo()
        recebe_chute(palavra_forca, texto, tentativas, total_tentativas)

    elif nivel == 3:
        tentativas = 5
        total_tentativas = 5
        texto = 'DIFÍCIL'
        limpa_terminal()
        titulo_jogo()
        recebe_chute(palavra_forca, texto, tentativas, total_tentativas)

    else:
        limpa_terminal()
        print('ESSA OPÇÃO NÃO EXISTE!\n')
        verifica_tentivas()


    return nivel, tentativas, total_tentativas
    
    
def recebe_chute(palavra_forca, texto, tentativas, total_tentativas):
    '''Função responsável por:
    - Validar o chute do usuário.
    - Executar determinada função de acordo com o chute do usuário.
    - A lista ver é usada apenas para armazenar todas as letras da palavra_forca. Caso a lista verifica seja igual à lista ver, significa que o usuário acertou a palavra. Se não, o programa continuará sendo executado. Toda vez que a função for executada, a lista ver será limpa com o método .clear para evitar o acúmulo de letras da palavra_forca.
    - A lista ver serve apenas para fazer essa validação, pois nela ficam armazenadas as letras sem que ocorra alteração na lista. Quando as listas ver e verifica forem iguais, significa que o usuário acertou.
    '''
    exibe_tentativas(tentativas, total_tentativas)
    dificuldade_escolhida(texto)

    print(verifica)

    for l in palavra_forca:
        ver.append(l)

    if verifica == ver:
        limpa_terminal()
        return mensagem_ganhou(palavra_forca)
    elif tentativas == 0:
        limpa_terminal()
        return mensagem_perdeu(total_tentativas, palavra_forca)
    else:
        pass
    
    for chute in range(0, tentativas):
        ver.clear()
        
        try:
            chute_usuario = input('Digite uma letra: ').capitalize().strip()
        except:
            limpa_terminal()
            titulo_jogo()
            print('Essa informação não é valida\n')
            return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)

        if len(chute_usuario) == 1:
            verifica_letra_chute(chute_usuario,texto,tentativas,total_tentativas)
                            
        elif len(chute_usuario) < 1:
            limpa_terminal()
            titulo_jogo()
            print('✍  INFORME UMA LETRA!✍')
            return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)
                        
        else:
            limpa_terminal()
            titulo_jogo()
            print('✍  DIGITE AO MENOS UMA LETRA POR VEZ!✍')
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
    '''Função responsável por:
    - Informar que o chute está correto.
    Adicionar a letra na lista verifica, que armazena a formação da palavra correta, na mesma posição em que está presente na lista armazena_forca, de acordo com os acertos do usuário.
    - Remover e substituir o chute do usuário na palavra que armazena a forca. Com isso, caso determinada letra tenha mais de uma ocorrência na palavra, todas as suas ocorrências serão acrescentadas na lista que forma a palavra correta e removidas da lista armazena_forca em um único chute do usuário.
    '''
    while chute_usuario in armazena_forca:
        for indice ,letra in enumerate(armazena_forca):
            if letra.capitalize() == chute_usuario.capitalize():
                titulo_jogo()
                print('ACERTOU!👍\n')
                armazena_forca[indice] = '!'
                verifica[indice] = letra

    else:
        return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def chute_repetido(chute_usuario, texto, tentativas, total_tentativas):
    '''Função responsavel por verificar chutes certos repetidos'''
    titulo_jogo()
    print(f'A LETRA "{chute_usuario}" JÁ FOI INSERIDA!👎\n')
    return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def chute_errado_repetido(chute_usuario, texto, tentativas, total_tentativas):
    '''Função responsavel por verificar chutes errados repetidos'''
    titulo_jogo()
    tentativas -= 1
    print(f'A LETRA "{chute_usuario}" NÃO EXISTE NA PALAVRA E JÁ FOI INFORMADA ANTERIORMENTE!👎')
    print('INFORME UMA LETRA DIFERENTE!\n')
        
    return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def letra_nao_existe(chute_usuario, texto, tentativas, total_tentativas):
    '''Função responsavel por:
    - Subtrair a tentativa do usuario
    - Informar que o chute está incorreto
    '''
    titulo_jogo()
    tentativas -= 1
    chutes_errados.append(chute_usuario)
    print('ERROU!👎')
    print(f'A LETRA "{chute_usuario}" NÃO EXISTE NA PALAVRA!\n')
    return recebe_chute(palavra_forca, texto, tentativas, total_tentativas)


def exibe_tentativas(tentativas, total_tentativas):
    print(f'RESTAM {tentativas} TENTATIVAS DE {total_tentativas}!')


def exibe_niveis():
    '''Função responsavel apenas por exibir os niveis de dificuldades
    '''
    print("""            DIFICULDADES
            1 - FÁCIL --> 15 Chances
            2 - INTERMEDIARIO --> 10 Chances
            3 - DIFÍCIL --> 5 Chances
            """)


def dificuldade_escolhida(texto):
    print(f'DIFICULDADE: {texto}\n')
        

def mensagem_ganhou(palavra_forca):
    '''Função responsavel por exibir uma mensagem positiva caso o usuario acerte a palavra'''
    print(f'👏👏👏  PARABÉNS,VOCÊ ACERTOU A PALAVRA "{palavra_forca}"  👏👏👏')
    return jogar_novamente(lambda: mensagem_ganhou(palavra_forca))


def mensagem_perdeu(total_tentativas, palavra_forca):
    '''Função responsavel por exibir uma mensagem em caso de derrota no jogo'''
    print('⍨⍨⍨   FIM DE JOGO, VOCÊ PERDEU   ⍨⍨⍨\n')
    print(f'VOCÊ USOU TODAS AS SUAS {total_tentativas} TENTATIVAS ANTES DE DESCOBRIR A PALAVRA FORCA!')
    print(f'A PALAVRA FORCA ERA "{palavra_forca}"')
    return jogar_novamente(lambda: mensagem_perdeu(total_tentativas, palavra_forca))


def jogar_novamente(func):
    '''Função responsavel por: 
    Perguntar ao usuario se quer jogar novamente, e executar a função de acordo com a resposta do usuario.
    '''
    print()
    rejogar = input('Jogar novamente,"Sim" para rejogar ou "Nao" para sair.\n? ').capitalize().strip()

    if rejogar == 'Sim' or rejogar == 'S':
        armazena_forca.clear()
        verifica.clear()
        ver.clear()
        return jogo()
    elif rejogar == 'Nao' or rejogar == 'N':
        agradecimento()
    else:
        limpa_terminal()
        print('OPÇÃO INVALIDA!\n')
        return func()


def agradecimento():
    '''Função responsavel por exibir mensagem de agradecimento quando o usuario sair do jogo'''
    limpa_terminal()
    print('OBRIGADO POR JOGAR! :)\nESPERO QUE TENHA SE DIVERTIDO!')
    

if __name__ in '__main__':
    jogo()
    
