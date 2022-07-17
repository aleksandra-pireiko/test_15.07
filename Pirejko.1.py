# 1. напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def secret_number(card_number):
    if card_number.isdigit() is True and len(card_number) == 16: # проверяем соответствие введенного номера номерам карт
        secret_number = str()
        for i in card_number:
            if card_number.index(i) < 12: # заменяем первые 12 чисел звездочкой
                i = "*"
                secret_number += i
            elif card_number.index(i) > 11:
                secret_number += i
    else:
        print("Вы ввели несуществующий номер кредитной карты!")
    return secret_number

print(secret_number(str(input("Введите номер вашей карты: "))))