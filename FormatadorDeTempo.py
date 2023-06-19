
def ConverterHora(h):
    if h == 24:
        h = 0     
    elif h <= 12:
        pass    
    elif h > 12:
        h = h - 12 
    return h

def saida():
    while(True):
        h = int(input('digite a hora: '))
        m = int(input('digite os minutos: '))
        visor = f'{ConverterHora(h)}:{m}' + ' A' if (h <12) else f'{ConverterHora(h)}:{m}' + ' P'
        print(visor)
        
print(saida())