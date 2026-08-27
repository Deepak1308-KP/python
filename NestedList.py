##It is called Matrix
# ns=[[1,2],
#     [3,4],
#     [5,6],
#     [7,8],
#     [9,10]]


# ns=[[1,2],[3,4],[5,6],[7,8],[9,10]]
##For indexing
# print(ns[2][0])
##For A loop
# for i in ns:
#     print(i)
# print(ns)

##Flatten
# ns=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# for i in ns:
#     for j in i:
#         print(j)

# Another method to show in list
# ns=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# ns1=[]
# for i in ns:
#     for j in i:
#         ns1.append(j)
# print(ns1)

# ns=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# ns[2][1]=12
# print(ns)

# ns.pop(3)
# print(ns)

# ns[1].remove(3)

# ns.append(3)
# print(ns)

# ns.clear()
# print(ns)

# del ns[1]
# print(ns)

# ns.reverse()
# print(ns)

# ns1=ns.copy()
# print(ns1)

# ns1=len(ns)
# print(ns1)

##Replace all the negative numbers with zero
# ns=[[1,-2],[3,-4],[5,-6],[7,-8],[9,-10]]
# ns1=[]
# for i in ns:
#     for j in i:
#         if j<0:
#             ns1.append(0)
#         else:
#             ns1.append(j)
# print(ns1)

##In nested only
# ns = [[1,-2],[3,-4],[5,-6],[7,-8],[9,-10]]

# for i in ns:
#     for j in range(len(i)):
#         if i[j] < 0:
#             i[j] = 0

# print(ns)


##Ternary operator
# n=int(input("Enter a number"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

 ##Ternary operator   
##In ternary we can't use elif we can use onested if else;
# n=int(input("Enter a number"))
# result="Even" if n%2==0 else "Odd"
# print(result)


# in normal code
# n=int(input("Enter a number:"))
# if n>0:
#     print("+")
# elif(n<0):
#     print("-")
# else:
#     print("0")
    
# IN Ternary 
# n=int(input("Enter a number:"))
# result ="+" if n>0 else "-" if n<0 else "0"
# print(result)

# ns=[1,2,3,4,5,6,7,8,9]
# j=[]
# for i in ns:
#     j.append(i+1)
# print(j)

#using ternary
# ns=[1,2,3,4,5,6,7,8,9]
# result=[i+1 for i in ns]
# print(result)

# for only even
# ns=[1,2,3,4,5,6,7,8,9]
# result=[i+2 for i in ns if i%2==0]
# print(result)

# names=["deepak","vikesh", "gagan", "suhail"]
# NAME=[word.upper() for word in names]
# print(NAME)

##Generate a list of squares of the first 20 natural number

# natural= [i**2 for i in range(1, 21,1)]
# print(natural)

##Convert a list of temp from celsius to fahrenhait
# c = [0, 10, 20, 30, 40]
# f = [i * 9/5 + 32 if i >= 0 else i for i in c]
# print(f)


#Extract lengths of each word from a sentence split into words.
# s="Python is easy to learn"
# lengths=[len(word) for word in s.split()]
# print(lengths)

#Convert a list of prices from INR to USD (use fixed conversion rate)
# ind=[100, 250, 500]
# usd=95.34
# prices1=[price/usd for price in ind]
# print(prices1)

#Create a list of first letters from each city name.
# cities=["Banglore", "Shivamogga", "Mysore"]
# ls=[city[0] for city in cities]
# print(ls)

#Multiply each element in a list by 5.
# n=[1,2,3,4,5,6,7,8]
# ls=[i*5 for i in n]
# print(ls)

#Convert a list of integers to strings.
# integer=[1,2,3,4,5,6,7]
# ls=[str(i)  for i in integer ]
# print(ls)

#Generate cube values for numbers 1 to 15.
# natural= [i**3 for i in range(1, 16,1)]
# print(natural)

#Convert a list of usernames to lowercase.
# user=["Deepak", "GAGAN", "SUHAIL" ,"VIKESH", "CHEATHAN"]
# ls=[word.lower() for word in user]
# print(ls)

#Strip whitespace from each string in a list.
# s=[" Deepak kp ", " GAGAN aj "]
# ls=[word.strip() for word in s]
# print(ls)

#Add 18% GST to each product price.
# n=[12, 34, 45,56]
# ls=[price+(price*18/100) for price in n]
# print(ls)


#Convert a list of ages into months.
# n=[12, 24, 43, 56]
# ls=[age*12 for age in n]
# print(ls)

#Create a list of ASCII values for each character in a string.
# num=[64,65, 66, 67,68]
# ls=[chr(i)  for i in num]
# print(ls)

# Extract domain names from a list of email IDs.
# emails = [
#     "abc@gmail.com",
#     "user@yahoo.com",
#     "test@outlook.com",
#     "hello@gmail.com"
# ]
# domains = [email.split("@")[1] if "@" in email else "Invalid" for email in emails]
# print(domains)

# Convert a list of weights from kg to grams.
# kg=[2,3,4,5]
# ls=[ i*1000 for i in kg]
# print(ls)

