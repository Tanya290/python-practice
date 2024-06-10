#lists are used to store multiple items in a single variable
#list are one of 4 built in data types in python used to store collections of data, the other 3 are tuple, set and dictionary, all with different qualities and usage.
#lists are created using square brackets


#create a list
thislist=["coconut","almond","walnut"]
print(thislist)

#list items
#list items are ordered,changeable,and allow duplicate values
#list items are not indexed, the first item has index[0],the second item has index[1] etc

#ordered:
#when we say that lists are ordered,it means that the items have defined prder, and that order will not change
#if you add new items to a list, the new items will be placed at the end of the list

#changeable:
#we can change, add and remove items in a list after it has been created
#allow duplicate:
#since lists are indexed,lists can have items with the same value

thislist=["coconut","almond","walnut"]
print(thislist)

#lists allow duplicate values


#list length:
#to determine how many items has, use the len() function:
#print the number of items in the list:

thislist=["coconut","almond","walnut"]
print(len(thislist))

#list items-data types:
#string,boolean and int data types:
list1=["coconut","almond","walnut"]
list2=[1,2,3,4]
list3=[True,False,True]
#and also 
list1=["abc",25,True,80,"female"]

#type()
#lists are defined as objects with data type "list":
<class 'list'>
#what is the datatype of a list:
thislist=["coconut","almond","walnut"]
print(type(thislist))


#the list() constructor:
#it is also possible to use the list() constructor creating a new list
thislist=list(("coconut","almond","walnut")) #note the double round-brackets
print(thislist)

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered and changeable. No duplicate members.

#access items:
#list items are indexed and can be accessed by referring to the index number:
#print the second item of the list:

thislist=["coconut","almond","walnut"]
print(thislist[1])

#negative indexing:
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.

thislist=["coconut","almond","walnut"]
print(thislist[-1])

#range of indexes:
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items

thislist=["coconut","almond","walnut","cashew","dates","pista","raisin","hazelnut"]
print(thislist[2:5])

#negative index

thislist=["coconut","almond","walnut","cashew","dates","pista","raisin","hazelnut"]
print(thislist[-4:-1])

#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

thislist=["coconut","almond","walnut"]
if "almond" in thislist:
    print("yes, 'almond' is in the list")


#change item values
thislist=["coconut","almond","walnut"]
(thislist[1])="hazelnut"
print(thislist)

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:
#insert "raisin" as third item:

thislist=["coconut","almond","walnut"]
thislist.insert(2,"raisin")
print(thislist)

#extend list:
#To append elements from another list to the current list, use the extend() method.
thislist=['coconut',"almond","walnut"]
tropical=["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

#add elements of a tuple to a list:

thislist=['coconut',"almond","walnut"]
thistuple=("kiwi","orange")
thislist.extend(thistuple)
print(thislist)


#Remove Specified Item
#The remove() method removes the specified item.

thislist=['coconut',"almond","walnut"]
thislist.remove("almond")
print(thislist)

#remove specified index:
thislist = ["coconut", "almond", "walnut"]
thislist.pop(1)
print(thislist)

#Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.

thislist=['coconut',"almond","walnut"]
thislist.clear()
print(thislist)

#loop lists:
#You can loop through the list items by using a for loop:
#print all the items through the list items one by one:

thislist=['coconut',"almond","walnut"]
for x in thislist:
    print(x)


#loop through the index numbers:
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#print all items by referring to their index number:

thislist=['coconut',"almond","walnut"]
for i in range(len(thislist)):
    print(thislist[i])


#using a while loop:
#Print all items, using a while loop to go through all the index numbers

thislist = ["coconut", "almond", "walnut"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists:

#Example
#A short hand for loop that will print all items in a list:

thislist = ["coconut", "almond", "walnut"]
[print(x) for x in thislist]


#sorting lists:
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

#sort the list alphabetically:
thislist = ["coconut", "almond", "walnut", "hazelnut", "raisin"]
thislist.sort()
print(thislist)

#sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#Sort Descending
#To sort descending, use the keyword argument reverse = True:
thislist = ["coconut", "almond", "walnut", "hazelnut", "raisin"]
thislist.sort(reverse = True)
print(thislist)

#numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.

#The function will return a number that will be used to sort the list (the lowest number first):

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Case Insensitive Sort
# default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

#Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


#What if you want to reverse the order of a list, regardless of the alphabet?

#The reverse() method reverses the current sorting order of the elements.
#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#copy a list:
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.

#One of the easiest ways are by using the + operator.
#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



#LIST METHODS:
#METHOD              DESCRIPTION
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	    Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	    Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	    sSSorts the list