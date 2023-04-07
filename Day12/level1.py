import random
import string

def random_user_id(n_char = 6):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choices(characters, k = n_char))
    return random_id

def user_id_gen_by_user():
    number_of_characters = int(input('Enter number of characters: '))
    number_of_ids = int(input('Enter number of ID\'s: '))
    list_of_ids = list()
    for i in range(0,number_of_ids,1):
        list_of_ids.append(random_user_id(number_of_characters))
    return list_of_ids

def rgb_color_gen():
    color1 = random.randrange(0,255)
    color2 = random.randrange(0,255)
    color3 = random.randrange(0,255)
    color = 'rgb ({},{},{})'.format(color1,color2,color3)
    return color