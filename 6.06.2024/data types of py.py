#python data types are the classification of data items.it represents the kind of value that tells what operations can be performed on a particular data
#since everything is an object in python the python data types are classes and variables are instances(objects)of these classes
#the following are the standard or buit-in data types in python:
#numeric
#sequence type
#boolean
#set
#dictionary

#numeric data type:represents data that has a numeric value.a numeric value can be an integer,a floating number or even a complex number.

#integer:this value is represented by int class.
       #it contains positive or negative whole numbers(without fractions or decimals)
       #in python,there is no limit to how long an integer value can be
#float:this value is reprensented by float class
       #it is a real number with a floating point representation
       #specified by a decimal point
#complex:reprensented by complex class
       #it is specified as real part+imaginary part


a=5
print("type of a:",type(a))

b=5.0
print("type of b:",type(b))

c=2+4j
print("type of c:",type(c))

#sequence data type:is the ordered collection of similar or different python data types.
         #allows storing of multiple values in an organized and efficient manner

        
#string:are arrays of bytes representing unicode characters
       #is a collection of one or more characters put in single quote,double quote or triple quote.


string1='welcome to python'
print("string with use of single quote:")
print(string1)

string2="welcome"
print("string with use of double quote:")
print(string2)


#accessing elements in string:
string1="python"
print("initial string:")
print(string1)
print("first character of string is:")
print(string1[0])
print("last character of string is:")
print(string1[-1])


#list:are just like arrays declared in other languages which is an ordered collection of data
    #it is very flexible as the items in a list do not need to be of the same type


list=[]
print("initial blank list:")
print(list)
list=["python"]
print("list with use of string:")
print(list)
list=["hello","to","python"]
print("list containing multiple values:")
print(list[0])
print(list[1])
print(list[2])

#tuple:is an ordered collection of python objects
      #immutable(cant be modified)
      #represented by tuple class

tuple1=()
print("initial empty tuple")
print(tuple1)

tuple1=("python","py")
print("tuple with use of string:")
print(tuple1)

list1=[1,2,3,4]
print("tuple using list:")
print(tuple(list1))

tuple1=tuple('python')
print("tuple with use of function:")
print(tuple1)

tuple1=(0,1,2,3)
tuple2=('python','py')
tuple3=(tuple1,tuple2) 
print("tuple with nested tuples:") 
print(tuple3)   

#boolean:true/false values
print(type(True))
print(type(False))

print(type(True))


#set data type:is an unordered collection of data types that is iterable,mutable and has no duplicate elements
set1=set()
print("initial blank set:")
print(set1)
set1=set("python")
print("set with use of string:")
print(set1)
set1=set(["py","python"])
print("set with use of listt:")
print(set1)
set1=set([1,2,"py","python"])
print("set with use of mixed values")
print(set1)

#dictionary:is an unordered collection of data values,used to store data values like a map
dict={}
print("empty dictionary:")
print(dict)

dict={1:'py',2:'python'}
print("dictionary with use of integer key:")
print(dict)

dict={'name':'geeks',1:[1,2,3,4]}
print("dictionary with the use of mixed keys:")
print(dict)

dict=dict{1:'py',2:'python'}
print("dictionary with use of dict():")
print(dict)

dict=dict([(1,'python'),(2,'py')])
print("dictionary with each item as a pair:")
print(dict)


