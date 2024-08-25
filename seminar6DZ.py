"""

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
"""
"""
# Zadacha 1
# Считываем значения с клавиатуры
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

# Создаем массив для хранения элементов прогрессии
progression = []

# Заполняем массив элементами прогрессии
for i in range(n):
    an = a1 + i * d  # Формула для n-го элемента прогрессии
    progression.append(an)

# Выводим массив
print(" ".join(map(str, progression)))
"""

"""
# Zadacha 2
# Заданный массив
arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Заданные значения минимума и максимума
min_val = 7
max_val = 10

# Массив для хранения индексов элементов, которые находятся в заданном диапазоне
indices = []

# Итерируемся по массиву с использованием enumerate для получения индексов и значений
for index, value in enumerate(arr):
    if min_val <= value <= max_val:
        indices.append(index)

# Выводим индексы
print(indices)
"""