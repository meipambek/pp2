import os
path = '/Users/meira/OneDrive/Рабочий стол/pp2/lab4'

if(os.path.exists(path)):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print('Does not exist')