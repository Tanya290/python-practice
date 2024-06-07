#encapsulation is one of the fundamental concepts in oop
#it describes the idea of wrapping data and the methods that work on data within one unit
#this pits restrictions on accessing variables and methods directly and can prevent the accidental modification of data
#to prevent accidental change an objects variable can only be changed ny an objects method
#those types of variables are known as private variables

#a class is an example of encapsulation as it encapsulates all the data that is member functions, variables etc.


#base class
class base:
    def __init__(self):
        self.a="python"
        self.__c="python"

#derived class
class derived(base):
    def __init__(self):

        #calling constructor of
        #base class
        base.__init__(self)
        print("calling private memeber of base class:")
        print(self.__c)

#example
obj1=base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class