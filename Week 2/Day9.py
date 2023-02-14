# Python Functions

# def my_function():
#     print("hello from a function")

# my_function() 

# Argument Passing

# def my_function(fname):
#     print(fname + " Allcroft")

# my_function("Connor")
# my_function("Brendan")
# my_function("Dylan")

# Multiple Arguments (args)

# def my_function(fname, lname):
#     print(fname + " " + lname)

# my_function("Connor", "Allcroft")

# Arbitrary Arguments (*args)

# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Connor", "Brendan", "Dylan")

# Keyword Arguments

# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)

# my_function(child1 = "Connor", child2 = "Brendan", child3 = "Dylan")

# Arbitrary Keyword Arguments (**kwargs)

# def my_function(**kid):
#     print("His last name is " + kid["lname"])

# my_function(fname = "Dylan", lname = "Allcroft")

# Default Parameter Value

# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Canada")

# Return Values

# def my_function(x):
#     return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(7))

# Recursion

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

