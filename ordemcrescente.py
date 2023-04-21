
#faça um programa que receba um conjunto de 
# números e retorne esse conjunto em ordem crescente

def listaAscende(listaAleatoria):
    def menorNumero(lista):
        menor = lista[0]
        for i in lista:
            if i < menor:
                menor = i
        return menor
        
    listaAscendente = []
    while len(listaAleatoria) > 0:
        menor = menorNumero(listaAleatoria)
        listaAscendente.append(menor)
        listaAleatoria.remove(menor)
    return listaAscendente

print(listaAscende([22,-1,-7,5,15,99]),"\n")
print(listaAscende([5,3,0,4,1,2]),"\n")
print(listaAscende([55,67,101,999]),"\n")