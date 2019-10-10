

targetList = []
for x in range(1,101):
    num = int(input())
    if num in targetList:
        num = int(input())
    else:
        targetList.append(num)

maxNumber = max(targetList)
maxNumberIndex = targetList.index(maxNumber) + 1
print(maxNumber)
print(maxNumberIndex)
