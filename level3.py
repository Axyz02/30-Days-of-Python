person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    lst = person['skills']
    print(lst[len(lst)//2])
if 'skills' in person:
    print('Python' in person['skills'])
skillset = set(lst)

front_end = ['JavaScript', 'React']
fullstack = front_end + ['Node', 'MongoDB', 'Python']

javascript, react, *rest = lst

if lst == front_end:
    print('Frontend developer')
elif lst == fullstack:
    print('Fullstack developer')
else:
    print('Unknown tittle')

if person.get('is_married') and person.get('country') == 'Finland':
    print('{} {} lives in {}. He is married'.format(person.get('first_name'), person.get('last_name'), person.get('country')))