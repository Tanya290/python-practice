#inheritance:
#it allows us to define a class that inherits all the methods and properties from another class
#parent class:class being inherited from 
#child class:class that inherits from another class


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)


x=person("tanya","nair")
x.printname()

#types of inheritance
#single:allows a derivative class to inherit properties of one parent class and this allows code reuse and the introduction of additional features in the existing code

#base class
class parent1:
    def func_1(self):
        print("this function is defined inside the parent class")

#derived class
class child1(parent1):
    def func_2(self):
        print("this function is defined inside the child class")

#example
object=child1()
object.func_1()
object.func_2()

#multiple inheritance:if a class is able to be created form multiple base classes, this kind of inheritance is multiple inheritance
#when there is a multiple inheritance, each of the attributes that are present in the classes of the base has been passed onto the class that is derived from it

#base class
class mother1:
    mothername1=""
    def mother1(self):
        print(self.mothername1)

#base class 2
class father1:
    fathername1=""
    def father1(self):
        print(self.fathername1)

#derived class
class son1(mother1,father1):
    def parents1(self):
        print("father name is:",self.fathername1)
        print("mother name is:",self.mothername1)

s1=son1()
s1.fathername1="rajesh"
s1.mothername1="shreya"
s1.parents1()


#multilevel inheritance:the features that are part of the original class, as well as the class that is derived from it, are passed on to the new class
#it is similar to a relationship involving grandparents and children

#base class
class grandfather1:
    def __init__(self,grandfathername1):
        self.grandfathername1=grandfathername1

#intermediate class
class father1(grandfather1):
    def __init__(self,fathername1,grandfathername1):
        self.fathername1=fathername1

        #we will invoke the constructor of grandfather class
        grandfather1.__init__(self,grandfathername1)

#derived class
class son1(father1):
    def __init__(self,sonname1,fathername1,grandfathername1):
        self.sonname1=sonname1

        #we will invoke the constructor of father class
        father1.__init__(self,fathername1,grandfathername1)
    
    def print_name(self):
        print("grandfather name is:",self.grandfathername1)
        print("father name is:",self.fathername1,)
        print("son name is:",self.sonname1)


#example
s1=son1("may","may jr","may jr jr")
print(s1.grandfathername1)
s1.print_name()


#hierarchial inheritance:if multiple derived classes are created from the same base, this kind of inheritance is known as hierarchial inheritance.in this instance, we have two base classes as parent(base) class as well as two children(derived)classes.

#base class
class parent1:
    def func_1(self):
        print("this function is defined inside the parent class")

#derived class1
class child_1(parent1):
    def func_2(self):
        print("this function is defined inside the child 1")

#derived class2
class child_2(parent1):
    def func_3(self):
        print("this function is defined inside the child 2")

#example
object1=child_1()
object2=child_2()
object1.func_1()
object1.func_2()
object2.func_1()
object2.func_3()