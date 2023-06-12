import adivinhacao
import forca

print('********************************')
print('****** Seletor de jogos ********')
print('********************************')

print('Escolha o jogo desejado')
jogos = int(input('(1) Adivinhação (2) Forca \n'))

if  (jogos == 1):
    print('Voce escolheu o jogo de adivinhação')
    adivinhacao.jogar()
elif (jogos ==2):
    print('Voce escolheu o jogo da forca')
    forca.jogar()
