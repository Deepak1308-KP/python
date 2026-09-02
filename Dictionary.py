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

# Set default= it inserts the key with the specified default value into the dictionary.
# info={'name':'Deepak', 'age':22, 'Hometown':'Shivamogga'}
# age = info.setdefault('village', 'kanasinakatte')
# print(info)

