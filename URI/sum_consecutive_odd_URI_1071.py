
number1 = int(input())
number2 = int(input())

totalOdd = 0;
for x in range(number2,number1):
    if x % 2 != 0:
        totalOdd += x
print(totalOdd)
