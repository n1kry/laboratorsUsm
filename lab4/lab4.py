# Определение функций
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} добавлен в список покупок.")


def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} удален из списка покупок.")
    else:
        print(f"{item} отсутствует в списке покупок.")


def show_list(shopping_list):
    print("Текущий список покупок:")
    for item in shopping_list:
        print(item)


# Создание меню
def print_menu():
    print("\nМеню:")
    print("1. Вывести список текущих товаров")
    print("2. Добавить товар в список")
    print("3. Удалить товар из списка")
    print("4. Выход")


# Инициализация списка покупок и запуск цикла
shopping_list = []
while True:
    print_menu()
    choice = input("Выберите опцию (1-4): ")

    if choice == "1":
        show_list(shopping_list)
    elif choice == "2":
        item_to_add = input("Введите товар для добавления: ")
        add_item(shopping_list, item_to_add)
    elif choice == "3":
        item_to_remove = input("Введите товар для удаления: ")
        remove_item(shopping_list, item_to_remove)
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите от 1 до 4.")


# Пример использования функции со списком
def process_list(my_list):
    print("Элементы списка:")
    for item in my_list:
        print(item)


my_list = [1, 2, 3, 4, 5]
process_list(my_list)


# Пример использования функции с множеством
def process_set(my_set):
    print("Элементы множества:")
    for item in my_set:
        print(item)


my_set = {1, 2, 3, 4, 5}
process_set(my_set)


# Пример использования функции с словарем
def process_dict(my_dict):
    print("Ключи и значения словаря:")
    for key, value in my_dict.items():
        print(f"Ключ: {key}, Значение: {value}")


my_dict = {'a': 1, 'b': 2, 'c': 3}
process_dict(my_dict)
