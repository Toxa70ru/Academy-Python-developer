number1 = int(input("Введите целое число: "))
number2 = 0

if number1 > 0:
    while number1 > 0:
        digit = number1 % 10 # находим остаток - последнюю цифру
        number1 = number1 // 10 # делим нацело - удаляем последнюю цифру
        number2 = number2 * 10 # увеличиваем разрядность второго числа
        number2 = number2 + digit # добавляем очередную цифру
    print('"Обратное" ему число:', number2)    
else:
    number1 = number1 * -1
    while number1 > 0:
        digit = number1 % 10
        number1 = number1 // 10
        number2 = number2 * 10
        number2 = number2 + digit 
    print('"Обратное" ему число:', number2 * -1) 
