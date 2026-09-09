# def = defination 
# def <function>():
#     {
#     {    resuable code
#     {
#      <function>()
#     }

# Two types of functions 
# 1.inbuilt function
# 2. user defined function


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

def bank(bonus, blance):
    print(f"your total bank blance is {bonus+blance}")
bank(100, 220)