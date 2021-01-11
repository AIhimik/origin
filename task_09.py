# Ввести строку. Вывести на экран букву,
# которая находится в середине этой строки.
# Также, если эта центральная буква равна первой
# букве в строке, то создать и вывести часть строки
# между первым и последним символами исходной строки.
print('введите строку символов')
stroka = input()
dl_stroki = len(stroka)
nomer_simbol = dl_stroki // 2
cent_simbol = stroka[nomer_simbol]
print(cent_simbol)
if stroka[0] == cent_simbol:
    print(stroka[1:(dl_stroki - 1)])
