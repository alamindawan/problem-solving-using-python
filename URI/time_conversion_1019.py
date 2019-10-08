import math
num = int(input())
h = m = s = 0
if num >= 3600:
    hm = hss = 0
    h = math.floor(num / 3600)
    hs = num % 3600
    if hs >= 60 and hs < 3600:
        hm = math.floor(hs / 60)
        hss = hs % 60
    else:
        hss = num % 3600
    timeTable = str(h)+':'+str(hm)+':'+str(hss)
elif num >= 60 and num < 3600:
    m = math.floor(num / 60)
    ms = num % 60
    timeTable = '0:'+str(m)+':'+str(ms)
else:
    s = num
    timeTable ='0:0:'+str(s)

print(timeTable)
