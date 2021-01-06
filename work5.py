# Даны катеты прямоугольного треугольника. Найти его
# гипотенузу и площадь
from math import sqrt
print('Введите длину первого катета')
katet_a = float(input())
print('Введите длину второго катета')
katet_b = float(input())
gipotenuza = sqrt(katet_a*katet_a + katet_b*katet_b)
ploshad = (katet_a * katet_b)/2
print('Гипотенуза равна', gipotenuza)
print('Площадь треугольника равна', ploshad)