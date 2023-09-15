# Условие: На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.

def multiplication(number):
    i = 1
    while i <= 10:
        j = 1
        while j <= number:
            print(f"{j} * {i} = {j * i} | ", end = "")
            j += 1
        print()
        i += 1

number = int(input("Введите число n: "))
multiplication(number)