# for i in range(1,5):
#     for j in range(1,5):
#         print("*", end=" ")
#     print()

##Patrens
# n=int(input("Enter a number:"))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print("*", end=" ")
#     print()


# n= int(input("ENter a value: "))
# for row in range(1, n+1):
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()

# n=int(input("Enter a Nuber:"))
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()


# n=int(input("Enter a number:"))
# for row in range(1, n+1):
#     for col in range(1,row+1):
#         print("#", end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         print("#", end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         print(col, end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(col, end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(n):
#     for col in range(n,row, -1):
#         print(col, end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(n,0,-1):
#     for col in range(n,row-1, -1):
#         print(col, end=" ")
#     print()


##         *
#     **
#    ***
#   ****
#  *****

# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for space in range(n-row):
#         print (" ", end=" ")

#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for space in range(n-row):
#         print (" ", end=" ")

#     for col in range(1, row+1):
#         print(row, end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for space in range(n-row):
#         print (" ", end=" ")

#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()

##Reverse need to print

# n=int(input("Enter a value:"))
# for row in range(n,0,-1):
#     for sapce in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()

# n=int(input("Enter a value:"))
# for row in range(n,0,-1):
#     for sapce in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print(row, end=" ")
#     print()

# n=int(input("Enter a value:"))
# for row in range(n,0,-1):
#     for sapce in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()


# Traingle of right
#
##
###
####
##
#


# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()
# for row in range(n-1,0,-1):
#     for col in range(1,row+1):
#         print("*",end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for col in range(1, row+1):
#         print(row, end=" ")
#     print()
# for row in range(n-1,0,-1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()
# for row in range(n-1,0,-1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()


##Triangle And reverse ones


# n=int(input("Enter a Number:"))
# for row in range(n):
#     for space in range(1, n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(n):
#     for space in range(1, n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print(chr(64+col), end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(n):
#     for space in range(1, n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(n):
#     for space in range(1, n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print(row, end=" ")
#     print()


#########reversed Traingle##############

# n=int(input("Enter a Number:"))
# for row in range(n,0,-1):
#     for space in range(1, n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()

# n = int(input("Enter a Number:"))
# for row in range(n, 0, -1):
#     for space in range(1, n - row):
#         print(" ", end="")
#     for col in range(1, row + 1):
#         print(col, end=" ")
#     print()


##########revesed Number Triangle##############
# n = int(input("Enter a Number:"))
# for row in range(n, 0, -1):
#     for space in range(1, n - row):
#         print(" ", end="")
#     for col in range(1, row + 1):
#         print(row, end=" ")
#     print()







###################################Printing a Char In Trianle#############################
# n=int(input("Enter a Number: "))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print(chr(64+col),end=" ")
#     print()
    
# n=int(input("Enter a Number: "))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print(chr(64+row),end=" ")
#     print()

# n=int(input("Enter a Number: "))
# for row in range(1, n+1):
#     for col in range(1, row+1):
#         print(chr(64+col),end=" ")
#     print()

# n=int(input("Enter a Number: "))
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(chr(64+row),end=" ")
#     print()



#        1
#       12
#      121
#     1212
#    12121

# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end=" ")
#     for col in range(1,row+1):
#         if(col%2!=0):
#             print(1,end=" ")
#         else:
#             print(2, end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end="")
#     for col in range( 1, row+1):
#         print(col, end=" ")
#     print()

# n=int(input("Enter a Number:"))
# for row in range(1,n+1):
#     for space in range( n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print(row, end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         if(col%2!=0):
#             print(1,end=" ")
#         else:
#             print(0, end=" ")
#     print()
    
# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end="")
#     for col in range(1, row+1):
#         if(row%2!=0):
#             print(1,end=" ")
#         else:
#             print(0, end=" ")
#     print()




