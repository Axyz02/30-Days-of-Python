import math

def even_and_odds(number):
    total_even = 0
    total_odd = 0
    for i in range(0,number+1,1):
        if i % 2 == 0:
            total_even += 1
        elif i % 2 == 1:
            total_odd += 1
    return total_even, total_odd

even_odds = even_and_odds(100)
print('The number of odds are {}.\nThe number of evens are {}.'.format(even_odds[1],even_odds[0]))

def factorial(number):
    return math.factorial(number)

print(factorial(8))

def is_empty(param):
    if param != None:
        return False

print(is_empty(2))

