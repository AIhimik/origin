# Дан список целых чисел.Создать новый список, каждый элемент которого
# равен исходному элементу умноженному на -2
print('Введите список целых чисел через пробел. Вконце нажмите Enter')
spisok1 = [int(i) for i in input().split()]  # вводим элементы списка через пробел
n = len(spisok1)  # количество элементов в списке
i = 0
spisok2 = []  # вводим новый пустой список 2
while i < n:
    spisok2.append(spisok1[i] * -2)  # добавляем список 2 элементами из исходного списка, умноженных на -2
    i += 1
print(spisok2)
