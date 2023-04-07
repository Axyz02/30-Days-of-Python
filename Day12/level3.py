import random
def shuffle_list(lst=[]):
    random.shuffle(lst)
    return lst

def unique_numbers():
    possible_numbers = list(range(10))
    random.shuffle(possible_numbers)
    random_numbers = possible_numbers[:7]
    return random_numbers

print(unique_numbers())