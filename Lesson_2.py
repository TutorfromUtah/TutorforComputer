# Задача 1
# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр. 
# Пример:- 6782 -> 23 - 0,56 -> 11

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")


# Задача 2
# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] 
# (1, 1*2, 1*2*3, 1*2*3*4) """

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

