# Day 4: Exploring variables in Python
print("Welcome to Day 4 of my Python learning journey!")

# A variable is created the moment you first assign a value to it.
x = 23
print(x)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 'hello'
print(x)

# You can get the data type of a variable with the type() function.
y = 4
print (type (y))
print (type (x))

# Variable names are case-sensitive.
num = 2006
Num = 11
NUM = 20
print (num)
print (Num)
print (NUM)

'''
Rules for Python variables:

A variable name must start with a letter or the underscore character.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.                                       '''

_book = 'Harry Ptter'   # ✔️
House_no = 5            # ✔️
# 5th_streat           ❌ its wrong ! 


''' Multi Words Variable Names '''
# There are several techniques you can use to make them more readable:
'''   Camel Case    '''
# Each word, except the first, starts with a capital letter:
myVariableName = 'camel'
'''   Pascal Case    '''
# Each word starts with a capital letter:
MyVariableName = 'pascal'
'''   Snake Case     '''
# Each word is separated by an underscore character:
my_variable_name = 'snake'

print ( myVariableName )
print ( MyVariableName )
print ( my_variable_name )

# Assign Many Values to Multiple Variables
a , b , c = "apple ", "banana" , "grapes"
print (a)
print (b)
print (c)
# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
n = m = l = "python"
print(n)
print(m)
print(l)

s = 'its'
r = 'programming'
# n the print() function, you output multiple variables, separated by a comma:
print ( s , r )
# You can also use the + operator to output multiple variables:
print ( s +  r)
# For numbers, the + character works as a mathematical operator:
o = 2
p = 6
print (o + p)