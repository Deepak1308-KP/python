# Write a program that uses three functions to print information about a laundromat, Liam's Laundry:
# laundromat_info(): Prints the name, Liam's Laundry, and hours of operation, 7a - 11p, and calls washers_open() and dryers_open().
# washers_open(): Reads an integer, assigns washer_count with the value, and prints washer_count.
# dryers_open(): Reads an integer, assigns dryer_count with the value, and prints dryer_count.

# def washers_open():
#     washer_count = int(input())
#     print("Open washers:", washer_count)

# def dryers_open():
#     dryer_count = int(input())
#     print("Open dryers:", dryer_count)

# def laundromat_info():
#     print("Liam's Laundry")
#     print("7a - 11p")
#     washers_open()
#     dryers_open()
# laundromat_info()


# Write an updated function, terms(), that asks the user to accept the terms and conditions, reads in Y/N,
# and outputs a response by calling accepted() or rejected().
# accepted() prints "Thank you for accepting the terms." and rejected() prints "You have rejected the terms. Thank you."

# def accepted():
#     print("Thank you for accepting the terms.")
# def rejected():
#     print("You have rejected the terms.")
# def terms():
#     check_box=input("Do you accept the terms and conditions?(y/n):")
#     if check_box=="y":
#         accepted()
#     elif check_box=="n":
#         rejected()
# terms()



# Write a function, print_area(), that takes in the base and height of a right triangle and
# prints the triangle's area. The area of a right triangle is bh/2, where b is the base and h is the height.

# def area():
#     print("Enter a height and breadth to calculate area of triangle")
#     a =int(input("Base:"))
#     b=int(input("Height:"))
#     print(f"{a*b/2}")
# area()

##Another method
# def print_area(base, height):
#     area =(base*height)/2
#     print("Triangle area", area)
# print_area(3,4)


# Write a function, print_scores(), that takes in a 
# list of test scores and a number representing how many points to add. For each score,
# print the original score and the sum of the score and bonus. Make sure not to change the list.

# def total(score, bonus):
#     for value in score:
#         updated_score= value+bonus
#         print(f"{score} be updated to {updated_score}")
# total([67, 68, 72, 71, 69], 10)


#Filter Function
# num=[1,44,2,3,4,5,6,7,8]
# fill=list(filter(lambda x:x%2==0, num))
# print(fill)

##using user defined function replacing in the place of lambda 

# def squr(x):
#     return x*x
# num=[1,2,3,4,5,6,7,8]
# result=list(map(squr, num))
# print(result)

# def n(x):
#     return x.upper()
# name=["deepak", "gagan"]
# result=list(map(n, name))
# print(result)

# """Write a Python program to calculate a student's total marks, percentage, and result using user-defined functions.
# The program should:
# Create a function calculate_total() that accepts marks of 3 subjects and returns the total marks.
# Create a function calculate_percentage() that accepts the total marks and calculates the percentage.
# Create a function check_result() that accepts the percentage.
# If the percentage is 40 or above, return "Pass".
# Otherwise, return "Fail".
# Display the Total, Percentage, and Result.
# """

# def calculate_total(maths, science, physics):
#     return maths+science+physics
# def calculate_percentage(total):
#     return total/3
# def check_result(percentage):
#     if percentage>=40:
#         return "Pass"
#     else:
#         return "Fail"
# total=calculate_total(20, 43, 20)
# percentage=calculate_percentage(total)
# result=check_result(percentage)
# print("total:", total)
# print("percentage:", percentage)
# print("Result:", result)

##Function returning multiple values 
# def multiple(a,b,c):
#     return a+b,a-b,a*b, a/b
# w,x,y,z=multiple(1,2,3)
# print(w)
# print(x)
# print(y)
# print(z)

##Global VAriable
# x=100
# def gol(a):
#     global y
#     y=20
#     return a+x+y
# print(gol(3))
# print(y)



# students=[("A",80), ("B",60), ("C",90)]
# students.sort(key=lambda x:x[1])
# print(students)

# nums=[35,45,65,21,30,69,12,86]
# nums.sort(key=lambda x:x>=35)
# print(nums)

# only we pass only positional argumnet without a keyword argument
# def posti(a, b,/):
#     return a+b
# ans=posti(10,20)
# print(ans)

# only we pass only keyword  argumnet after giving a * without a positional argument
# def keyword(name,*, age, place):
#     return f"name:{name},\n Age:{age},\n place:{place}"
# print(keyword("Deepak", age=66,place="xyz"))

##FUnction argument unpacking 
# for the unpacking list we will use a * for a list 
#for dictionary we will use 2*

# def students(a,b,c,d):
#     return a,b,c,d
# marks=[23,45,78,88]
# print(students(*marks))

# for dictionary unpacking
# def students(name,age,place):
#     return name,age,place
# details={"name":"deepak", "age":22, "place":"Bnglr"}
# print(students(**details))

# DECORATOR= modify or extend there behaviour with out changing original code
# def decorator(func):
#     def wrapper():
#         print("before decoration")
#         func()
#         print("After decoration")
#     return wrapper
# @decorator
# def greet():
#     print("Hello world")
# greet=decorator(greet)  for this implementation we will use @decorator
# greet()


##Default mutable argument 
# def cal(item,items=None):
#     if items is None:
#         items=[]
#     items.append(item)
#     return items
# print(cal(3))
# print(cal(4))
# print(cal(5))


##clouser
# a clouser occurs when an innner function remebers values from its enclosing function even after enclosing the fun has finished excution 

# def create_acc(balance):
#     def deposite(amount):
#         nonlocal balance
#         balance +=amount
#         return balance
#     def withdraw(amount):
#         nonlocal balance
#         if amount <= balance:
#             balance-=amount
#             return balance
#         else:
#             return "Insufficient balance"
#     return deposite, withdraw
# deposite, withdraw=create_acc(10000)
# print(deposite(2000))
# print(withdraw(3000))
# print(deposite(500))

#Simple calculator
# def calculator():
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
#     def multi(a,b):
#         return(a*b)
#     def division(a, b):
#         if b==0:
#             return "Cannot divide by zero"
#         return a/b
#     num1=float(input("Enter first number: "))
#     num2=float(input("Enter Second number: "))
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. multiplication")
#     print("4. Division")
#     choice=int(input("Enter your chaoice: "))
#     if choice ==1:
#         result = add(num1,num2)
#     elif choice==2:
#         result=sub(num1,num2)
#     elif choice==3:
#         result=multi(num1,num2)
#     elif choice==4:
#         result=division(num1,num2)
#     else:
#         result="Invalid choice"
#     print("Result:", result)
# calculator()


##Check palindrom
# def palindrome():
#     num=input("enter the value:")
#     rev=num[::-1]
#     if num==rev:
#         return 'it is palindrome'
#     else:
#         return 'it is not a palindrome'
# print(palindrome())
   
##find the factorials
# def factorial():
#     fact=1
#     num=int(input("Enter a number:"))
#     for i in range(1, num+1):
#         fact*=i
#     return fact
# print(factorial())


# check given number is prime or not
# def check_prime():
#     count=0
#     num=int(input("enter a number:"))
#     for i in range(1,  num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         return("Prime number")
        
#     else:
#         return("Not a prime number")
    
# print(check_prime())
            
            
# another way 
# def check_prime(n):
#     if n<2:
#         return "Not prime"
#     for i in range(2,n):
#         if n%i ==0:
#             return "Not Prime"
#     return "Prime"
# num=int(input("Enter a number:"))
# result=check_prime(num)
# print(result)