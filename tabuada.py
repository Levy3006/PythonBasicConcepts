
# o probelma consiste em 3 etapas:
# 1º: receber um número n ao qual se deseja obter a tabuada
# 2º: verificar se esse número é diferente de zero
# 3º: se for zero, o programa pintará uma mensagem informando que a tabuada de zero é zero.
# 4º: se o numero for diferente de zero, para cada numero no intervalo 0 a 10, o programa 
# exibirá "n x numero = " n*numero 

n = int(input("Digite um número"))

def tabuada(n):
    print("A tabuada de {} é:".format(n))
    if n == 0:
        print("A tabuada de zero é igual a zero")
    else:
        for i in range(1, 10 +1):
            print("{} x {} = {}".format(n,i,(n * i)))

tabuada(n)

