# Даны два действительных числа. Найти среднее
# арифметическое и среднее геометрическое этих
# чисел
from math import sqrt
print('Ввведите первое действительное число')
pervoe = float(input())
print('Ввведите второе действительное число')
vtoroe = float(input())
sr_arif = (pervoe + vtoroe)/2
sr_geom = sqrt(pervoe*vtoroe)
print('Среднее арифметическое =', sr_arif)
print('Среднее геометрическое =', sr_geom)
