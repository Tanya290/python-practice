#In Python, classes and objects are fundamental concepts of object-oriented programming (OOP). They allow you to create reusable, modular, and organized code by encapsulating data and behavior into logical units.
#create class
class MyClass:
  t = 24

#create object
p1=MyClass()
print(p1.x)

#__init__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("coco", 4)

print(p1.name)
print(p1.age)

#__str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("coco", 4)

print(p1)


#Key Concepts in OOP:
#Encapsulation: Bundling the data (attributes) and methods (functions) that operate on the data into a single unit, a class. This helps protect the data from outside interference and misuse.

#Inheritance: Creating a new class from an existing class. The new class, known as a subclass, inherits attributes and methods from the existing class, known as a superclass.

class animal:
  def __init__(self,name):
    self.name=name

  def speak(self):
    raise NotImplementedError("subclass must implement abstract method")
  
class cat(animal):
    def speak(self):
      return f"{self.name} says meow"
    
class dog(animal):
  def speak(self):
      return f"{self.name} says woof"

# Create instances of Cat and Dog
cat = cat("tuna")
dog = dog("bone")

print(cat.speak())  # Output: Whiskers says Meow
print(dog.speak())  # Output: Buddy says Woof

#Polymorphism: The ability to present the same interface for different underlying forms (data types). It allows methods to be used interchangeably between objects of different classes.

#Abstraction: Hiding the complex implementation details and showing only the necessary features of an object.