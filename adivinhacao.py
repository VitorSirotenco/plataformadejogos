import random

numero_secreto = random.randrange(1,101)
total_tentativas = 0
rodada = 1

print('********************************')
print('Bem-vindo ao jogo de advinhação!')
print('********************************')

print('Níveis de dificuldade:')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input("Escolha o nivel:"))

if(nivel == 1):
    total_tentativas = 10
elif(nivel == 2):
    total_tentativas = 5
else:
    total_tentativas = 3


for rodada in range (1, total_tentativas + 1):
    chute_str = input('digite um numero entre 1 e 100: ') #devolveu um tipo string
    chute = int(chute_str) #função que transforma o retorno da variavel em int

    if(chute < 1 or chute > 100):
        print('voce dever chutar um numero de 1 a 100')
        continue

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if(acertou):
        print('voce acertou, parabens')
        break
    else:
        if(maior):
            print('Errou, vc chutou mt alto')
        elif(menor):
            print('Errou, vc chutou mt baixo')
    print('Tentativa {} de {}'.format(rodada, total_tentativas))

rodada = rodada + 1

print('final do jogo')
print('o numero era:', numero_secreto)






