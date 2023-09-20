# -*- coding: cp1251 -*-
import math
print('Добро пожаловать в калькулятор')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Возвести в степень')
print('6. Найти квадратный корень')
print('7. Нафти факториал')
print('8. Нафти синус')
print('9. Нафти косинус')
print('10. Найти тангенс')
print('11. Выход')
znachenie = input('Введите операцию: ')
 
while True:
    if znachenie == '1':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = a + b
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '2':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = a - b
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '3':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = a * b 
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '4':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        if b == 0:
            print('На ноль делить нельзя')
        else:
            c = a / b
            print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '5':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = a ** b
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '6':
        a = float(input('Введите число: '))
        c = math.sqrt(a)
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '7':
        a = float(input('Введите число: '))
        c = math.factorial(a)
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '8':
        a = float(input('Введите число: '))
        c = math.sin(math.radians(a))
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '9':
        a = float(input('Введите число: '))
        c = math.cos(math.radians(a))
        print(c)
        znachenie = input('Введите операцию: ')
    elif znachenie == '10':
        a = float(input('Введите число: '))
        c = math.tan(math.radians(a))
        print(c)
    elif znachenie == '11':
        print('Досвидание!')
        break
    else:
        break