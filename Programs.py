# items=[('apple','fruit'),('Carrot', 'Vegetable'), ('Tamoto', 'vegetable'), ('Banana', 'fruit')]
# grouped={}
# for item, category in items:
#     grouped.setdefault(category,[]).append(item)
# print(grouped)


##Inverted  changing value into key and keys into values

# value={'a':1, 'b':2, 'c':1, 'd':3}
# Reversed={}
# for item, category in value.items():
#     Reversed.setdefault(category,[]).append(item)
# print(Reversed)

##Another Method
# value={'a':1, 'b':2, 'c':1, 'd':3}
# Inverted={}
# for key, value in value.items():
#     if value in Inverted:
#         Inverted[value].append(key)
#     else:
#         Inverted[value]=[key]
# print(Inverted)


##Each word id the key length of the word is value
# Sentence="Python is the eas"
# dict={}
# word=Sentence.split(" ")
# for i in word:
#     dict[i]=len(i)
# print(dict)

# Student ={"Deepak":{'kannada':100,'English':65,'Science':70,'Maths':80},
# "Gagan":{'kannada':80,'English':55,'Science':70,'Maths':80},"Vikesh":{'kannada':90,'English':55,'Science':60,'Maths':70}}
# average={}
# for Student, subjects in Student.items():
#     total=sum(subjects.values())
#     count=len(subjects)
#     average[Student]=total/count
# print("Average Marks:", average)


