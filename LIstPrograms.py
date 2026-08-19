
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
n=[1,2,3,4,5,6,7,8,9,10,11]
sum=0
for ns in n:
    if ns%2!=0:
        sum+=ns
print(sum)
