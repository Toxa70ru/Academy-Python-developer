number_x = int(input("Введите целое число: "))

if number_x % 2 != 0:
    print("Результат: Плохо")
elif 2 <= number_x <= 5 and number_x % 2 == 0:
    print("Результат: Неплохо")
elif 6 <= number_x <= 20 and number_x % 2 == 0:
    print("Результат: Так себе")
elif number_x % 2 == 0 and 20 <= number_x:
    print("Результат: Отлично")