# 2. Напишите функцию, которая проверяет является ли слово палиндромом

def palindrom(value):
    if len(value) <= 1: # если 1 значение или если не останется значений
        return "Палиндром"
    if value[0] != value[-1]: # если значения не равны
        return "Не палиндром"
    return palindrom(value[1:-1]) # убираем первый и последний символ

print(palindrom(input("Введите значение: ")))