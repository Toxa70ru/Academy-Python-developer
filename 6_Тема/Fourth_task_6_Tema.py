Spisoc = [3, 6, 20, 99, 10, 15]
dlina = len(Spisoc)
print("Список до сортировки: ", Spisoc)
senter_Spisoc = 0
mediana = 0
for i in range(dlina - 1):
    for j in range(dlina - i -1):
        if abs(Spisoc[j]) > abs(Spisoc[j+1]):
            Spisoc[j], Spisoc[j+1] = Spisoc[j+1], Spisoc[j]
print("Список после сортировки: ", Spisoc)

if dlina % 2 != 0:
    senter_Spisoc = dlina // 2
    print("Медиана = ",Spisoc[senter_Spisoc])
else:
    senter_Spisoc = dlina // 2

    senter_number1 = Spisoc[senter_Spisoc]
    senter_number2 = Spisoc[senter_Spisoc - 1]

    mediana =( senter_number1 + senter_number2) /2 
    print("Медиана = ",mediana)