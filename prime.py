def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
def primeBetween(start, end):
    for y in range(start, end + 1):
        if (prime(y)):
            print("{} - Is prime".format(y))
        else:
            print("{} - Not prime".format(y))
print(primeBetween(1,10))

