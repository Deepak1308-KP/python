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
# if total == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")



#Given Number is a Perfect number or not
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if sum == n:
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