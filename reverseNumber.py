
# write a program to reverse any number
def reverse(num):
    reversed_number = 0
    while num > 0:
        reminder = num % 10 # here I'm getting the last digit of the number
        reversed_number = (reversed_number * 10) + reminder # here I'm adding the last digit of the current number to the reverse string
        num = num // 10  # here I'm cutting out the digit I've already added to the reversed number
    return reversed_number

print(reverse(123456))
print(123 % 10)