age = int(input('Enter your age: '))
if age > 18:
    print('You are old enough to learn to drive.')
else:
    print('Wait for ', 18-age,' more years to learn to drive.')
myage = 24

if myage >= age:
    print('I\'m {} years older.'.format(myage-age))
elif myage == age:
    print('We are the same age.')
else:
    print('You are {} years older'.format(age-myage))

number_1 = input('Enter one number: ')
number_2 = input('Enter a seconde number: ')

if a > b:
    print('A is greater than B')
elif a < b:
    print('A is less than B')
else:
    print('A is equeal to B')
