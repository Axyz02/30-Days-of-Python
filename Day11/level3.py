import math
import countries_data

def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
            break
        else:
            return True
    else:
        return False

def is_unique(list):
    bufferlist = []
    for item in list:
        if item in bufferlist:
            return False
        else:
            bufferlist.append(item)
    return True

test_list = ['Nico', 'Matu', 'Jero']
test_list2 = ['Nico', 'Nico', 'Matu', 'Jero', 2]
print(is_unique(test_list))
print(is_unique(test_list2))

def same_data_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

print(same_data_type(test_list))
print(same_data_type(test_list2))

def is_valid_variable(var):
    """
    Check if a string is a valid Python variable.

    Args:
        var (str): A string to check.

    Returns:
        bool: True if the string is a valid Python variable, False otherwise.
    """
    # Check if the string is empty
    if var == "":
        return False

    # Check if the first character is a letter or underscore
    first_char = var[0]
    if not (first_char.isalpha() or first_char == "_"):
        return False

    # Check if the remaining characters are letters, digits, or underscores
    for char in var[1:]:
        if not (char.isalnum() or char == "_"):
            return False

    # Check if the string is a Python keyword
    keywords = ["and", "as", "assert", "break", "class", "continue", "def",
                "del", "elif", "else", "except", "False", "finally", "for",
                "from", "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise", "return",
                "True", "try", "while", "with", "yield"]
    if var in keywords:
        return False

    # If all checks pass, the string is a valid variable
    return True



def most_spoken_languages(num_languages=10):
    language_speakers = {}

    for country in countries_data.countries:
        for language in country["languages"]:
            language_speakers[language] = language_speakers.get(language, 0) + country["population"]

    sorted_languages = sorted(language_speakers.items(), key=lambda x: x[1], reverse=True)

    return [language[0] for language in sorted_languages[:num_languages]]

import countries_data

def most_populated_countries(num_countries=10):
    sorted_countries = sorted(countries_data.countries, key=lambda x: x["population"], reverse=True)

    return [country["name"] for country in sorted_countries[:num_countries]]
1