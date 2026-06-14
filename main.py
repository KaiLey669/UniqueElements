import random


def add_unique_elements_to_list():
    return [random.randint(1, 10) for _ in range(10)]

def count_unique_elements(elems: list):
    return len(set(elems))


elems = add_unique_elements_to_list()
print(f"Список: {elems}")
print(f"Количество уникальных элементов: {count_unique_elements(elems)}")
