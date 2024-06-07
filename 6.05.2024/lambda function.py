#A lambda function in Python is a small anonymous function defined using the lambda keyword.
# It is often used for creating small, one-off functions on-the-fly, especially in situations where a full function definition would be unnecessarily verbose.

#basic syntax
lambda arguments: expression

#key points
#Anonymous: Lambda functions do not have a name.
#Single Expression: Lambda functions are limited to a single expression. The result of this expression is automatically returned.
#Compact: They are more compact than traditional function definitions

#adding 2 numbers:
def add(x,y):
    return x+y

print(add(2,3)) #output:5

#map function
numbers=[1,2,3,4]
doubled=list(map(lambda x:x*2,numbers))
print(doubled)#output:[2,4,6,8]

#filter function
numbers=[1,2,3,4]
evens=list(filter(lambda x:x%2 ==0,numbers))
print(evens)#output:[2,4]