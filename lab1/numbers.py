#1
x = 5
x = float(x)

#2
x = 5.5
x = int(x)

#3
x = 5
x = complex(x)

#example 1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#example 2
print(type(x))
print(type(y))
print(type(z))

#example 3 INT
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#example 4 FLOAT
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#example 4 Floats
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#example 5 COMPLEX
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Example Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Example Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))
