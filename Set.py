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

# st2=frozenset({1,"P","p",1,3,0,4,5,6,True, False})
# st1=frozenset({1,"p","P", 1,3,4})
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