number_n = int(input("Введите число N: "))
massiv = []

for i in range(1, number_n+1):
    massiv += [str(i)] 

print("".join(massiv))