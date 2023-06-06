import random

lista_palavras = {"carro" : "veículo", "arroz" : "grão", "colar" : "pescoço"}
palavra, dica = random.choice(list(lista_palavras.items()))
print(palavra, dica)