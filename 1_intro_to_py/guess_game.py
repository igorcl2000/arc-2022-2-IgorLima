print("\n*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

secret_number = 42
guess = input("Digite o seu número: ")
print("Você digitou: ", guess)

if secret_number == int(guess):
    print("Acertô miseravi!")
else:
    print("Errrrooouuu!")

print ("Fim do jogo")