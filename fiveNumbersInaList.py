# make a program that reads 5 numbers from a list, and shows the sum, 
# multiplication and show the numbers

#creating the sum function:
def sum(randomList):
    randomList = list(randomList)
    sum_ = 0
    for x in randomList:
        sum_+= x
    return "The Sum is {} ".format(sum_)

#creating the times funcion
def times(randomList):
    randomList = list(randomList)
    times_ = 1
    for x in randomList:
        times_*= x
    return "The multiplication is {}".format(times_)

n = [2,6,4,12]
numbers = "The numbers are {}, {}, {}, {}".format(n[0],n[1],n[2],n[3])
sum_numbers = sum(n)
times_numbers = times(n)
print(numbers,"\n", sum_numbers,"\n", times_numbers)

# By @Levy3006 and @CarlosRavick