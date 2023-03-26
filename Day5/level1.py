emptylist = list()
numbers = [1,2,3,4,5]
print(len(numbers))
print(numbers[0],numbers[2],numbers[4])
mixed_data_types = ['Nicolas',24,1.73,'singe','Not today']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[3],it_companies[6])
it_companies[3] = 'Tracab'
print(it_companies)
it_companies.append('Nokia')
print(it_companies)
it_companies.insert(3, 'Samsung')
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
joined = '#; '.join(it_companies)
print(joined)
if 'IBM' in it_companies:
    print(True)
it_companies.sort()
print(it_companies)
it_companies.reverse()
it_slice1 = it_companies[3:]
it_slice2 = it_companies[:6]
print(it_companies)
it_companies.pop(0)
it_companies.pop(4)
it_companies.pop(-1)
it_companies.clear()
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.append('Python')
full_stack.append('SQL')
full_stack.append('Redux')