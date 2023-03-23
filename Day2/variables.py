#Day 2: 30 Days of Python programming
#Excercises Day 2
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md#-exercises---day-2

#Level 1

first_name = 'Nicolas'
last_name = 'Ibba Gonzalez'
full_name = 'Nicolas Andres Ibba Gonzalez'
country = 'Argentina'
city = 'Tigre'
age = 24
year = 2023
is_married = False
is_true = False
is_light_on = True

olFirst_name, olLast_name, olFull_name = 'Agustina', 'Centurion', 'Agustina Silvana Centurion'


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
name_comparision = len(last_name) - len(first_name)
print('La diferencia entre el nombre y el apellido es de ', name_comparision, ' letras.')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

area_of_circle = 3.14 * (30 ** 2)
circum_of_circle = (2*3.14)*30
radius = input('Ingrese el radio:')

first_name = input('Ingrese Nombre: ')
last_name = input('Ingrese Apellido: ')
country = input('Ingrese Pais: ')
age = input('Ingrese Edad: ')
