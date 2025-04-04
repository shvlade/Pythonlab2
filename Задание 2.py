# -*- coding: utf8 -*-
def iskl():
    try:
        a = float(input("Введите число:"))
        b = float(input("Введите второе число:"))
        res = a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('напишите число')
    else:
        print(f"Результат: {res}")
iskl()


