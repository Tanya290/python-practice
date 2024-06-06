#statements
#if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#while statement
i = 1
while i < 6:
  print(i)
  i += 1

#while with else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#for with else
for x in range(6):
  print(x)
else:
  print("Finally finished!")




# Conditional Statements
a = 20
b = 3

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")


#break statement
# for loop traversing from 1 to 4
for i in range(1, 5):
# If this condition becomes true break will execute
	if(i == 3):
	# Break statement will terminate the entire loop
		break
	print(i)

#continue statement
# for loop traversing from 1 to 5
for i in range(1, 6):
# If this condition becomes true continue will execute
	if(i == 2):
	# Continue statement will skip the iteration when i=2 and continue the rest of the loop
		continue
	print(i)
