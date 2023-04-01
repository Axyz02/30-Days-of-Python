grade = int(input('Enter student score: '))

if grade >= 90:
    print('A')
elif grade > 69 and grade <90:
    print('B')
elif grade > 59 and grade < 70:
    print('C')
elif grade > 49 and grade <60:
    print('D')
else:
    print('F')

#Using a dictionary for a prettier code:
autumn = ('September', 'October', 'November')
winter = ('December', 'January', 'February')
spring = ('March', 'April', 'May')
summer = ('June', 'July', 'August')

month = input('Enter the month of the year: ')
if month in autumn:
    print('Autumn')
elif month in winter:
    print('Winter')
elif month in spring:
    print('Spring')
else:
    print('Summer')


fruit_user = input('Enter a fruit')
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit_user not in fruits:
    fruits.append(fruit_user)
    print(fruits)
else:
    print(fruits)