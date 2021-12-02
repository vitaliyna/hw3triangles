import math

b = []
c = []
a = input("Введите строку с цифрами через пробел. После окончания ввода нажмите ENTER\n")
a = [int(i) for i in a.split(' ')]
if len(a) % 2 != 0:
    print("Для каждого треугольника нужно ввести два катета. Вы же ввели нечетное количество чисел")
else:
    for i in range(len(a)):
        if a[i] % 2 > 0:
            b.append(a[i])
        if a[i] % 2 == 0:
            c.append(a[i])    
#for i in range(len(b)):
#    print(f"Теугольник {i + 1} с катетами {b[i]} и {c[i]} имеет площадь {b[i] * c[i] / 2} и гипотенузу {round(math.sqrt(pow(b[i],2) + pow(c[i],2)),2)}")

for i, j in zip(b, c):
    print(f"Треугольник {i + 1} с катетами {i} и {j} имеет площадь {i * j / 2} и гипотенузу {round(math.sqrt(pow(i,2) + pow(j,2)),2)}")