import os 
path  = '/Users/meira/OneDrive/Рабочий стол/pp2/lab6/dir/currentfile.txt'
if os.path.exists(path):
    print("TRUE")
    os.remove(path)