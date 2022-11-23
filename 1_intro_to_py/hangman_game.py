import random


def play():
    # Chama mensagem de abertura
    print_opening()

    # Carrega palavra secreta
    secret_word = load_secret_word()


def print_opening():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def load_secret_word():
    # Esta função sorteia uma palavra secreta
    # a partir de uma lista de palavras
    # armazenadas em um arquivo externo

    # abre o arquivo em modo de leitura (r)
    file = open("words.txt", "r")

    # lista para armazenar as palavras
    words = []

    for line in file:           # Para cada linha do arquivo
        line = line.strip()     # Remove o \n do final da linha
        words.append(line)      # Insere a palavra na lista

    #fecha o arquivo
    file.close()

    # sorteia um número para escolher a palavra secreta
    number = random.randrange(0, len(words))

    # seleciona a palavra secreta, coloca todos as letras em maiúsculo
    # e a retorna
    secret_word = words[number].upper()
    return secret_word


if __name__ == "__main__":
    play()