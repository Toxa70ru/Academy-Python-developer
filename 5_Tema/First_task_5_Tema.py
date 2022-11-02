number = int(input("Введите целое положительное число: "))

if (number%3) == 0 and (number%5) == 0:
    print("Результат: Fizz Buzz")
elif number%3 == 0:
    print("Результат: Fizz")
elif number%5 == 0:
    print("Результат: Buzz")
else:
    print("Результат: ",number)        
