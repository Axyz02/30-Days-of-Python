import math
ex1 = 'Thirty' + 'Days' + 'Of' + 'Python'
ex2 = 'Coding' + 'For' + 'All'
company = 'Coding For All'
print(company)
print(len(company))
company = company.upper()
company = company.lower()
company = company.capitalize()
company = company.title()
company = company.swapcase()
company_sliced = company[0:7]
company = 'Coding For All'
company.index('Coding')
if 'Coding' in company:
    True
company.replace('Coding','Pyhton')
company = 'Coding For All'
company.split(' ')
company = 'Python For Everyone'
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(company[0])
print(company[-1])
print(company[10])
acronym = company[0] + company[7] + company[11]
print(acronym)
company = 'Coding For All'
acronym = company[0] + company[7] + company[11]
print(acronym)
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))
print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
phrase = 'You cannot end a sentence with because because because is a conjunction'
phrase = phrase[31:54]
print(phrase)
'You cannot end a sentence with because because because is a conjunction'.index('because')
if 'Coding For All'.startswith('Coding'):
    print(True)
else:
    print(False)
if 'Coding For All'.startswith('coding'):
    print(True)
else:
    print(False)
company = ' Coding For All '
company = company.removeprefix(' ')
company = company.removesuffix(' ')
print(company)

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#The second one
l1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(l1))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\t\tCity\nNicolas\t 24\tArgentina\tBuenos Aires')
r = 10
area = int(math.pi * r ** 2)
print('The area of a circle with radius {} is {} meters square.'.format(r,area))
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{}\033[1;31m * \033[1;37m{} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{}\033[1;31m ** \033[1;37m{} = {}'.format(a, b, a ** b))
#End of day 4!