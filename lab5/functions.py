def function_without_parameters():
    print("Функция без параметров вызвана.")


def function_with_parameters(param1, param2):
    print(f"Функция с параметрами вызвана. Параметры: {param1}, {param2}")


def function_with_default_value(param1, param2="по умолчанию"):
    print(f"Функция с предопределенным значением вызвана. Параметры: {param1}, {param2}")


def function_with_return_value():
    result = 42
    return result


multiply = lambda x, y: x * y
print("Результат lambda функции:", multiply(5, 3))


def sum_of_numbers(numbers):
    return sum(numbers)


def first_three_letters(words):
    return ''.join(word[:3] for word in words)


def highest_score_student(students):
    return max(students, key=students.get)


def common_keys_dict(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    return {key: (dict1[key], dict2[key]) for key in common_keys}


def reverse_words_order(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
