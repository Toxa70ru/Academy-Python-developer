Spisoc = [10.2, -2.2, 0, 1.1, 0.5]
itog = 0

if len(Spisoc) == 0:
    print("Elements = ",Spisoc," Результат: 0")
else:
    itog = max(Spisoc) - min(Spisoc)
    print("Elements = ",Spisoc, " Результат:",'{0:.3}'.format(itog))
