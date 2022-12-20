# Домашние / Дополнительные решения 

# Задача 1
# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет,  
# является ли этот день выходным. 
# Пример:
# - 6 -> да - 7 -> да - 1 -> нет  """

# First Decision

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print("число вне пределов 7 дней")


num = InputNumbers("Введите число: ")
checkNumber(num)

# Задача 1
# Second Decision
# Дано число обозначающее день недели. 
# Вывести его название и указать является ли он выходным.

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
n = int(input("Введите число, обозначающее день недели: "))
print(f"{days[n-1]} - рабочий день") if 0 < n < 6 else print(f"{days[n-1]} - выходной день")


# Задача 2
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится). 
# Пример:
# - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3  """

# First Decision

def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a

def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")

koordinate = inputKoord(2)
checkCoordinates(koordinate)


# Задача 2
# Second Decision

x, y = int(input("Введите координату x: ")), int(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка в 1-ой четверти координатной плоскости")
elif x < 0 and y > 0:
    print("Точка во 2-ой четверти координатной плоскости")
elif x < 0 and y < 0:
    print("Точка в 3-ей четверти координатной плоскости")
elif x > 0 and y < 0:
    print("Точка в 4-ой четверти координатной плоскости")
elif x == 0:
    print("Точка на оси Y")
else:
    print("Точка на оси X")


# Задача 3
# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  

# First Decision

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")



# Задача 3
# Проверить истинность утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат 

# Second Decision

def logical_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")



# 5 Семинар
# Задания с учебного Телеграм 
# Напишите программу вычисления арифметического выражения 
# заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# Пример:
# 2 + 2 => 4;
# 1 + 2 * 3 => 7;
# 1 - 2 * 3 => -5;

# Задача A

num = '1 * 2 * 3 / 5'
num = num.split()
print(num)
while len(num) > 1:
    while '*' in num or '/' in num :
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
        else:
            if '*' in num:
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
print(num)


# 5 Семинар
# Задания с учебного Телеграм
# Задача B

num = '1 + 2 + 3 - 5'
num = num.split()
print(num)
while len(num) > 1:
    while '+' in num or '-' in num :
        if num.count('*+') > 0 and num.count('-') > 0:
            if num.index('-') > num.index('+'):
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
        else:
            if '+' in num:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
print(num)


