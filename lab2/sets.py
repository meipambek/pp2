#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
    
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#example Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#example Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#example True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#example False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#example Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#example String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#example A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

#example What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#example Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#example Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#example Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#example Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#example Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#example Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#example Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#example Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#example Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#example The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#example The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#example Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#example The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#example The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#example 
'''
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''
