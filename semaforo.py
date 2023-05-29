# algoritimo de semaforo
import time
botaoPedestre = False
luzSemaforo = "----Verde-----"

def segundos(t):    
    while (t > 0):
        
        t -=1
        time.sleep(1)

def checagemDoBotao():
    global botaoPedestre
    global luzSemaforo
    if botaoPedestre == True:
        print("------- Sinal Vermelho em alguns instantes -------")
        print(luzSemaforo)
        segundos(10)
        luzSemaforo = "----Amarelo-----"
        print(luzSemaforo, "\n" + "ATENÇÂO!!")
        segundos(10)
        luzSemaforo = "------VERMELHO------"
        print(luzSemaforo, "\n" + " PARE!!")
        segundos(30)
        luzSemaforo = "----Verde-----"
        print(luzSemaforo,"\n" + "GO!!!")
        semaforo()
    else:
        semaforo()

def semaforo():
    global botaoPedestre
    global luzSemaforo
    botaoPedestre = False
    while (botaoPedestre == False):
        luzSemaforo = "----Verde-----"
        print(luzSemaforo)
        segundos(30)
        alterar = int(input("Deseja atraavessar a rua? 1 - Sim e 0 - Não "))
        alterar = bool(alterar)
        print(alterar, type(alterar)) 
        if alterar:
            botaoPedestre = True
            checagemDoBotao()
        else:
            botaoPedestre = False
            semaforo()
           
semaforo()