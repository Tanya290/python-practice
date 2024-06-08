#exception handling:
#types of exceptions in python:
#SyntaxError:is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon,or an unbalanced parenthesis
#TypeError:is raised when an operation when an operation or function is applied to an object of the wrong type, such as adding a string to an integer
#NameError:is raised when a variable or function name is not found in the current scope
#IndexError:is raised when an index is out of range for a list, tuple, or other sequence types
#KeyError:is raised when a key is not found in a dictionary
#ValueError:is raised when a function or method is called with an invalid argument or input such as trying to convert a string to an integer when the string does not represent a valid integer
#AttributeError:is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance
#IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
#ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
#ImportError: This exception is raised when an import statement fails to find or load a module.


#ex1
x=int(input("enter a number:"))
result=10/x
print("result:",result)


except ValueError:
print("please enter a valid number.")

except ZeroDivisionError:
print("cannot divide by zero.")



#nameerror
try:
   print(x)

except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#using else keyword:
try:
  print("hello.")
except:
  print("something went wrong.")
else:
  print("nothing went wrong")


#using finally:
try:
  print(x)
except:
  print("something went wrong")
finally:
  print("the 'try except' is finished")


#raise an exception:
x=-1
if x<0:
  raise Exception("sorry, no numbers below zero")


#typeerror:
x="hello"
if not type(x) is int:
  raise TypeError("only intergers are allowed")