#check the smallest digit from the given number
# n = int(input("Enter a number: "))
# small = 9
# while n > 0:
#     digit = n % 10
#     if digit < small:
#         small = digit
#     n = n // 10
# print(small)

##another way of min
# n = input("Enter a number: ")
# small = int(min(n))
# print(small)

# Count how many odd and how many even in given Number
# n=int(input("Enter a numbers:"))
# odd=0
# even=0
# while n>0:
#     digit=n%10
#     n = n // 10
#     if(digit%2==0):
#         even+=1
#     else:
#         odd+=1 
# print(even)
# print(odd)
     
##Print the last digit of the given number
# n=int(input("Enter a number:"))
# digit=n%10
# print(digit)

#Calculate the sum of frist and last digit of a given number
# n = int(input("Enter a number: "))
# last_digit = n % 10
# while n >= 10:
#     n = n // 10
# first_digit = n
# sum = first_digit + last_digit
# print(sum)

#Another Way
# n = input("Enter a number: ")
# lastdigit = int(n[-1])
# frstdigit = int(n[0])
# sum = frstdigit + lastdigit
# print(sum)



#Find the given digit is amstrong number or not
# n = int(input("Enter a number: "))
# digits = len(str(n))
# temp = n
# total = 0
# while temp > 0:
#     rem = temp % 10
#     total += rem ** digits
#     temp //= 10
# if(total == n):
#     print("Armstrong")
# else:
#     print("Not Armstrong")


#Given Number is a Perfect number or not
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if(sum == n):
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")


#Check the Prime 
# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

    
#Print the prime number 1-100
# for n in range(1, 101):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print(n)

##Find the power without using exponential
# power=int(input("Enter a Number: "))
# base=int(input("Enter a NUmber:"))
# result=1
# for i in range(power):
#     result*=base
# print(result)

##LCM List col multiple
# n=int(input("Enter a Number:"))
# m=int(input("Enter a number:"))
# lcm=max(n,m)
# while True:
#     if lcm%n==0 and lcm%m==0:
#         break
#     lcm+=1
# print(lcm)


##GCD
# a=int(input("Enter a Number: "))
# b=int(input("Enter a Number: "))
# f=min(a,b)
# gcd=1
# for i in range(1,f//2+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print(gcd)

#Check The given number belongs to fibonacci series
# n=int(input("Enter a number:"))
# a=0
# b=1
# while a<n:
#     c=a+b
#     a=b
#     b=c
# if a==n:
#     print("it is belong's to fibonacci")
# else:
#     print("it is not belongs to fibonacci")


###Palindrome Number
# n = int(input("Enter a number: "))
# a = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if rev == a:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")


##Given Number is Strong or not 
# n = int(input("Enter a number: "))
# a = n
# sum = 0
# while n > 0:
#     digit = n % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     sum += fact
#     n = n // 10
# if sum == a:
#     print("Strong number")
# else:
#     print("Not a strong number")



##Print only the even number 
# n=int(input("Enter a number: "))
# even_no=0
# place=1
# while n>0:
#     digits=n%10
#     if(digits%2==0):
#         even_no=digits*place+even_no
#         place*=10
#     n=n//10
# print(even_no)


##Prints only the odd nnumber
# n=int(input("Enter a numbers: "))
# odd_no=0
# place=1
# while n>0:
#     digits=n%10
#     if digits%2!=0:
#         odd_no=digits*place+odd_no
#         place*=10
#     n=n//10
# print(odd_no)

##Separate the even numbers and odd number from given integer
# n=int(input("Enter a number:"))
# even_no=0
# odd=0
# pos=1
# place=1
# while n>0:
#     digits=n%10
#     if(digits%2==0):
#           even_no=digits*place+even_no
#           place*=10
#     else:
#         odd=digits*pos+odd
#         pos*=10
#     n=n//10
# print(even_no)
# print(odd)


# n=int(input("Enter a number: "))
# even=[]
# odd=[]
# while n>0:
#     digits=n%10
#     if(digits%2==0):
#         even.append(digits)
#     else:
#         odd.append(digits)
#     n=n//10
# print(odd)
# print(even)
        
        
        
          
        
          
    