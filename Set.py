##set is unoreded collection of data or items, mutable and 
# it will not allows a duplicate and it store multiple values or data or variables 

# st={1,2,3,"Deepak", "KP", "DKP"}
# print(st)

##hash function is used for find the hash value of particular element
# st={1,2,3,"Deepak", "KP", "DKP"}
# for i in st:
#     print(hash(i),"====>",i)

# st={1,2,3,"Deepak", "KP", "DKP"}
# st1={"No", "Yes", "Java"}

#update/add only one element
# st.add("python")

# it will updated 2sets
# st.update(st1)

#it will remove particular element
# st.remove(1)

# t will remove any element
# st.pop()

#it will clear all element
# st.clear()
# print(st)


##EMpty set created by using
# st=set()
# print(st)

# st=set()
# for i in range(1,3):
#     st.add(i)
# print(st)

# se = set()
# n = int(input("How many words? "))
# for i in range(n):
#     word = input("Enter a word: ")
#     se.add(word)
# print(se)

##Find the no of unique  elements,set
# st={1,2,2,3,3,4,5,6}
# print(len(st))
# print(st)


#it will use to remove particular element or items
# st.discard(1)


##porperties of set
# st={1,2,2,1,3,4,5,6}
# st1={1,2,3,4,5,6,7,8,9}
# st2=st1.union(st)

# st2=st.intersection(st1)

# st.intersection_update(st1)

# st2=st1.difference(st)

# st1.difference_update(st)

# st2=st.symmetric_difference(st1)

# st.symmetric_difference_update(st1)

# print(st2)
# print(st)
# print(st1)

# Frozen set is immutable and ordered dead opposite of set
#hashable (Fixed values)


# st2=frozenset({1,"P","p",1,3,0,4,5,6,True, False})
# st1=frozenset({1,"p","P", 1,3,4})
# print(st1)
# print(st2)

# fs1 = frozenset([1, 2])
# fs2 = frozenset([3, 4])
# result = fs1.union(fs2)
# print(result)

# fs1 = frozenset([1, 2, 3])
# fs2 = frozenset([2, 3, 4])
# result = fs1.intersection(fs2)  
# print(result)

# fs1 = frozenset([1, 2, 3])
# fs2 = frozenset([3, 4])
# result = fs1.difference(fs2)
# print(result)

# fs1 = frozenset([1, 2, 3])
# fs2 = frozenset([3, 4])
# result = fs1.symmetric_difference(fs2) 
# print(result)


##Subset method
# a={1,2,3}
# b={1,2,3,4,5,6}

# print(a.issubset(b)) ##if it correct it will give True else it give false

# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5}
# print(a.issuperset(b))  ##if it correct it will give True else it give false


##Disjoint is the not same in both the sets and even if it has single element common it gives Flase 
# a={11,12,13,14}
# b={1,2,3,4,5,6,7,14}
# print(a.isdisjoint(b))

# a={1,2,3,4,5}
# b={5,4,6,7,8,9,10}
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)
# print(a<=b)
# print(a>=b)

#Set comphereations

# Set=(1,2,3,4,5,6,7,8,12,14,16)
# print(type(Set))
# result={x for x in Set if x%2==0}
# print(result)

# FROm name list out uniq char
# Char=("Deepak")
# result={name for name in Char  }
# print(result)



##Common char between two string
# str1="Python"
# st2="Program"
# common=set(str1).intersection(set(st2))
# print(common)




# Create a set of numbers find the prime number from set
# Prime={1,2,3,4,5,6,7,8,9}
# result = {x for x in Prime if x > 1 and sum(x % i == 0 for i in range(1, x + 1)) == 2}
# print(result)

# set=int(input("Enter a number:"))
# count=0
# for i in range(1, set+1):
#     if set%i==0:
#         count+=1
# if count==2:
#     print("Prime:", set)
# else:
#     print("Not a prime")

    