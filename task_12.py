# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()(подсказка: создается новый ключ
# с цифрой в конце,старый удаляется)
dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar':'usd', 'ruble': 'rub'}
i = 0
keys = list(dictionary.keys())  # получаем список ключей в словаре
n = len(keys)  # находим количество ключей в словаре
while i < n:
    new_key = f'{keys[i]}{len(keys[i])}'  # новые ключи
    dictionary[new_key] = dictionary.pop(keys[i])  # присваивание новому ключу значение из старого ключа
    i += 1
print(dictionary)

