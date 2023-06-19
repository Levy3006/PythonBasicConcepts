#Faça um Programa que peça uma data no formato dd/mm/aaaa
#e determine se a mesma é uma data válida.

ano = [x for x in range(1970,2024)]
mes = [y for y in range(1,13)]
ano_mes_dia = {}
for i in range(1,len(mes)+1):
    if len(mes) == 31:
        ano_mes_dia[i] = [x for x in range(1,32)]
    elif len(mes) == 30:
        ano_mes_dia[i] = [x for x in range(1,31)]
    elif len(mes) == 29:
        ano_mes_dia[i] = [x for x in range(1,29)]
print(ano_mes_dia)

def DateValidator(string):
    string = str(string)
    PADRAO = "dd/mm/aaaa"
    #slashes = [k for k in range(len(string)) if string.find('/', k) == k]
    padraoSeparado = PADRAO.split(sep='/') #lista
    condicaoSlash = string[2] == PADRAO[2] and string[5] == PADRAO[5] 
    condicaoDiaMesAno = len(padraoSeparado[0]) == len(string[0:2]) and len(padraoSeparado[1]) == len(string[3:5]) and len(padraoSeparado[2]) ==       len(string[6:10])
    if condicaoSlash and condicaoDiaMesAno:
        return True
    else:
        return False

print(DateValidator("01/02/1996")) #True
print(DateValidator("1999/12/30")) #False
print(DateValidator("30/06/2000")) #True
print(DateValidator("12345/1234")) #False

# expected outcome : True, False, True, False 