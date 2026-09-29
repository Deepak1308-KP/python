# Recursion
# Recursion is when a function calls itself.
# Every recursive function must have two parts:

# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument

# def printnum(Lnum, nno):
#     if Lnum>nno:
#         return
#     print(Lnum)
#     printnum(Lnum+1, nno)
# printnum(1,5)

# def printnum(Lnum, nno):
#     if Lnum>nno:
#         return
#     printnum(Lnum+1, nno)
#     print(Lnum)
# printnum(1,5)

##Sum of array elements
# def sum_array(arr):
#     if not arr:
#         return 0
#     return arr[0]+sum_array(arr[1:])
# arr=[1,2,3,4]
# result=sum_array(arr)
# print(result)

