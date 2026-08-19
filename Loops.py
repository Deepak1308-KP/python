#while loop
# i=1
# while(i<=100):
#     print("Om namma Shivaya")
#     i+=1
# else:
#     print("Completed")

# i=1
# while(i<=10):
#     print(i)
#     i+=1
# else:
#     print("Completed")
    
    
    
# i=10
# while(i>=1):
#     print(i)
#     i-=1
# else:
#     print("Completed")
    

# a=int(input("Enter a Number:"))
# i=1
# while(i<=10):
#     print(f"{a}*{i}={a*i}")
    # i+=1

# n=int(input("Enter a number"))
# i=1
# while(i<=n):
#     print(i)
#     i+=1


#Sum of natural numbers
# n=int(input("Enter a Number:"))
# a=0
# i=0
# while(i<=n):
#     a+=i
#     i+=1
# print(a)  


#Even Numbers untill 100
# even=int(input("Enter a Number:"))
# i=1
# while(i<=100):
#     if (i%2==0):
#         print(i)
#     i+=1
# else:
#     print("completed")

    
# i=2
# while(i<=100):
#     print(i)
#     i+=2
# else:
#     print("Completed")
    
#Odd Numbers untill 100
# i=1
# while(i<=100):
#     if(i%2!=0):
#         print(i)
#     i+=1
# else:
#     print("Completed")
    
    
# i=1
# while(i<=100):
#     print(i)
#     i+=2
# else:
#     print("Completed")

# #Counts Digits are in number
# even=int(input("Enter a Number:"))
# i=1
# while(i<=10):
#     print(i)
#     i+=1
# else:
#     print("Completd")
#     print(str(i).isdigit())


#Sum of digits of NUmber

#Reverse The string
# n=input("Enter a string:")
# rev=" "
# i=len(n)-1
# while i>=0:
#     rev+=n[i]
#     i-=1
# print(rev)

# n=int(input("Enter a number:"))
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)
    

#Count the Digits in number
# n=int(input("Enter a numbers:"))
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)

#keep taking the input Until  user gives enter 0 Then submit
# n=int(input("Enter a Numbers:"))
# total=0
# while(n!=0):
#     total+=n
#     n=int(input("Enter the number:"))
# print(total)
    
     
# n=int(input("Enter a Factorial number:"))
# i=1
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print(fact)

##################################################################For Loop##################################
# for i in range(1,21,1):
#     print(i)
# else:
#     print("Loop completed")

#Reverse
# for i in range(11,0,-1):
#     print(i)

# for i in range(2, 50, 2):
#     print(i)

# for i in range(1,50,2):
#     print(i)
    

# a=int(input("enter a value"))
# b=int(input("Enter a values"))
# for a in range(1,11,1):
#     print(f'{a}*{b}={a*b}')
    
#Sum of n Natural Numbers
# n=int(input("Enter a Numbers"))
# sum=0
# for a in range(1,n+1,1):
#     sum+=a
# print(sum)


#factorial
# n=int(input("Enter a Numbers:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#count How many Numbers divisible by 3 1to100
# count=0
# for i in range(1,100):
#     if(i%3==0):
#         count=count+1
#         # print(i)
#         print(count)
        

#Squares the number 1 to 10
# for i in range(1,11, 1):
#      print(i**2)

#Sum of only a even numbers 1 to n
# n=int(input("ENter a numbers:"))
# sum=0
# for i in range(1, n+1):
#     if(i%2==0):
#         sum+=i
# print(sum)


#Sum of odd and even 1 to n
# n=int(input("ENter a numbers:"))
# even.sum=0
# odd.sum=0
# for i in range(1, n+1,1):
#     if(i%2==0):
#         even.sum+=i
#     else:
#         odd.sum+=i
# print(even.sum)
# print(odd.sum)
      
#Find the average of Sum From 1 to n
#Find the avg of odd 1 to n

##################################nested FOr Loop################################################  
   
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
#     print()   

####nested While#######
####while used in we not know the range#############
# i=1
# while(i<=10):
#     j=1
#     while(j<=10):
#          print(f"{i}*{j}={i*j}")  
#          j+=1  
#     print()  
#     i+=1
      
