# Dictionary is ordered collection, it has a keyvalue pairs, and
# it can be store multiple items in a single variable, it has used{},  
# it is mutable in nature and we  can accesed by separetly by using key, values

# Dictionary={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# print(Dictionary)

# dictionary={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# print(dictionary['name'])
# print(dictionary.get('age'))

# Dictionary={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# print(Dictionary.values())

# Dictionary={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# print(Dictionary.keys())

# Dictionary={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# print(Dictionary.items())

# Methods of dictionary
#Update
# info={'name':'DKP', 'age':21}
# info.update({'age':22})
# info.update({'DOB':2004})
# print(info)

##Removing items from dict
##Clear==removes all the items from list

# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# info.clear()
# print(info)

##Pop()= removes the key value pairs enclose key is passed as a parameter
# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# info.pop('age')
# print(info)

# popitem()=removes the last keyvalue pairs from dictionary in info.popitem
# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# info.popitem()
# print(info)

# Delete= we can use also the del keyword to remove a dict item of particular element 
# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# del info['age']
# print(info)


#Copy()=This is the method returns a shallow of copy from the dictionary
# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# info1=info.copy()
# print(info1)
# print(info)

# Set default= it inserts the key with the specified default value into the dictionary if not value in dictionary.
# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# age = info.setdefault('village', 'kkt')
# print(info)

# dic={"name":"Deepak", "roll_no":35, "clg":"kit"}
# if "marks" in dic:
#     dic.setdefault("marks", 55)
#     print(dic)
# else:
#     dic.setdefault("marks", 60)
#     print(dic)

# Nested Dictionary
# information ={"stu1":{"name": "Deepak"},
#               "stu2":{"name":"DKP"}}
# print(information)

# dic=("name", "age", "DOB", "height")
# dic1=dict.fromkeys(dic)
# print(dic1)

##Sorted
# student ={"name ":"Deepak", "age":22, "DOB":2004}
# stu=dict(sorted(student.items()))
# print(stu)

##Feq letter counting
# name=input("Enter a your name:")
# dic={}
# for char in name:
#     if char in dic:
#         dic[char]+=1
#     else:
#         dic[char]=1
# print(dic)
    
##Word frequency
# sentence="Python is easy and  python is powerfull"
# sent=sentence.split(" ")
# dic={}
# for word in sent:
#     if word in dic:
#         dic[word]=dic[word]+1
#     else:
#         dic[word]=1
# print(dic)
            
            
##ZIp function
# D=["name", "Roll_no","class", "Native"]
# D1=["Deepak", 29, 12, "Shivamogga"]
# dic=dict(zip(D,D1))
# print(dic)

# ##Dictionary Comprehential
# square={i:i*i for i in range(1, 11)}
# print(square)

# even={i:i for i in range(1,50) if i%2==0}
# print(even)

##Student of marks highst
# students={"Deepak":80, "Gagan":90, "Vikesh":75, "Suhail":85}
# max={}
# for i in students:
#     i.max


# Find the most freq char
n={"name1":"vikesh","name2":"pradeep","name3":"suresh","name4":"mahesh"}
repeated_char=max(n,key=n.get)
print(repeated_char)
    