# -*- coding: cp1251 -*-
import math
print('����� ���������� � �����������')
print('1. ��������')
print('2. ���������')
print('3. ���������')
print('4. �������')
print('5. �������� � �������')
print('6. ����� ���������� ������')
print('7. ����� ���������')
print('8. ����� �����')
print('9. ����� �������')
print('10. ����� �������')
print('11. �����')
znachenie = input('������� ��������: ')
 
while True:
    if znachenie == '1':
        a = float(input('������� ������ �����: '))
        b = float(input('������� ������ �����: '))
        c = a + b
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '2':
        a = float(input('������� ������ �����: '))
        b = float(input('������� ������ �����: '))
        c = a - b
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '3':
        a = float(input('������� ������ �����: '))
        b = float(input('������� ������ �����: '))
        c = a * b 
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '4':
        a = float(input('������� ������ �����: '))
        b = float(input('������� ������ �����: '))
        if b == 0:
            print('�� ���� ������ ������')
        else:
            c = a / b
            print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '5':
        a = float(input('������� ������ �����: '))
        b = float(input('������� ������ �����: '))
        c = a ** b
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '6':
        a = float(input('������� �����: '))
        c = math.sqrt(a)
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '7':
        a = float(input('������� �����: '))
        c = math.factorial(a)
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '8':
        a = float(input('������� �����: '))
        c = math.sin(math.radians(a))
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '9':
        a = float(input('������� �����: '))
        c = math.cos(math.radians(a))
        print(c)
        znachenie = input('������� ��������: ')
    elif znachenie == '10':
        a = float(input('������� �����: '))
        c = math.tan(math.radians(a))
        print(c)
    elif znachenie == '11':
        print('����������!')
        break
    else:
        break