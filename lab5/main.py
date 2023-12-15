from functions import *

# Вызов функций
function_without_parameters()

param1_value = 10
param2_value = "пример"
function_with_parameters(param1_value, param2_value)

function_with_default_value(param1_value)
function_with_default_value(param1_value, "новое значение")

result = function_with_return_value()
print("Результат функции с возвратом значения:", result)

# Задание 2
# a) Функция, которая получает список чисел и возвращает их сумму.
numbers_list = [1, 2, 3, 4]
result_sum = sum_of_numbers(numbers_list)
print(f"Сумма чисел в списке {numbers_list}: {result_sum}")

# b) Функция для создания строки из первых трех букв каждого слова
words_list = ["apple", "banana", "cherry"]
result_letters = first_three_letters(words_list)
print(f"Строка из первых трех букв каждого слова: {result_letters}")

# c) Функция для нахождения студента с самой высокой оценкой
students_grades = {'John': 85, 'Alice': 92, 'Bob': 78}
highest_scorer = highest_score_student(students_grades)
print(f"Студент с самой высокой оценкой: {highest_scorer}")

# d) Функция для создания словаря с общими ключами
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
common_keys_result = common_keys_dict(dict1, dict2)
print(f"Общие ключи и их значения: {common_keys_result}")

# e) Функция для обратного порядка слов в строке
input_string = "Hello world, how are you?"
reversed_words_result = reverse_words_order(input_string)
print(f"Строка с обратным порядком слов: {reversed_words_result}")