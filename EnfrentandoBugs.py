# Como desenvolvedor sênior da Cubos Game, empresa da Cubos Academy destinada a 
#fazer jogos eletrônicos para computadores, você ficou responsável por implementar a 
#lógica que mostre ao jogador do "Enfrentando Bugs", novo jogo da empresa, se ele pode 
# ou não entrar na sala do chefão da fase em que ele se encontra no jogo.  Para ter o 
# direito de enfrentar o chefão, o jogador deve ter coletado três itens específicos ao 
# longo da fase, que variam de chefão para chefão.  
# Entrada: A entrada do seu programa será composta por quatro variáveis:  
# itensColetados: array de strings em que cada posição indica um item coletado ao
# longo da fase; itemNecessario1: uma string que indica o primeiro item necessário 
# para enfrentar o chefão; itemNecessario2: uma string que indica o segundo item 
# necessário para enfrentar o chefão; itemNecessario3: uma string que indica o terceiro 
# item necessário para enfrentar o chefão. Saída Você deve retornar:  PODE ENFRENTAR: caso o
# jogador tenha os três itens necessários para  enfrentar o chefão; NAO PODE ENFRENTAR: caso o
# jogador não tenha os três itens necessários para enfrentar o chefão. Exemplo Entrada 
# itensColetados = ["capa", "arco", "flecha", "machado", "escudo", "comida", "sapato", "capacete"] 
# itemNecessario1 = "machado"  
# itemNecessario2 = "espada"  itemNecessario3 = "sapato" 
# Saída NAO PODE ENFRENTAR  
#  Explicação Apesar do jogador ter conseguido coletar dois dois itens necessários, 
# o machado e o sapato, ele não conseguiu obter a espada.

def faseChefao(intensColetados,i1,i2,i3):
    intensColetados = list(intensColetados)
    if i1 and i2 and i3 in intensColetados:
        return "ENTRE AGORA NA SALA DO CHEFÃO!!"
    return "VOCE NÃO ESTÁ PERMITIDO ENTRAR NA SALA DO CHEFÃO AINDA!"

print(faseChefao(["vassoura magica","machado","esfera","escudo magico"], "machado","esfera","escudo magico"))
#segunda solução:
def checkArray(a,b):
    a = list(a)
    b = list(b)
    for x in b:
        for y in a:
            if y == x:
                a.remove(y)
            else:
                pass
    if len(a) == 0:
        return True
    else:
        return False
def faseChefao(itensColetados,i1,i2,i3):
    itensColetados = list(itensColetados)
    #i1,i2,i3 = "machado","esfera","escudo magico"
    for x in itensColetados:
        if x == i1 or x == i2 or x == i3:
            pass
        else:
            itensColetados.remove(x)
        itensNecessarios = [i1,i2,i3]
        if checkArray(itensNecessarios, itensColetados) == True:
            return "ENTRE AGORA NA SALA DO CHEFÃO!!"
        return "VOCE NÃO ESTÁ PERMITIDO ENTRAR NA SALA DO CHEFÃO AINDA!"
        
print(faseChefao(["machado","esfera","magia negra","vassoura do tempo"],"machado","esfera","escudo magico"))



