import collections
import math

a = input("Введите первую строку с цифрами через пробел. После окончания ввода нажмите ENTER\n")
a = a.strip(" ")
b = input("Введите вторую строку с цифрами через пробел. После окончания ввода нажмите ENTER\n")
b = b.strip(" ")

a = [int(i) for i in a.split(' ')]    #первая строка преобразуется в список
b = [int(i) for i in b.split(' ')]    #вторая строка преобразуется в список
if len(a) != len(b):
    print("Количество введенных данных в строках не совпадает")
else:
    for i in range(len(a)):
        print(f"Теугольник {i + 1} с катетами {a[i]} и {b[i]} имеет площадь {a[i] * b[i] / 2} и гипотенузу {round(math.sqrt(pow(a[i],2) + pow(b[i],2)),2)}")

