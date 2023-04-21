
#Separate numerical values from text values in a string using .split(). 

def separate(genList):
    list_num = []
    list_alpha = []
    #genList is a generic list with random values
    #list_num is the list that'll get the numeric values
    #the list_alpha is the list that'll get the string values
    genList = list(genList)
    for i in genList:
        if type(i) == str:
            list_alpha.append(i)
        else:
            list_num.append(i)
    return "Numbers: {}\n Strings: {}".format(list_num, list_alpha)

listaB = ["A",1.5,3,"Levi","Amanda",3**(1/2)]
print(separate(listaB))
#Second Solution: Using list Comprehension 
def separate2(genList):
    list_alpha = [x for x in genList if type(x) == str]
    list_num   = [x for x in genList if type(x) != str]
    return "Numbers: {}\n Strings: {}".format(list_num, list_alpha)
listaC = [1,2,3,4,"Carlos","1"]
print(separate2(listaC))



