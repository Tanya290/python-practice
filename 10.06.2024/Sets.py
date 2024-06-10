#sets:
#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Unordered
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Unchangeable
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.


#Duplicates Not Allowed
#Sets cannot have two items with the same value.

#Example
#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


#Get the Length of a Set
#To determine how many items a set has, use the len() function.
#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types
#Set items can be of any data type:

#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

#type()
#sets are defined as objects with the data type 'set':

<class 'set'>


#What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access Items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#To add one item to a set use the add() method.
#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


#add sets:
#add elements from tropical into thisset:
thisset={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

#add any iterable:
#the object in the update() method does not have to be a set, it can be any iterable object
#add elements of a list to a set:
thisset={"apple","banana","cherry"}
mylist=["kiwi","orange"]
thisset.update(mylist)
print(thisset)

#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


#Loop Items
#You can loop through the set items by using a for loop:
#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#Join Sets
#There are several ways to join two or more sets in Python.
#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.

#union:The union() method returns a new set with all items from both sets.
#join set1 and set2 into a new set:
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)


#Join Multiple Sets
#All the joining methods and operators can be used to join multiple sets.
#When using a method, just add more sets in the parentheses, separated by commas:
#Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"coco", "truffle"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


#join a set and a tuple:
x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)

#Update
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#Intersection
#Keep ONLY the duplicates
#The intersection() method will return a new set, that only contains the items that are present in both sets.

#Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)



#Difference
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

#Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Symmetric Differences
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

#Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


#Set Methods
#Python has a set of built-in methods that you can use on sets.

#Method	      Shortcut	                       Description
#add()	 	                           Adds an element to the set
#clear()	 	                       Removes all the elements from the set
#copy()	 	                           Returns a copy of the set
#difference()	-	                   Returns a set containing the difference between two or more sets
#difference_update()	-=	           Removes the items in this set that are also included in another, specified set
#discard()	 	                       Remove the specified item
#intersection()	&	                   Returns a set, that is the intersection of two other sets
#intersection_update()	&=	           Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	 	                   Returns whether two sets have a intersection or not
#issubset()	<=          	           Returns whether another set contains this set or not
# 	<	                               Returns whether all items in this set is present in other, specified set(s)
#issuperset()	>=	                   Returns whether this set contains another set or not
# 	>	                               Returns whether all items in other, specified set(s) is present in this set
#pop()	 	                           Removes an element from the set
#remove()	 	                       Removes the specified element
#symmetric_difference()	^	           Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	^=	   Inserts the symmetric differences from this set and another
#union()	|	                       Return a set containing the union of sets
#update()	|=	                       Update the set with the union of this set and others