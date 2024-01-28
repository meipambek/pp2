#1
print(10>9)
True

#2
print(10==9)
False

#3
print(10<9)
False

#4
print(bool("abc"))
True

#5
print(bool(0))
False

#example
print(10 > 9)
print(10 == 9)
print(10 < 9)

#example Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#example Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#example Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#example The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#example The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example Print the answer of a function:
def myFunction() :
  return True

print(myFunction())

#example Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#example Check if an object is an integer or not:
x = 200
print(isinstance(x, int))


