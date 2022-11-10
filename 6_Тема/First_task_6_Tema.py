Spisoc = [0,1,2,3,4,5]
summa = 0
itog = 0

if len(Spisoc) == 0:
    print("Elements = ",Spisoc," Результат: 0")
else:
    for index in range(len(Spisoc)):
        if index % 2 == 0:
            summa = summa + Spisoc[index]
    itog = summa * Spisoc[index]
    print("Elements = ",Spisoc, " Результат:",itog)


