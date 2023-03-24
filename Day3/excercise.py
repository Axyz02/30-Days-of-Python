import math
age = int(input('Ingrese edad: '))
height = float(input('Ingrese altura: '))
complex = 1j

# Script
#Start of the script
base = float((input('Enter base: ')))
height = float(input('Enter height: '))
print('The area of the triangle is: ', 0.5*base*height)


#Script 2
side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))
print('The perimeter of the triangle is: ', side_a + side_b + side_c)

#Script 3 
lenght = float(input('Enter lenght: '))
width = float(input('Enter width: '))
print('The area of the rectangle is: ', lenght * width)
print('The perimeter of the rectangle is: ', 2 * (lenght + width))

#Script 4
radius = float(input('Enter the radius: '))
print('Circle area is: ', 3.14*radius*radius)
print('Circle circumference is: ', 2*3.14*radius)

#8
slope1 = (0-0/-2-1)
print('The slope is: ', 0-0/-2-1)

#9
slope2 = (10-2/6-2)
print('The slope is: ', slope2)

print('The eucladian distance is: ',math.dist([2,2],[6,10]))

#10
n10 = slope1 - slope2


#11
var_x = -3
var_y = var_x^2 + 6*var_x + 9

#12
python_l = len('pyhton')
dragon = len('dragon')
falsy = python_l != dragon

#13
if 'on' in 'python' and 'on' in 'dragon':
    print("Both 'python' and 'dragon' contain 'on'")
else:
    print("At least one of 'python' and 'dragon' does not contain 'on'")

#14
if 'jargon' in 'I hope this course is not full of jargon':
    print('Jargpm is on the sentence')

#15
#I don't get this point

#16
pylen = float(len('pyhton'))
pylen = str(pylen)

#17
n = 1
if n%2 == 0:
    print('even number')

#18
if (7/3) == int(2.7):
    print('Equal')

#19
if type('10') == type(10):
    print('Equal type')

#20
if int('9.8') == 10:
    print('Equal')

#21 Script
hours = int(input('Enter hours: '))
rate = int(input('Enter rate: '))
print('Weekly earning is: ', hours*rate)

#22 Script
years = int(input('Enter number of years lived: '))
print('You lived for ', years*31,556,952, 'seconds')

#23
print(1,1**0, 1**1, 1**2, 1**3)
print(2,2**0, 2**1, 2**2, 2**3)
print(3,3**0, 3**1, 3**2, 3**3)
print(4,4**0, 4**1, 4**2, 4**3)
print(5,5**0, 5**1, 5**2, 5**3)