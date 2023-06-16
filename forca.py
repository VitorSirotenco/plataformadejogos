def jogar():

    print('********************************')
    print('**Bem-vindo ao jogo da forca!***')
    print('********************************')

    palavra_secreta = 'banana'
    letras_acertadas = ['_','_','_','_','_','_',]

    enforcou = False
    acertou = False

    #enquanto (true)
    while (not enforcou and not acertou):

        chute = input('Qual letra? \n').strip() #pra desconsiderar espaços na letra

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #para comparar sempre entre letras maisculas
                letras_acertadas[posicao] = letra
                break
            elif(chute.upper() != letra.upper()):
                print('Não tem essa letra')
                break

            posicao = posicao +1

        print(letras_acertadas)


if(__name__ == '__main__'): #para chamar a função e rodar o jogo sem dar erro no arquivo jogos
    jogar()
