print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

secret_number = 42
tries = 3
run = 1

while tries:
    print("\nTentativa", run, "de", tries)
    guess_str = input("Qual o seu chute? ")
    guess = int(guess_str)

    correct = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

    if correct:
        print("Acertô miseravi!")
    else:
        if bigger:
            print("Errrrooouuu! O seu chute foi maior que o número secreto.")
        elif smaller:
            print("Errrrooouuu! O seu chute foi menor que o número secreto.")

    run += 1
    tries -= 1

print("\nFim do Jogo!")