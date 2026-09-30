# Recursion
# Recursion is when a function calls itself.
# Every recursive function must have two parts:

# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument

# def printnum(Lnum, nno):
#     if Lnum>nno:
#         return
#     print(Lnum)
#     printnum(Lnum+1, nno)
# printnum(1,5)

# def printnum(Lnum, nno):
#     if Lnum>nno:
#         return
#     printnum(Lnum+1, nno)
#     print(Lnum)
# printnum(1,5)

##Sum of array elements
# def sum_array(arr):
#     if not arr:
#         return 0
#     return arr[0]+sum_array(arr[1:])
# arr=[1,2,3,4]
# result=sum_array(arr)
# print(result)

# reverse the string 
# def reverseString(a):
    
## sum of digits from the given number
# def sumofnum(n):
#     if n==0:
#         return 0
#     return n%10+sumofnum(n//10)
# n=int(input("Enter the number:"))
# print("Sum of digits:",sumofnum(n))

#find the factorial of a nth number
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# n=int(input("Enter the number:"))
# print(factorial(n))

##check given string is palindrome or not
# def palindrome(s):
#     if len(s)<=1:
#         return True
#     elif s[0]!=s[-1]:
#         return False
#     return palindrome(s[1:-1])
# s=input("Enter the string:")
# if palindrome(s):
#     print("palindrome")
# else:   
#     print("not a palindrome")

# Fibbonacci series
# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1)+fibonacci(n-2)
# n=int(input("Enter the number:"))
# for i in range(n):
#     print(fibonacci(i), end=" ")

##Count the number by given digit
# def countdigit(n):
#     if n==0:
#         return 0
#     return 1+countdigit(n//10)  
# n=int(input("Enter the number:"))
# print("Count of digits:",countdigit(n))