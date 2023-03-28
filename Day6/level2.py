brothers = ('Agus','Mati','Nacho','Rodrigo','Sergio')
sisters = ('Cata','Pia','Mel','Mariana')
family_members = brothers + sisters
print(family_members)
(*siblings, mother) = family_members
parents = family_members[3:5]
print(mother, parents)

fruits = ("apple", "banana", "cherry")
vegetables = ("Patato","Tomato","Bringle")
animal_products = ('Milk','Egs','Meat')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[4:5])
print(food_stuff_lt[0:3] + food_stuff_lt[6:9])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)