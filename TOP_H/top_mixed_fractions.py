#problem link https://toph.co/p/mixed-fractions?statement=bn_bd

import math
n,d = input().split()
n = int(n)
d = int(d)
en = n % d

qu = math.floor(n / d)

print(str(qu)+' '+str(en)+' '+str(d))
