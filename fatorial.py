
# #first solution
def fato(n):
    if n == 0 or n ==1:
        return 1
    if n <0:
        return "Impossible factorial!"
    return n*fato(n-1)

print(fato(0))

#second solution
def fatorial(a):
    if a < 0:
        return "Impossible factorial!"
    fatorial = 1
    for i in range(1, a+1):
        fatorial *= i
    return fatorial
print(fatorial(5))