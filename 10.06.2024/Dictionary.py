#dictionary:Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#create and print a dictionary:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
print(thisdict)


#Dictionary Items
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
print(thisdict["brand"])



#ordered or unordered
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicates Not Allowed.
#Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024,
  "year": 2020
}
print(thisdict)


#Dictionary Length
#To determine how many items a dictionary has, use the len() function:
#Print the number of items in the dictionary:

print(len(thisdict))

#Dictionary Items - Data Types
#The values in dictionary items can be of any data type:

#Example
#String, int, boolean, and list data types:

thisdict = {
  "brand": "bmw",
  "electric": False,
  "year": 2024,
  "colors": ["blue", "red", "black"]
}

#type()
#dictionaries are defined as objects with the data type 'dict':

<class 'dict'>


#Example
#Print the data type of a dictionary:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
print(type(thisdict))

#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.

#Example
#Using the dict() method to make a dictionary:

thisdict = dict(name = "jain", age = 49, country = "India")
print(thisdict)


#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
#Get the value of the "model" key:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
x = thisdict["model"]


#Get Keys
#The keys() method will return a list of all the keys in the dictionary.

#Example
#Get a list of the keys:

x = thisdict.keys()

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

#Get Values
#The values() method will return a list of all the values in the dictionary.

#Example
#Get a list of the values:

x = thisdict.values()

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "bmw",
"model": "330 Li",
"year": 2024
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.

#Example
#Get a list of the key:value pairs

x = thisdict.items()

#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

#Example
car = {
"brand": "bmw",
"model": "330 Li",
"year": 2024
}

x = car.items()

print(x) #before the change

car["year"] = 2021

print(x) #after the change



#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:

#Example
#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



#Change Values
#You can change the value of a specific item by referring to its key name:
#Change the "year" to 2021:

thisdict = {
  "brand": "bmw",
  "model": "33- Li",
  "year": 2024
}
thisdict["year"] = 2021


#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.

#Example
#Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
thisdict.update({"year": 2020})

#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
thisdict["color"] = "blue"
print(thisdict)


#Removing Items
#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
thisdict.pop("model")
print(thisdict)


#The clear() method empties the dictionary:

thisdict = {
  "brand": "bmw",
  "model": "330 Li",
  "year": 2024
}
thisdict.clear()
print(thisdict)

#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)


#Example
#Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

#You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

#A dictionary can contain dictionaries, this is called nested dictionaries.
#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "coco",
    "year" : 2020
  },
  "child2" : {
    "name" : "tiger",
    "year" : 2015
  },
  "child3" : {
    "name" : "truffle",
    "year" : 2018
  }
}


#Access Items in Nested Dictionaries
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

#Example
#Print the name of child 2:

print(myfamily["child2"]["name"])

#Loop Through Nested Dictionaries
#You can loop through a dictionary by using the items() method like this:

#Example
#Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.

#Method	Description
#clear()	        Removes all the elements from the dictionary
#copy()	            Returns a copy of the dictionary
#fromkeys()	        Returns a dictionary with the specified keys and value
#get()	            Returns the value of the specified key
#items()	        Returns a list containing a tuple for each key value pair
#keys()	            Returns a list containing the dictionary's keys
#pop()	            Removes the element with the specified key
#popitem()	        Removes the last inserted key-value pair
#setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	        Updates the dictionary with the specified key-value pairs
#values()	        Returns a list of all the values in the dictionary