# Generate the length of each sentence in a paragraph.
# n=["Python is easy level language"]
# ls=[len(word) for word in n]
# print(ls)

# Convert a list of tuples into lists.
# ls=[(1,2), (3,4),(5,6)]
# t=[list(t) for t in ls]
# print(t)

# Round off all float values in a list.
# ls=[1.22, 34.545, 56.77, 99.99]
# R=[round(x) for x in ls]
# print(R)

# Reverse each string in a list of strings.
# names=["deepak","vikesh", "gagan", "suhail"]
# R=[x[::-1] for x in names]
# print(R)

# Convert a list of integers into their binary representation.
# ls=[12,34,56,21]
# b=[bin(x) for x in ls]
# print(b)

# Generate the square root of numbers from a list.
# ls=[12.24,2,4,6]
# S=[x**0.5 for x in ls]
# print(S)

# Convert list of product names into title case.
# name=["lays", "kurkure","happy happy"]
# product=[x.title() for x in name]
# print(product)

# Append “_EMP” to each employee ID.
# emp=["Deepak","Vikesh", "Gagan", "Suhail"]
# ID=[x+"_EMP"  for x in emp]
# print(ID)

# Convert a list of booleans into integers.
# value=[True, False]
# V=[int(x) for x in value]
# print(V)

# Add 10 bonus points to each score.
# Score=[220, 330, 44, 90]
# P=[x+10 for x in Score]
# print(P)

# Extract year from a list of date strings (YYYY-MM-DD).
# year=["2025-08-27"]
# E=[x[:4] for x in year]
# print(E)

# Convert list of distances from km to meters.
# KM=[1,2,3,54,350]
# M=[x*1000 for x in KM]
# print(M)

# Prefix “Mr.” to each male customer name.
# names=["Deepak","Vikesh", "Gagan", "Suhail"]
# P=[f"Mr.{x}" for x in names]
# print(P)

# Convert a list of marks to percentages.
# Marks=[441, 350, 600, 500]
# per=[(x/600)*100 for x in Marks]
# print(per)

# Generate absolute values from a list of integers.
# value=[23, -1, 23, -45]
# A=[x if x>=0 else -x for x in value]
# print(A)

# Convert a list of dictionary keys into uppercase.
# data = {"name": "Deepak", "city": "Bangalore"}
# U=[x.upper() for x in data]
# print(U)

# Convert a list of angles from degrees to radians.
# deg=[90, 120, 180]
# ra=[x * 3.14/180 for x in deg]
# print(ra)

# Convert a list of phone numbers to strings.
# num=[6363753781, 8277328017]
# s=[str(x) for x in num]
# print(s)

# Generate powers of 2 for a given list of exponents.
# P=[2,3,4,5]
# E=[2**x for x in P]
# print(E)

# Replace spaces with underscores in filenames.
# Name=["Deepak K P"]
# R=[x.replace(" ","_") for x in Name]
# print(R)

# Convert a list of salaries into annual salaries.
# sal=[25000, 30000, 18000, 50000]
# annual=[x*12 for x in sal]
# print(annual)

# Extract last character of each string.
# SS=["Deepak", "Gagan", "Sachin"]
# E=[x[-1] for x in SS]
# print(E)

# Convert float values into integers.
# F=[24.43, 12,2, 50.00, 99.99]
# I=[int(x) for x in F]
# print(I)

# Create a list of word counts per sentence.
# sentences = ["I love Python", "Python is easy", "I am learning Python"]
# count = [len(x.split()) for x in sentences]
# print(count)

# Capitalize the first letter of each word.
# Name=["deepak", "gagan", "sachin"]
# capital=[x.capitalize() for x in Name]
# print(capital)

# Generate reciprocal values for a list of numbers.
# numbers=[2,3,4,5]
# R=[1/x for x in numbers]
# print(R)


# # Convert a list of byte values to KB.
# B=[1,2,3,4]
# K=[x/1000 for x in B]
# print(K)

# Create a list of string lengths.
# ls=["Mysore", "Shivamogga"]
# S=[len(x) for x in ls]
# print(S)

# Convert numbers into negative values.
# number=[1,2,3,45,67]
# Convert=[x if x<0 else -x for x in number]
# print(Convert)

#Another method
# number=[1,2,3,45,67]
# Convert1= [x * -1 for x in number]
# print(Convert1)

# Remove currency symbol and convert prices to integers.
# Currency=["₹100","₹98.05", "₹75.78"]
# R=[int(float(x[1:])) for x in Currency]
# print(R)

# Convert list of characters into Unicode values.
# char=["A", "B", "C"]
# unicode=[ord(x) for x in char]
# print(unicode)

# Multiply corresponding values using a constant.
# values = [2, 4, 6, 8]
# constant = 5
# result = [x * constant for x in values]
# print(result)

# Generate time in seconds from minutes.
# time=[30, 60, 1]
# second=[x*60 for x in time]
# print(second)

# Convert list of percentages into decimal values.
# percentage=[80, 90, 70,75]
# decimal=[x/100 for x in percentage]
# print(decimal)