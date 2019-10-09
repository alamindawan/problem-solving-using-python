import math
num = 576.73

if num >= 100:
    note100 = math.floor(num / 100)
    remNote100 = num % 100

    if remNote100 >= 50 and remNote100 < 100:
        note50 =  math.floor(num / 50)
        remNote50 = num % 50
        if remNote50 >= 20 and remNote50 < 50:
            note20 =  math.floor(num / 20)
            remNote20 = num % 20
            if remNote20 >= 10 and remNote20 < 10:
                note10 =  math.floor(num / 10)
                remNote10 = num % 10

