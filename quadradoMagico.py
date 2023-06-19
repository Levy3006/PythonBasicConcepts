def quadradoMagico(qm):
    qm = list(qm)
    condicaoLinhas   = qm[0]+qm[1]+qm[2] == qm[3]+qm[4]+qm[5] == qm[6]+qm[7]+qm[8]  
    condicaoColunas  = qm[0]+qm[3]+qm[6] == qm[1]+qm[4]+qm[7] == qm[2]+qm[5]+qm[8] 
    condicaoDiagonais= qm[0]+qm[4]+qm[8] == qm[2]+qm[4]+qm[6] 
    if condicaoLinhas and condicaoColunas and condicaoDiagonais:
        return "É QUADRADO MÁGICO!"
    return "NÃO É QUADRADO MÁGICO!"
    
print(quadradoMagico([8,3,4,1,5,9,6,7,2]))