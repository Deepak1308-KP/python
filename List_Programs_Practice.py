# 1.	Create and print — Create a list of 5 fruits and print it.
# List=["Deepak", 22, "B.E", "Shivamogga", 2004,76.77]
# print(List)

# 2.	Access elements — Given fruits = ["apple", "banana", "cherry", "date", "fig"],
# print the first and last elements.
# fruits = ["apple", "banana", "cherry", "date", "fig"]
# print(fruits[0])
# print(fruits[-1])

# 3.	Length of a list — Write a program to find the number of elements in a list.
# fruits = ["apple", "banana", "cherry", "date", "fig"]
# print(len(fruits))

# 4.	Append and remove — Add "grape" to the list, then remove "banana".
# fruits = ["apple", "banana", "cherry", "date", "fig"]
# fruits.append("grape")
# fruits.remove("banana")
# print(fruits)

# 5.	Sum of numbers — Given a list of numbers, calculate their sum without using sum().
# num=[1,2,3,4,5,6,7,8,9]
# sum=0
# for value in num:
#     sum+=value
# print(sum)

# 6.	Find max/min — Find the largest and smallest number in a list without using built-in max()/min().
# num = [1,2,3,4,5,6,7,8,9,12,14,16]
# minimum = num[0]
# maximum = num[0]
# for i in num:
#     if i > maximum:
#         maximum = i
#     if i < minimum:
#         minimum = i
# print("Max:", maximum)
# print("Min:", minimum)

# 7.	Reverse a list — Reverse a list without using reverse() or slicing.
# num = [1,2,3,4,5,6,7,8,9,12,14,16]
# reverse = []
# for i in range(len(num)-1, -1, -1):
#     reverse.append(num[i])
# print(reverse)
        
# 8.	Count occurrences — Count how many times a given value appears in a list.
# num = [1,2,1,3,4,5,6,1,7,8]
# search = int(input("Enter a number: "))
# count = 0
# for value in num:
#     if value == search:
#         count += 1
# print("Occurrences:", count)

# 9.	Check membership — Check if a given item exists in the list using in.
# fruits = ["Apple", "Mango", "Jackfruit","watermelon", "Banana"]
# search = input("Enter a item name: ")
# if search in fruits:
#     print("This is there in given list")
# else:
#     print("Not is there in list")

# 10.	Slicing practice — Given a list of 10 numbers,
# print the first 3, last 3, and every alternate element.
# num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(num[0:3])
# print(num[0:13:2])
# print(num[-3:])


# 11.	List concatenation — Combine two lists into one.
# list=[1,2,4,5,6]
# list2=[3,7,8,9,10]
# ls=list+list2
# print(ls)

# 12.	Sort a list — Sort a list of numbers in ascending and descending order.
# list1=[9,87,6,5,4,3]
# list2=[1,51,62,39,98]
# list1.sort()
# list2.sort(reverse=True)
# print(list1, list2)

# 13.	Copy a list — Copy a list so changes to the copy don't affect the original.
# list=[1,2,3,4,5,6,7]
# list1=list.copy()
# print(list, list1)

# 14.	Sum of even numbers — Given a list of numbers, print only the even ones.
# list=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in list:
#     if i%2==0:
#         print(i)
#         sum+=i
# print(sum)

# 15.	Convert string to list — Convert a string into a list of its characters.
# name="Deepak"
# list=[]
# for i in name:
#     list.append(i)
# print(list)

# Intermediate (Medium)

# 16.	Remove duplicates — Remove duplicate elements from a list while preserving order.
# list=[1,2,3,4,5,6,7,2,3,4,5,6,7]
# duplicate=[]
# for i in list:
#     if i not in duplicate:
#         duplicate.append(i)
# print(duplicate)

# 17.	List of lists (matrix) — Given a 3x3 matrix (list of lists), print its transpose.
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# transpose = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(matrix[j][i])
#     transpose.append(row)
# print(transpose)

# 18.	Flatten a nested list — Convert [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6].
# list=[[1,2],[3,4],[5,6]]
# for i in list:
#     for j in i:
#         print(j)

# Another Way
# list=[[1,2],[3,4],[5,6]]
# flat=[]
# for i in list:
#     for j in i:
#         flat.append(j)
# print(flat)

# 19.	Second largest element — Find the second largest number in a list without sorting.
# list=[12,100,99,89,56]
# largest=list[0]
# secondmax=list[0]
# for i in list:
#     if i>largest:
#         secondmax=largest
#         largest=i
#     elif i>secondmax:
#         secondmax=i
# print(secondmax)

# 20.	List comprehension basics — Use a list comprehension to generate squares of numbers from 1 to 20.
# square=[x**2 for x in range(1,21)]
# print(square)

# 21.	Filter with comprehension — Use list comprehension to extract all words longer than 4 letters from a list.
# words=["Deepak", "Vikesh" , "Book", "Gagan", "Note","Boss"]
# result=[x for x in words if len(x)>4 ]
# print(result)

# 22.	Merge and sort — Merge two sorted lists into a single sorted list without using sorted().
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# result = []
# for i in list1:
#     result.append(i)
# for i in list2:
#     result.append(i)
# for i in range(len(result)):
#     for j in range(i + 1, len(result)):
#         if result[i] > result[j]:
#             result[i], result[j] = result[j], result[i]
# print(result)

# 23.	Rotate a list — Rotate a list left or right by n positions.
# list1 = [1, 2, 3, 4, 5]
# n = 2
# result = list1[n:] + list1[:n]
# print(result)

# 24.	Find common elements — Given two lists, find the elements common to both (without using set).
# list=[1,2,3,4,5,6,7,8]
# list1=[1,2,3,4,5]
# result=[]
# for i in list:
#     for j in list1:
#         if i==j:
#             result.append(i)
# print(result)

# 25.	Frequency counter — Build a dictionary that counts the frequency of each element in a list.
# list=[1,2,2,3,4,5,6,6,7,8,9,2,1,1]
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# 26.	Chunking a list — Split a list into chunks of size n.
# list1 = [1,2,2,3,4,5,6,6,7,8,9,2,1,1]
# n = 2
# result = []
# temp = []
# for i in list1:
#     temp.append(i)
#     if len(temp) == n:
#         result.append(temp)
#         temp = []
# if temp:
#     result.append(temp)
# print(result)

# 27.	Zip two lists — Combine two lists into a dictionary using zip().
# list=["name", "Roll_no","class", "Native"]
# list1=["Deepak", 29, 12, "Shivamogga"]
# dic=dict(zip(list,list1))
# print(dic)

# 28.	Swap elements — Swap the first and last elements of a list.
# 29.	Palindrome check on list — Check if a list reads the same forward and backward.
# 30.	Custom sort — Sort a list of tuples/dictionaries by a specific key (e.g., sort students by marks).
# 31.	Running sum — Given a list, return a new list where each element is the cumulative sum up to that index.
# 32.	Remove specific type — Remove all strings from a mixed list (containing ints, strings, floats).
# 33.	Find missing number — Given a list of numbers from 1 to n with one missing, find the missing number.
# 34.	List rotation detection — Check if one list is a rotated version of another.
# 35.	Group anagrams — Given a list of words, group anagrams together.


