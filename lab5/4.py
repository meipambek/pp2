import re
s = input()
x = '[A-Z]+[a-z]+$'
z = re.findall(x, s)
print(*x)  