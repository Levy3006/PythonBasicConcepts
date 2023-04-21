# Faça um programa que receba dois números inteiros e gere os números inteiros que 
# estão no intervalo compreendido por eles.

def intervalo(a,b):
    lista = []
    for i in range(a, b + 1):
        lista.append(i)
    return lista
print(intervalo(5,10))

def inter(a,b):
    for i in range(a, b + 1):
        print(i)
print(inter(5,10))