 # Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.

def maior_menor_soma(lista):  
    def menor(lista):
        menor = lista[0]
        for i in lista:
            if i < menor:
                menor = i
        return menor
    def maior(lista):
        maior = lista[0]
        for i in lista:
            if i > maior:
                maior = i
        return maior
    def soma(lista):
        soma = 0
        for i in lista:
            soma+=i
        return soma
    if maior(lista) > 1000:
        return "APENAS VALORES ENTRE 0 E 1000. O VALOR {} NÃO CORRESPONDE AO INTERVALO".format(maior(lista))
    if menor(lista) < 0:
        return "APENAS VALORES ENTRE 0 E 1000. O VALOR {} NÃO CORRESPONDE AO INTERVALO".format(menor(lista))
    return " Menor termo: {}\n Maior termo: {}\n Soma: {}".format(menor(lista),maior(lista),soma(lista))
print(maior_menor_soma([1,2,6,4,9,3,11]))