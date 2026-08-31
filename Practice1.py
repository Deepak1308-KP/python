# n=int(input("Enter a NUmber: "))
# count=0
# for i in range(1, n+1):
#     if n%i==0:
#      count+=1
# if count==2:
#     print("Prime ")
# else:
#     print("Not a prime")

# num=int(input("Enter a number: "))
# sum=0
# for i in range (1, num):
#     if num%i==0:
#         sum += i
# if sum==num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")
    
# n=int(input("Enter a number:"))
# fact=1
# for i in range(1, n+1):
#     fact*=i
# print(fact)

# leap=int(input("Enter a year: "))
# if (leap%4==0 and leap%100!=0) or leap%400==0:
#     print("Leap year")
# else:
#     print("Not a leap") 

# num=int(input("Enter a number:"))
# sum=0
# while num>0:
#     digits=num%10
#     sum+=digits
#     num=num//10
# print(sum)

# num=int(input("Enter a number:"))
# count=0
# while num>0:
#     digits=num%10
#     count+=1
#     num=num//10
# print(count)

# num=int(input("Enter a number:"))
# original=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if rev==original:
#     print("Palindrome")
# else:
#     print("not a palindrome")
    

# num=int(input("Enter a number:"))
# original=num
# temp=0
# digits=len(str(num))
# while num>0:
#     single=num%10
#     temp+=single**digits
#     num//=10
# if temp==original:
#     print("Amstrong number")
# else:
#     print("not Amstrong")
    
    
# num=int(input("Enter a number:"))
# original=num
# result=0
# while num>0:
#     digits=num%10
#     fact=1
#     for i in range(1, digits+1):
#         fact*=i
#     result+=fact
#     num=num//10
# if result==original:
#     print("Strong number")
# else:
#     print("Not a strong no")
        
# num=int(input("Enter a number:"))
# rev=0
# while num>0:
#     digits=num%10
#     rev=rev*10+digits
#     num=num//10
# print(rev)

# num= int(input("ENter a number:"))
# largest=0
# while num>0:
#     digits=num%10
#     if digits>largest:
#         largest=digits
#     num=num//10
# print(largest)

# num=int(input("Enter a number:"))
# smallest=9
# while num>0:
#     digit=num%10
#     if digit<smallest:
#         smallest=digit
#     num=num//10
# print(smallest)
        
# num=int(input("Enter a number:"))
# a=0
# b=1
# while a<num:
#     c=a+b
#     a=b
#     b=c
# if a==num:
#     print("fibbonacci")
# else:
#     print("not fibbonacci")

# num=int(input("Enter a number:"))
# even=0
# odd=0
# while num>0:
#     digits=num%10
#     if digits%2==0:
#         even+=1
#     else:
#         odd+=1
#     num=num//10
# print(even)
# print(odd)

# num=int(input("Enter a number:"))
# pos=1
# even=0
# while num>0:
#     digit=num%10
#     if digit%2==0:
#         even=digit*pos+even
#         pos*=10
#     num=num//10
# print(even)

# num=int(input("Enter a number:"))
# last=num%10
# while num>=10:
#    num=num//10
# first=num
# sum=last+first
# print(sum)
    
# power=int(input("Entr a number:"))
# base=int(input("Enter a number:"))
# result=1
# for i in range(power):
#     result*=base
# print(result)

# a=int(input("Enter a numbver;"))
# b=int(input("Enter a number"))
# lcm=max(a,b)
# while True:
#    if lcm % a == 0 and lcm % b == 0:
#        break
#    lcm+=1
# print(lcm)


# a = int(input("Enter a Number: "))
# b = int(input("Enter a Number: "))
# f = min(a, b)
# gcd = 1
# for i in range(1, f + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print(gcd)



##PAtterens
# n=int(input("Enter a number:"))
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

##Reverse
# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# n=int(input("Enter a number:"))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end=" ")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


# n=int(input("Enter a number:"))
# for i in range(n):
#     for j in range(n, i,-1):
#         print(j, end=" ")
#     print()

# n=int(input("ENter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

#REverse    
# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     for space in range(n-i):
#         print(" ", end=" ")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

#Triangle
# n=int(input("ENter a number: "))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# n=int(input("Enter a number:"))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end=" ")
#     for j in range(2*i-1):
#         print("*", end=" ")
#     print()

# n=int(input("ENter a number: "))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print(chr(64+j), end=" ")
#     print()


# n=int(input("enter a number:"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if (j==1 or i==j or i==n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n=int(input('Enter a number:'))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         if i==j or j==1 or i==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n=int(input("Enter a number:"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==1 or j==1 or i==n or j==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     for j in range(1, 2*n):
#         if i==n or j==n-i+1 or j==n+i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
    
# n=int(input("Enter a number:"))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         if i==j or j==1 or i==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n=int(input("Enter a number:"))
# for i in range(1, n+1):
#     for space in range(n-i):
#         print(" ", end=" ")
#     for j in range(1,i+1):
#         if i==j or j==1 or i==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n=int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==n or i==1 or j==n or j==1 or j==n-i+1 or i==j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# a = [1, 2, 3, 4, 5, 6, 67, 78, 98]
# first = a[0]
# second = a[0]
# third = a[0]
# for value in a:
#     if value > first:
#         third = second
#         second = first
#         first = value
#     elif value > second:
#         third = second
#         second = value
#     elif value > third:
#         third = value
# print(third)


