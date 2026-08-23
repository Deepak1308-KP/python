# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
    
    
# n=int(input("Enter a number:"))
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# if a > b:
#     print(f"greatest number is a {a}")

# elif b > a:
#     print(f"greatest number is b {b}")

# else:
#     print("Both numbers are equal")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a > c:
#     print(f"Greatest number is {a}")

# elif b > a and b > c:
#     print(f"Greatest number is {b}")

# else:
#     print(f"Greatest number is {c}")


# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# num=int(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

#reverse number
# num=int(input("Enter a number: "))
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)    

# num=int(input("Enter a number:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(sum)

# num=int(input("Enter a number:"))
# count=0
# while num>0:
#     digit=num%10
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
# if original==rev:
#     print("It is palindrome")
# else:
#     print("It is not a palindrome")

# num=int(input("Enter a number:"))
# fact=1
# for i in range(1, num+1):
#     fact*=i
# print(fact)

# num = int(input("Enter a number: "))
# largest = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num = num // 10
# print("Greatest digit:", largest)


# num = int(input("Enter a number: "))
# smallest = 9
# while num > 0:
#     digit = num % 10
#     if digit < smallest:
#         smallest = digit
#     num = num // 10
# print("Smallest digit:", smallest)


# num = int(input("Enter a number: "))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     print("Prime number")
# else:
#     print("Not a prime number")


# n = int(input("Enter a number: "))
# original = n
# digits = len(str(n))
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit ** digits
#     n //= 10
# if total == original:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
   
   
##strong number
# num = int(input("Enter a number: "))
# original = num
# total = 0
# while num > 0:
#     digit = num % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     total += fact
#     num //= 10
# if total == original:
#     print("Strong number")
# else:
#     print("Not a strong number")



# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if(sum == n):
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")

# num=int(input("Enter a number:"))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

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


# num = int(input("Enter a number: "))
# even = 0
# odd = 0
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     num = num // 10
# print("Even digits:", even)
# print("Odd digits:", odd)


#Print only the even number 
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


# num=int(input("enter a number:"))
# digit=num%10
# print(digit)

# num = int(input("Enter a number: "))
# while num >= 10:
#     num = num // 10
# print(num)

# num = int(input("Enter a number: "))
# last = num % 10
# while num >= 10:
#     num = num // 10
# first = num
# sum = first + last
# print(sum)
    

# base=int(input("Enter a number: "))
# power=int(input("Enter a number:"))
# result=1
# for i in range(power):
#     result*=base
# print(result)


# n = int(input("Enter a number: "))
# m = int(input("Enter a number: "))
# lcm = max(n, m)
# while True:
#     if lcm % n == 0 and lcm % m == 0:
#         break
#     lcm += 1
# print(lcm)


# a=int(input("Enter a Number: "))
# b=int(input("Enter a Number: "))
# f=min(a,b)
# gcd=1
# for i in range(1,f//2+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print(gcd)