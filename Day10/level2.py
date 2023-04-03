sum = 0
sum_even = 0
sum_odds = 0
for number in range(101):
    sum += number
    if number % 2 == 0:
        sum_even += number
    elif number % 2 != 0:
        sum_odds += number

else:
    print('The sum of all numbers is: {}'.format(sum))
    print('The sum of all even numbers is: {}. And the sum of all odds is: {}'.format(sum_even, sum_odds))
