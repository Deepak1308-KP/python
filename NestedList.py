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