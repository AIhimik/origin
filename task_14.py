# Составить список чисел Фибоначчи содержащий 15элементов.(подсказка: числа Фибоначчи - последовательность,
# вкоторой первые два числа равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущихчисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
spisok = [1, 1]  # задаем начальные элементы списка
while len(spisok) < 15:
    new_item = (spisok[-1] + spisok[-2])  # находим новые элементы списка
    spisok.append(new_item)  # расширяем список новыми элементами
print(spisok)
