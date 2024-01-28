#1
a = 50
b = 10
if a > b:
    print("Hello World")
    
#2
a = 50
b = 10
if a != b:
    print("Hello World")

#3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
    
#4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
    
#5
if a == b and c == d:
    print("Hello")
    
#6
if a == b or c == d:
    print("Hello")

#7
if 5 > 2:
  print("YES")
  
#8
a = 2
b = 5
print("YES") if a == b else  print("NO")

#9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES") 
  
  
#example
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#example If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

#example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#example 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#example One line if statement:
if a > b: print("a is greater than b")

#exanple One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

#example One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#example Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#example Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
#example Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
#example 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")\
        
#example 
a = 33
b = 200

if b > a:
  pass


  
