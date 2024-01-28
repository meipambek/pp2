#1
x = "Hello World"
print(len(x))

#2
txt = "Hello World"
txt[0]

#3
txt = "Hello World"
txt[2:5]

#4
txt = " Hello World "
txt.strip()

#5
txt = "Hello World"
txt.upper()

#6
txt = "Hello World"
txt.lower()


#7
txt = "Hello World"
txt.replace("H", "J")

#8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example 1
print("Hello")
print('Hello')

#Example 2
a = "Hello"
print(a)

#Example 3 You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example 4 You can use three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Example 4 Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#EXample 5 Loop through the letters in the word "banana":
for x in "banana":
  print(x)
  
#Example 6 The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Example 7
txt = "The best things in life are free!"
print("free" in txt)

#Example 8
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#Example 9 Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#Example 10 print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#Example Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Example Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Example Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

'''
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
b = "Hello, World!"
print(b[-5:-2])

#Example The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#Example The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#Example The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Example
a = "Hello"
b = "World"
c = a + b
print(c)

#Example
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Example
age = 36
txt = "My name is John, I am " + age
print(txt)

#Example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Example
txt = "We are the so-called \"Vikings\" from the north."
