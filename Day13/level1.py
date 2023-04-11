numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in numbers if i < 0]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

def flatten_list(list_of_lists):
    flattened_list = [element for sublist in list_of_lists for subsublist in sublist for element in subsublist]

    return flattened_list

print(flatten_list(list_of_lists))

lst = [(i, 1, i**2, i**3, i**4, i**5, i**6) for i in range(11)]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_flat = flatten_list(countries)
print(countries_flat)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dictionary = [{'country': country.upper(), 'city': city} for [[country, city]] in countries]

print(dictionary)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

lst = [' '.join(name) for [name] in names]

linear_fn = lambda x1, y1, x2, y2, var: (y2 - y1) / (x2 - x1)
