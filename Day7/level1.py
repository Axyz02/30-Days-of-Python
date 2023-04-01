# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Tracab','Variacode','PagerDuty'])
print(it_companies)
print(it_companies)
it_companies.pop()
print(it_companies)

#Remove method will raise errors if the desired item does not exist, however discard will not.

