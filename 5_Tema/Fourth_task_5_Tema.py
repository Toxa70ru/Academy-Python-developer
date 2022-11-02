stroka = str(input("Введите строку для расшифровки: "))
result = ''
for ch in stroka:
    if ch.isupper() == True:
       result += ch
print("Сообщение: ",result)
