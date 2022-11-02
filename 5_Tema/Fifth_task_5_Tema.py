stroka = str(input())

count = 0
for w in stroka.split(" ") :
    if w.isalpha() :
        count = count + 1
        if count == 3 :
            print("True")
            break 
    else :
        count = 0
        print("False")
        break 
