import os

path = '/Users/meira/OneDrive/Рабочий стол/pp2'

print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nFiles:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll :")
print([ name for name in os.listdir(path)])
  