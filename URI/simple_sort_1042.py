a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
x = min(a, b, c)
z = max(a, b, c)
y = (a + b + c) - (x + z)

print(x)
print(y)
print(z)
print()
print(a)
print(b)
print(c)


