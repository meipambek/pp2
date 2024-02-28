import re
s = input()
x = '^[a-z]+_[a-z]+$'
if re.search(x,  s):
    print("matches")
else:
    print("Not matches")