# -*- coding: utf8 -*-
def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя')