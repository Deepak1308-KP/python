# def = defination 
# def <function>():
#     {
#     {    resuable code
#     {
#      <function>()
#     }

# Two types of functions 
# 1.inbuilt function
# print()
# len()
# type()
# input()
# sum()
# max()
# min()
# range()

# 2. user defined function
# def add(a, b):
#     return a + b
# print(add(10, 20))

# return
# Function starts
#      ↓
# Execute statements one by one
#      ↓
# Reach return
#      ↓
# Send value back
#      ↓
# STOP FUNCTION

# Adavntages
# code reusability
# reduce the code duplications
# improves readability
# debugging easir
# make testing is easir
# breaks larges prgm into the smaller module
# improves maintainability

# Example
# def addition():
#     return f"addition of 5 and 6 is {5+6}"
# print(addition ())

# def name():
#     for i in range(1,11):
#         print("Deepak")
# name()

# if not we use loop we want call function upto 
# 10 time for print name 10times
# def name():
#     print("Deepak")
# name();name();name();name();name();name();name();name();name();name();


#example for passing argumnet
# def print_scores(score, name):
#     print(f"i am {name} and i got {score} scores points")
# print_scores(80, "Deepak")

# def bank(bonus, blance):
#     print(f"your total bank blance is {bonus+blance}")
# bank(100, 220)  

##Positional Argument
# argument assigned according to the position

##Keyword argumnet
#Argument are passed using parameter and here order it is not matter
# def print_scores(score, name):
#     print(f"i am {name} and i got {score} scores points")
# print_scores(name="Deepak", score=90)

##Default Argument
# parameter have a default value, and
# it will be override by passing another name or value

# def print_scores(score, name="Deepak"):
#     print(f"i am {name} and i got {score} scores points")
# print_scores(80,"Deepak K P")


# ==>Variable length argument

# *args is used in a Python function to accept any number of positional
# arguments. The arguments are stored inside a tuple.
# *args allows a function to accept any number of positional arguments.


# def numbers(*num):
#     print(num)
# numbers(1,2,3,4,5,6,7,8,9)

# **kwargs is used in a Python function to accept any
# number of keyword arguments. The arguments are stored inside a dictionary.
# **kwargs allows a function to accept any number of keyword arguments

# def students(**details):
#     print(details)
# students(name="Deepak", Education="B.E", Native="Shivamogga")


# Order of execution if pass all in one prgm
# 1. Normal positional arguments
#           ↓
# 2. *args (extra positional arguments)
#           ↓
# 3. Keyword / keyword-only arguments
#           ↓
# 4. Default Keyword
#           |
# 5. **kwargs (extra keyword arguments)

# def print_scores(num1,*scores, num2:str="Deepak", num3, **number):
#     print(scores)
#     print(number)
#     print(num1)
#     print(num2)
#     print(num3)
# print_scores(67, 71,69, num3=72, year=2021, month=8)

# def check_num(num):
#     if num>0:
#         return "+ve"
#     elif num<0:
#         return "-ve"
#     else:
#         return 0
# print(check_num(0))


