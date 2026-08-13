# n=int(input("Enter the number: "))
# if(n%2==0):
#     print(f"Given number {n} is even Number ")
# else:
#     print(f"Given number {n} is odd Number")

# num=int(input("Enter the NUmber:"))
# if(n<0):
#     print(f"the given Number {num} is negative")
# else:
#     print(f"Given number is the positive")

# n1=int(input("Enter the Number:"))
# n2=int(input("Enter the Number:"))
# if(n1<n2):
#     print(f"n1 is samller than {n2} number")
# elif(n2>n1):
#     print(f"n2 is greater than {n1}")

# leap=int(input("Enter a year:"))
# if(leap%400==0 or(leap%4==0 and leap%100!=0)):
#     print(f"{leap} is a leap year")
# else:
#     print(f"{leap} is  Not a leap year") 


#check The person is eligible to vote or not
# age=int(input("enter age:"))
# if(age>=18):
#     print(f"your {age} is eligibe to vote")
# else:
#     print(f"your {age} is  not eligibe to vote")
    
# num=int(input("Enter a number:"))
# if(num%3==0):
#  print(f"the {num} is multiply by 3")
# else:
#     print(f"the{num} is not multiple by 3")
    

# alpha=input("enter a charcter:").upper()
# if(alpha in "aeiouAEIOU"):
#     print(f"the {alpha} is vowel")   
# else:
#     print(f" the {alpha} is consonent") 


# n=int(input("Enter the number:"))
# if(n>0 and  n<=100):
#     print(f"the {n} is between in 1-100")
# else:
#     print(f"the {n} is not betwen in 1-100")


# n=input("Enter a word:")
# if n ==n[::-1]:
#     print(n)
#     print("The Word Is Palindrome.")
# else:
#     print("The Word Is not a Palindrome.")


############### ELIFF ##############

# n=int(input("Enter Your Number:"))
# if(n>0):
#     print("positive")
# elif(n<0):
#     print("Negative")
# else:
#     print(f"{n}is zero or non zero element")


# gettingmarks=int(input("Enter your Total Marks:"))
# totalmarks=int(input("Enter Total marks:"))
# percentage=(gettingmarks/totalmarks)*100
# if (percentage < 60):
#     print(f"{percentage} Your percentage grade is C")
# elif (percentage < 70):
#     print(f"{percentage} Your percentage grade is B")
# elif (percentage < 80):
#     print(f"{percentage} Your percentage grade is B++")
# elif (percentage < 90):
#     print(f"{percentage} Your percentage grade is A")
# else:
#     print(f"{percentage}  Your percentage grade is A++")
    

# n=int(input("Enter your Number: "))
# if(0< n <=9):
#     print(f"{n} given number is single digit")
# elif(9 < n <100):
#     print(f"{n} is the two digit number")
# elif(99<n <1000):
#     print(f"{n} is the Three digit number")
# else:
#     print(f"{n} id gerater than three digit")
    
    
#Check the given number is diveded by 3 and 5 and both
    
# num=int(input("enter Your number:"))
# if(num%5==0 and num%3==0):
#     print(f"{num} is the divided by two numbers")
# elif(num%3==0):
#     print(f"{num}The number is diveded by Three")
# elif(num%5==0):
#     print(f"{num} is the divided by Five")

# else:
#     print("Enter a correct number")


# Given charcter is case or lower
# ch=input("enter a character:")
# if(ch.isupper()):
#     print("Enterd char is in Upper case")
# elif(ch.islower()):
#     print("Enterd char is in Lower case")
# else:
#     print("Enter a char not number")
    

# ch=input("enter the character")
# if(ch>="A" and ch< "Z"):
#     print("The word in uppercase")
# elif(ch>="a" and ch< "z"):
#      print("The word in lower")
# else:
#     print("other")
         

# check the given date is valid or not
date = int(input("Enter a date: "))
month = int(input("Enter a Month: "))
year = int(input("Enter a Year: "))

if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    leap = True
else:
    leap = False

if(month < 1 or month > 12):
    print("Invalid Month")

elif(date < 1 or date > 31):
    print("Invalid Date")

elif month in [4, 6, 9, 11]:
    if date <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")

elif month in [1, 3, 5, 7, 8, 10, 12]:
    if date <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")

elif month == 2:
    if leap == True and date <= 29:
        print("Valid Date")
    elif leap == False and date <= 28:
        print("Valid Date")
    else:
        print("Invalid Date")
    

    


# simple caluculator
# operator=input("Enter operator")
# a=int(input("Enter a Number:"))
# b=int(input("Enter a Number:"))
# if(operator=="+"):
#     print(a+b)
# if(operator=="-"):
#     print(a-b)
# elif(operator=="*"):
#     print(a*b)
# elif(operator=="%"):
#     print(a%b)
# elif (operator=="/"):
#     print(a/b)
# else:
#     print(fcasdbmjnbsa)


