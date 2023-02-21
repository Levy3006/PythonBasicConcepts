# -*- coding: utf-8 -*-
"""BasicExercis1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WGOBX4odOhoRDqc3Dom6Sr4paJlgsvJa
"""

# write a program that receives a list of numbers and return two new lists, one containing only even
# numbers and the other one containing only odd numbers

#creating the function that will provide the odd and even lists
def generatorList(lista):
    evenlist = []
    oddlist  = []
    #notice that we don't have any items in the even and odd lists. based on the list the function will receive
    # as a parameter, theses odd and even lists will be fullfield properly.

    #here's the logic of our program:
    for anynumber in lista:
        if anynumber % 2 == 0:
            evenlist.append(anynumber) 
        else:
            oddlist.append(anynumber)    
    return evenlist, oddlist

#finally we're gonna pass a list of numbers as a parameter, and our function will provide us two lists containing
# even and odd nmbers seperately:

generatorList([1,34,35,27,78,94,55,41,22])

# output: ([34, 78, 94, 22], [1, 35, 27, 55, 41])

#By Levy Pinheiro