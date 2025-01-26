"""
# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

#Your task is to change the letters with diacritics:

ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z
and print out the string without the use of the Polish letters.

For example:

"Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
"""


# Объявляем функцию, заменяющую польские буквы с диакритиками на их аналоги без диакритиков
def correct_polish_letters(string):
    # Создаем словарь замен, где ключи - польские буквы с диакритиками, значения - их аналоги без диакритиков
    replacements = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
    }

    # Инициализируем пустую строку для хранения результата
    result = ""

    # Перебираем каждый символ во входной строке
    for char in string:
        # Если символ находится в словаре замен, добавляем в результат его замену
        if char in replacements:
            result += replacements[char]
        else:
            # Если символа нет в словаре замен, добавляем его в результат без изменений
            result += char

    # Возвращаем итоговую строку с заменами
    return result


# Пример использования функции
string = "Jędrzej Błądziński"
result = correct_polish_letters(string)
print(result)  # Ожидаемый результат: "Jedrzej Bladzinski"
