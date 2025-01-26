def next_id(ids):
    # Создаем множество из списка идентификаторов для удаления дубликатов и быстрого поиска
    unique_ids = set(ids)

    # Ищем минимальный неиспользованный идентификатор, начиная с 0
    next_id = 0
    while next_id in unique_ids:
        next_id += 1

    return next_id


# Пример использования функции
def main():
    used_ids_list = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [5, 4, 3, 2, 1],
        [0, 1, 2, 3, 5],
        [0, 0, 0, 0, 0, 0],
        [],
        [0, 0, 1, 1, 2, 2],
        [0, 1, 1, 1, 3, 2],
        [0, 1, 0, 2, 0, 3],
        [9, 8, 0, 1, 7, 6],
        [9, 8, 7, 6, 5, 4],
        [8, 0],
    ]
    for ids in used_ids_list:
        print(f"For input {ids}: Smallest unused ID is {next_id(ids)}")


if __name__ == "__main__":
    main()
