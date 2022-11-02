from random import randint

number_X = randint(0,100)
number_Y = randint(0,100)

cel_rezalt = number_X // number_Y
ostatok = number_X - (cel_rezalt * number_Y)
print("Результат:")
print(cel_rezalt,",",ostatok)