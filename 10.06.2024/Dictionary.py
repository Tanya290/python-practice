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

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
