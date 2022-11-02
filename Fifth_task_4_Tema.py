number1 = int(input("Введите целое число: "))
number2 = 0
max_size = 2**32

if(number1 > max_size) or (number1 < max_size * -1):
    print('"Обратное" ему число: 0')
elif number1 > 0:
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

