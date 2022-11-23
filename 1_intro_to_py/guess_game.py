print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

secret_number = 42
tries = 3

for run in range(tries):
    print("\nTentativa {} de {}".format(run+1, tries))
    guess_str = input("Qual o seu chute? (Entre 1 e 100): ")
    guess = int(guess_str)

    correct = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

    if guess < 1 or guess > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    if correct:
        print("Acertô miseravi!")
        break
    else:
        if bigger:
            print("Errrrooouuu! O seu chute foi maior que o número secreto.")
        elif smaller:
            print("Errrrooouuu! O seu chute foi menor que o número secreto.")

print("\nFim do Jogo!")