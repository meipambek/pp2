#1
carname="Volvo"

#2
x=50

#3
X=5
print(x+y)

#4
z= x + y
print(z)

#5
x,y,z = "Orange", "Banana", "Cherry"

#6
x=y=z = "Orange"

#7
def myfunc():
  global x
  x = "fantastic"
  
#example
x = 5
y = "John"
print(x)
print(y)

#example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#example
x = 5
y = "John"
print(type(x))
print(type(y))

#example
x = "John"
# is the same as
x = 'John'

#example
a = 4
A = "Sally"
#A will not overwrite a

#example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#example
2myvar = "John"
my-var = "John"
my var = "John"

#example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#example
x = y = z = "Orange"
print(x)
print(y)
print(z)

#example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example
x = "Python is awesome"
print(x)

#example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#example
x = 5
y = 10
print(x + y)

#example
x = 5
y = "John"
print(x, y)

#example
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#example
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
