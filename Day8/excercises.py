dog = {}
dog['name'] = 'Samus'
dog['color']= 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 9
print(dog)

student = {
    'first_name':'Juan',
    'last_name':'Marces',
    'gender':'Male',
    'age':256,
    'marital_status':'Single',
    'skills':['HTML','CSS','JS','Python','AWS'],
    'country':'Argentina',
    'city':'Mendoza',
    'address':'Callefalsa 123'
}

print(len(student))
print(type(student['skills']))
student['skills'] += ['Azure','GCP']
print(student['skills'])
keys = student.keys()
values = student.values()
tple_list = student.items()
student.pop('marital_status')
print(student)
del student