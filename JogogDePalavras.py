import random

score = 0
letraUsuario = ""
lista_palavras = {"carro" : "Veículo", "arroz" : "Grão", "colar" : "Pescoço", "batom" : "Objeto Feminino", "processador" : "Computador"}
respostacerta, dica = random.choice(list(lista_palavras.items()))
palavraEscolhida = [x for x in respostacerta]
numeroDeLetras = len(palavraEscolhida)
display = ['' for x in range(1, len(palavraEscolhida)+1)]

def localizarIndice(string):
    global palavraEscolhida
    string = str(string)
    lista_resultado = []
    if palavraEscolhida.count(string) == 0:
        return lista_resultado
    
    if palavraEscolhida.count(string) == 1:
        lista_resultado.append(palavraEscolhida.index(string))
        return lista_resultado
    
    if palavraEscolhida.count(string) > 1:
        for indice, letra in enumerate(palavraEscolhida):
            if letra == string:
                lista_resultado.append(indice)
        return lista_resultado

def inserirNoDisplay(string):
    string = str(string)
    resultado = localizarIndice(string) # retorna um indice
    if len(resultado) == 1:
        indice = palavraEscolhida.index(string)
        display[indice] = string
    if len(resultado) > 1:
        for i in resultado:
            display[i] = string
    return display

def verificadorLetra(letraUsuario):
    global palavraEscolhida
    global numeroDeLetras
    for letra in palavraEscolhida:
        if letraUsuario in palavraEscolhida:
            if palavraEscolhida.count(letraUsuario)>=1:
                numeroDeLetras = numeroDeLetras - palavraEscolhida.count(letraUsuario)
                inserirNoDisplay(letraUsuario)
                print("-------LETRA CORRETA!! -------\n Letras Restantes {}".format(numeroDeLetras))
                return display
        else:
            return "-----LETRA INCORRETA-----"       
def verificadorPalavraFinal():
    global score
    global respostacerta
    global dica
    global numeroDeLetras
    global display
    global lista_palavras
    global palavraEscolhida
    print(" -----------DIGITE A PALAVRA FINAL!!-----------")
    palavraFinal = input("DIGITE A PALAVRA CERTA: ")

    if palavraFinal == respostacerta: 
        print(" =============== PARABÉENS! VOCÊ GANHOU !! A PALAVRA É {}! ================= ".format(respostacerta.upper()))
        score += 100
        print("Voce ganhou 100 pontos! seu score: {}".format(score))
        respostacerta, dica = random.choice(list(lista_palavras.items()))
        palavraEscolhida = [x for x in respostacerta]
        numeroDeLetras = len(palavraEscolhida)
        display = ['' for x in range(1, len(palavraEscolhida)+1)]
        return MainGame()
    else:
        print("--------VOCÊ PERDEU!! NÃO FOI DESSA VEZ :C --------- \n PALAVRA CORRETA: {} \n SUA PALAVRA: {}".format(respostacerta, palavraFinal))
        respostacerta, dica = random.choice(list(lista_palavras.items()))
        palavraEscolhida = [x for x in respostacerta]
        numeroDeLetras = len(palavraEscolhida)
        display = ['' for x in range(1, len(palavraEscolhida)+1)]
        return MainGame()
    
def MainGame():
    print("==================== BEM VINDO AO WORD GAME =======================")
    print("\n" + "A DICA É : " + dica)
    print("Essa palavra contem {} letras.".format(numeroDeLetras))
    print(display)
    while(numeroDeLetras > 2):
        letraUsuario = input("Digite uma letra: ")
        print(verificadorLetra(letraUsuario))
    verificadorPalavraFinal()   

print(MainGame())






