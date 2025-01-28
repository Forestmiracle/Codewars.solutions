# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.

# Examples:

# uniTotal("a") == 97
# uniTotal("aaa") == 291


def uni_total(string):
    return sum(ord(symvol) for symvol in string)


# Примеры
print(uni_total("a"))  # Выведет 97
print(uni_total("aaa"))  # Выведет 291
