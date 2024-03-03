import math
a = input()
lower = 0
upper = 0
for i in a:
    if (i.isupper()):
        upper += 1
    else:
        lower += 1
print("uppercase:", upper)
print("lowercase:", lower)