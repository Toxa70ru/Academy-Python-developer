Spisoc = [-1, -2, -3, 0]
dlina = len(Spisoc)
print("Elements = ",Spisoc)
for i in range(dlina - 1):
    for j in range(dlina - i -1):
        if abs(Spisoc[j]) > abs(Spisoc[j+1]):
            Spisoc[j], Spisoc[j+1] = Spisoc[j+1], Spisoc[j]           
print("Результат после сортировки: ", Spisoc)