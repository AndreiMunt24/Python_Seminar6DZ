
"""
# sp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Возведем все значения в квадрат
# sp2 = []
# for el in sp:
#     sp2.append(el ** 2)

# print(sp2)
# print([el ** 2 for el in sp])
"""

# import random

# # Генерация списка случайных чисел
# # sp = []
# # for _ in range(10):
# #     sp.append(random.randint(-10, 10))
# # print(sp)

# # Генерация списка случайных чисел с использованием генератора списков
# # sp = [random.randint(-10, 10) for _ in range(10)]
# # print(sp)

# # Использование присваивания через :=
# # print(sp := [random.randint(-10, 10) for _ in range(10)])

# # Вывод элементов списка через распаковку
# # print(*sp)

# sp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Возведение всех значений в квадрат
# # sp2 = []
# # for el in sp:
# #     sp2.append(el ** 2)
# # print(sp2)

# # Использование генератора списков для возведения в квадрат
# # print([el ** 2 for el in sp])

# # Возведение в квадрат всех нечетных значений
# # print([el ** 2 for el in sp if el % 2])

# # Возведение в квадрат всех нечетных значений, а четные обнуление
# # print([el ** 2 if el % 2 else 0 for el in sp])

# sp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Создание словаря с индексами элементов в виде ключей
# # d = {str(i): sp[i] for i in range(len(sp))}
# # dd = {}
# # for i in range(len(sp)):
# #     dd[str(i)] = sp[i]
# # print(dd)
# # print(d)

# # Создание множества с остатками от деления на 2
# print({el % 2 for el in sp})



#  def is_champ(i):
# return n[i] > n[i -1] and n[i] > n[(i + 1)% len(n)]




# n = [4,6,2,8,9,44]
# # count = 0
# # for i in range(len(n)):
# # if n[i] > n[i -1] and n[i] > n[(i + 1)% len(n)]:
# # count +=1
# # print(count)

# print(sum([1 for i in range(len(n)) if is_champ(i)]))

# def is_champ(i, n):
#     return n[i] > n[i - 1] and n[i] > n[i + 1]

# n = [1, 5, 1, 5, 1]

# # Измененный код для решения задачи
# count = sum([1 for i in range(1, len(n) - 1) if is_champ(i, n)])
# print(count)  # Ожидаемый результат: 2



# def sum_of_divisors(n):
#     Вычисляет сумму делителей числа n (включая 1, но исключая само n).
#     total = 1
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             total += i
#             if i != n // i:
#                 total += n // i
#     return total

# def find_amicable_numbers(k):
#     """Находит и выводит все пары дружественных чисел, каждое из которых не превосходит k."""
#     visited = set()
#     for n in range(2, k + 1):
#         if n in visited:
#             continue
#         m = sum_of_divisors(n)
#         if m != n and m <= k and sum_of_divisors(m) == n:
#             print(n, m)
#             visited.add(n)
#             visited.add(m)

# # Пример использования
# k = int(input("Введите число k: "))
# find_amicable_numbers(k)


# def sum_number_divisors(a):
#     summ = 1
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             summ += i
#             if i != a // i:
#                 summ += a // i
#     return summ

# k = 1500

# # Выводим каждую пару дружественных чисел
# for n in range(1, k + 1):
#     n_summ = sum_number_divisors(n)
#     if n_summ > n and sum_number_divisors(n_summ) == n:
#         print(n, n_summ)

# # Выводим список всех пар дружественных чисел
# amicable_pairs = [(n, sum_number_divisors(n)) for n in range(1, k + 1) 
#                   if sum_number_divisors(n) > n and sum_number_divisors(sum_number_divisors(n)) == n]

# print(amicable_pairs)

# Определяем размер таблицы умножения
table_size = 9

# Используем генератор списка для создания таблицы умножения от 2 до 9
multiplication_table = [[f"{i} x {j} = {i*j}" for i in range(2, table_size + 1)] for j in range(2, table_size + 1)]

# Количество столбиков в одной строке
columns_per_row = 4

# Печать таблицы умножения с заданным количеством столбиков в строке
for i in range(0, len(multiplication_table[0]), columns_per_row):
    for j in range(len(multiplication_table)):
        row = "\t".join(multiplication_table[j][i:i + columns_per_row])
        print(row)
    print()  # Пустая строка для разделения блоков
