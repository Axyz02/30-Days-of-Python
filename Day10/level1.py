''''
for number in range(11):
    print(number)

for number in range(10, 0, -1):
    print(number)

for x in range(7):
    print('#' * x)

for x in range(8):
    for y in range(8):
        print('#'*8)
        '''
for x in range(11):
    print('{} x {} = {}'.format(x,x,x*x))
    
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for language in lst:
    print(language)

for number in range(101):
    if number % 2 == 0:
        print(number)

for number in range(101):
    if number % 2 != 0:
        print(number)



for i in range(8):
    for j in range(8):
        print("# ", end="")
    print()
