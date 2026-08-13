#  *
#  * *
#  *   *
#  *     *
#  * * * * *


# n=int(input("Enter a Number: "))
# for row in range(1, n+1):
#     for col in range(1, row+1):
#         if(col==1 or col==row or row==n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

##reversed

# n=int(input("Enter a Number: "))
# for row in range(n,0,-1):
#     for col in range(1, row+1):
#         if(col==1 or col==row or row==n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n=int(input("Enter a Number:"))
# for row in range(n):
#     for col in range(n):
#         if(col==0 or row==0 or col==n-row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
        
       




#         *
#       * *
#     *   *
#   *     *
# * * * * * 
   
# n=int(input("Enter a Number: "))
# for row in range(1, n+1):
#     for space in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         if(col==1 or col==row or row==n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
  
##Reversed   
    
# n=int(input("Enter a Number: "))
# for row in range(n,0,-1):
#     for space in range(n-row):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         if(col==1 or col==row or row==n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# n=int(input("Enter a Values:"))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if(row==1 or row==n or col==1 or col==n):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#      *
#    *   *
#   *     *
#  *       *
# * * * * * *


# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for col in range(1, 2*n):
#         if( row==n or col==n-row+1 or col==n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
 
 
#Reversed Triangle
    
# n=int(input("Enter a Number:"))
# for row in range(n,0,-1):
#     for col in range(1, 2*n):
#         if( row==n or col==n-row+1 or col==n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



### Hallow Diamond With the Middle Line Star

# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for col in range(1, 2*n):
#         if( row==n or col==n-row+1 or col==n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for row in range(n,0,-1):
#     for col in range(1, 2*n):
#         if( col==n-row+1 or col==n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
    
### Hallow Diamond With OUt the Middle Line Star
# n=int(input("Enter a Number:"))
# for row in range(1, n+1):
#     for col in range(1, 2*n):
#         if(col==n-row+1 or col==n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for row in range(n,0,-1):
#     for col in range(1, 2*n):
#         if( col==n-row+1 or col==n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



#Square Inside Mini Square Using Diagnol

# * * * * * * * * * * 
# * *             * * 
# *   *         *   * 
# *     *     *     * 
# *       * *       * 
# *       * *       * 
# *     *     *     * 
# *   *         *   * 
# * *             * * 
# * * * * * * * * * *  

# n=int(input("Enter a Values:"))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if(row==1 or row==n or col==1 or col==n or col==n-row+1 or col==row):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n=int(input("Enter a Number: "))
# for row in range(n):
#     for col in range(row,n):
#         print(" ", end=" ")
#     for col in range (row+1):
#         print("*", end=" ")
#     for col in range (row):
#         print("*", end=" ")
#     print()
# for row in range(n):
#     for col in range(row+1):
#         print(" ",end=" ")
#     for col in range(row,n-1):
#         print("*",end=" ")
#     for col in range(row,n):
#         print("*",end=" ")
#     print()


