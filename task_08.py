# Ввести строку. Если длина строки больше 10
# символов, то создать новую строку, равную текущей,
# с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки.
print('введите строку символов')
stroka = input()
if len(stroka) > 10:
    print(stroka + '!!!')
else:
    print(stroka[1])
