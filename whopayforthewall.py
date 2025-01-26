# Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go.
# Don Drumphet wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood association to pay for it.
# He begins to solicit his neighbors to petition to get the association to build the wall.
# Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, and can only remember two letters from each of his neighbors’ names.
# As he collects signatures, he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.

# Your code will show Full name of the neighbor and the truncated version of the name as an array.
# If the number of the characters in name is less than or equal to two, it will return an array containing only the name as is.


def who_is_paying(name):
    # Проверяем длинну имени
    if len(name) <= 2:
        # Если длина имени меньше или равна двум, добавляем имя в массив как есть
        return [name]
    else:
        # Иначе добавляем полное имя и его укороченную версию (первые две буквы) в массив
        return [name, name[:2]]


# Пример использования функции
neighbors = ["Richard", "Jony", "Melissa", "Mirlanda", "", "I"]

# Вызов функции с примерными именами и вывод результата
for neighbor in neighbors:
    result = who_is_paying(neighbor)
    print(
        f"Полное имя: {result[0]}, Сокращенное имя: {result[1] if len(result) > 1 else 'Нет сокращения'}"
    )
