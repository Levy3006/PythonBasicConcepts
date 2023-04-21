# write a programe that returns the largest number of a list
#solution: levi and carlos 
lista3 = [7,2,5,4,1,9,67,84,103,34,35]

maior = 0
for i in lista3:
    for x in lista3:
        if i > x and i > maior:
            maior = i
        if x > maior and x > maior:
            maior = x
        
print(lista3)
print("the largest number is {}".format(maior))

