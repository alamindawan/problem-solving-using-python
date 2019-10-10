inString = input()
fr = {}
  
for i in inString:
    if i in fr:
        fr[i] += 1
    else: 
        fr[i] = 1

for x,y in fr.items():
    if x != ' ':
        print(x+' = '+str(y))
    else:
        print('SPACE = '+str(y))
