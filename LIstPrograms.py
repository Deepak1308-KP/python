
# lit=['Shivamogga',12, 13,34, 54, 12, 'python', 'java', 'abcd', 'deepak']
# for value in lit:
#     print(value)

# z=[12, 13,34, 54, 12, 'python', 'deepak']
# for value in z:
#     print(value)
    
# xyz=['Deepak', 'Python', 'the', 'dots','by', 'dashed']
# n=input("Enter a name:") 
# for i in  range(len(xyz)):
#     if n==xyz[i]:
#         print("It is there in List")     
#         break
# else:
#     print("Is not there")

##Find the  length of a list without using len function
# l=[12, 21, 32, 43, 56, 'Deepak', 'Python', 'Da', 'sql']
# count=0
# for value in l:
#     count+=1
# print(count)

# Create a number List and sum of the no 
# n=[1, 2, 3, 4, 5,6, 7]
# sum=0
# for value in n:
#     sum+=value
# print(sum)

#Without using len fun avg of given list
# n=[1, 2, 3, 4, 5, 6,7]
# count=0
# sum=0
# for value in n:
#     sum+=value
#     count+=1
# avg=sum/count
# print(avg)


# Find the largest Element without using max
# n=[1,2,3, 4,5,6, 7, 10]
# large=1
# for value in n:
#     if value > large:
#         large=value
# print(large)
    
##Sum of only even numbers from a list
# n=[1,2,3,4,5,6,7,8,9,12,10]
# sum=0
# for value in n:
#     if value%2==0:
#         sum+=value
# print(sum)


##SUM of only odd numbers from list
# n=[1,2,3,4,5,6,7,8,9,10,11]
# sum=0
# for ns in n:
#     if ns%2!=0:
#         sum+=ns
# print(sum)

##Add Element at the end without using append
# xyz=['Deepak', 'Python', 'the', 'dots','by', 'dashed']
# n=input("Enter a One Element: ")
# xyz.extend(n)
# print(xyz)

# Using loop
# xyz=['Deepak', 'Python', 'the', 'dots','by', 'dashed']
# n=input("Enter a Element:")
# a=[]
# for values in xyz:
#      a += [values]
# a += [n]
# print(a)

##Remove a particular element from the list without useing remove
# xyz=[1,2,4,'Deepak', 'Python', 'the', 'dots','by', 'dashed']
# n=input("Enter a removing element:")
# abc=[]
# target=n
# for value in xyz:
#     if value==target:
#         del value
#     else:
#         abc.append(value)
#         print(abc)
# print()
        
        
##Remove Duplicate FRom the list
# xyz=[1, 2, 3,'Deepak', 'Python', 'the','the', 'dots','by','by','dashed']
# # n=input("Enter a  ")
# a=[]
# for value in xyz:
#     if value not in a:
#         a.append(value)
# print(a)


##FInd the Second largest in the list
# a=[1,2,3,4,5,6,67,78,98]
# max=a[0]
# secondmax=a[0]
# for i in a:
#     if i > max:
#         secondmax=max
#         max=i
# print(secondmax)
    

##Find the Second smallest
# a = [0,1, 2, 3, 4, 5, 6, 67, 78, 98]
# small = a[0]
# secondsmall = a[1]
# if secondsmall < small:
#     small, secondsmall = secondsmall, small
# for value in a[2:]:
#     if value < small:
#         secondsmall = small
#         small = value
#     elif value < secondsmall and value != small:
#         secondsmall = value
# print(secondsmall)

        
# Find the 3rd largest
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
       
        
##Separate a odd and even num from a list
# a=[1,2,3,4,5,6,67,78,98]
# even=[]
# odd=[]
# for value in a:
#     if value%2==0:
#         even.append(value)
#     else:
#         odd.append(value)
# print(even)
# print(odd)


##Separate common elements btwn 2 list
# a=[1,2,3,4,5,6,67,78,98]
# b=[1,4,5,6,7,8,9,10]
# c=[]
# for value in a:
#         if value in b:
#             c.append(value)
# print(c)
        

##Find the frequency of each element
# a=[1,2,2,3,4,5,6,6,7,8,9,2,1,1]
# dict={}
# for value in a:
#     if value in dict:
#         dict[value]+=1
#     else:
#         dict[value]=1
# print(dict) 


# Move all  the zeros to a end
# a=[1,0,2,0,3,0,4,0,5,0]
# result=[]
# b=[]
# for i in a:
#     if i!=0:
#         result.append(i)
# for values in a:
#     if values==0:
#         result.append(values)
# print(result)


##Another method
# a=[1,0,2,0,3,0,4,0,5,0]
# dict=[]
# zero=0
# for i in a:
#     if i==0:
#         zero+=1
#     else:
#         dict.append(i)
# for j in range(zero):
#     dict.append(0)
# print(dict)

##write a prgm to rotate a list by one postion to the right 
# a=[1,2,3,4,5,6,7,8]
# pos=4
# n=[]
# right=[]
# for i in range(len(a)):
#     if i< pos:
#         right.append(a[i])
#     else:
#         n.append(a[i])
# n.extend(right)
# print(n)

        
# a=[1,2,3,4,5,6,7,8]
# k=int(input("Enter index to rotate:"))
# for j in range(k):
#     last=a[-1]
# for i in range(len(a)-1,0,-1):
#     a[i]=a[i-1]
# a[0]=last
# print(a)


# Check the given list is sorted or not
# a=[2,1,3,5,4,6,8,7]
# b=a.copy()
# c=a.copy()
# c.sort()
# if b==c:
#     print("It is a sorted:")
# else:
#     print("Not sorted")

#another method
# a=[2,1,3,5,4,6,8,7]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]>a[j]:
#             print("It ia not sorted")
#             break
#     if a[i]>a[j]:
#         break
# else:
#     print("Sorted")
