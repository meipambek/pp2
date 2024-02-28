import re
s = input()
print(''.join(i.capitalize() or '_' for i in s.split('_')))


