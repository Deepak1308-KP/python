# Extract even numbers from a list.
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# Even = [x for x in ls if x % 2 == 0]
# print(Even)

# Get all employees with salary above ₹50,000.
# employees = [
#     ["Rahul", 45000],
#     ["Priya", 60000],
#     ["Arun", 75000],
#     ["Sneha", 50000],
#     ["Kiran", 80000]
# ]
# salary=[x for x in employees if x[1]>50000]
# print(salary)

# Filter names longer than 5 characters.
# names=["Deepak", "Sachin" , "gagan", "Darshan"]
# filter=[x for x in names if len(x)>5 ]
# print(filter)

# Extract numbers divisible by 3.
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12,15]
# Three = [x for x in ls if x % 3 == 0]
# print(Three)


# Get positive numbers from a list.
# ls=[1,2,3,4,5,-1,-2,-3]
# pos=[x for x in ls if x>0]
# print(pos)

# Filter students who passed (marks ≥ 40).
# students = [
#     ["Rahul", 45],
#     ["Priya", 60],
#     ["Arun", 30],
#     ["Sneha", 35],
#     ["Kiran", 40]
# ]
# eligible=[x  for x in students if x[1]>=40]
# print(eligible)

# Extract vowels from a string.
# S=["The quick brown fox jumps over the lazy dog."]
# vowel=[x for x in S[0] if x in "aeiouAEIOU"]
# print(vowel)

# Get products priced above ₹1000.
# products = [
#     ["Phone", 15000],
#     ["Mouse", 800],
#     ["Keyboard", 1200],
#     ["Headphones", 900]
# ]
# price=[x for x in products if x[1]>1000]
# print(price)

# for we want product  for the above question
# price=[x[0] for x in products if x[1]>1000]

# # Filter odd numbers and square them.
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# odd = [x**2 for x in ls if x % 2 != 0]
# print(odd)


# Extract words starting with a vowel.
# Fruits=["Apple", "Egale", "Ice", "Orange", "Dragonfruit", "pineapple" ]
# vowel=[x for x in Fruits if x[0] in "aeiouAEIOU"]
# print(vowel)

# Get active users from user status list.
# users = [
#     ["Deepak", "active"],
#     ["Rahul", "inactive"],
#     ["Priya", "active"],
#     ["Arun", "inactive"]
# ]
# active=[x[0] for x in users if x[1]=="active"]
# print(active)

# Filter emails ending with “.com”.
# emails = ["a@gmail.com", "b@yahoo.in", "c@outlook.com", "d@gmail.in"]
# result = [x for x in emails if x.endswith(".com")]
# print(result)

# Extract ages greater than 18.
# user=[["Deepak", 22],
#       ["Sachin",22],
#       ["Bharath",17],
#       ["Vikesh",21]
# ]
# Age=[x[0] for x in user if x[1]>18]
# print(Age)

# Filter temperatures above normal.
# temperatures = [25, 32, 28, 40, 35, 22]
# normal = 30
# result = [x for x in temperatures if x > normal]
# print(result)

# Extract prime numbers from a list.
# num=[2,3,4,5,6,7,8,9,10]
# prime = [x for x in num if x > 1 and len([i for i in range(1, x+1) if x % i == 0]) == 2]
# print(prime)

# Get strings containing substring “admin”.
# strings = ["admin123", "user", "superadmin", "guest", "administrator"]
# result = [x for x in strings if "admin" in x]
# print(result)

# Filter negative values from sensor data.
# sensor_data = [
#     ["Temperature", 32],
#     ["Humidity", -65],
#     ["Pressure", 1012],
#     ["Temperature", 28],
#     ["Humidity", -75]
# ]
# result=[x for x in sensor_data if x[1]<0]
# print(result)

# Extract even-length words.
# names=["KP", "Deepak", "Gagan","Sachin" ,"Bharath"]
# result=[x for x in names if (len(x)%2==0)]
# print(result)

# Get employees from “IT” department.
# user=[["Deepak", "IT"],
#       ["Sachin","NON IT"],
#       ["Bharath"," NON IT"],
#       ["Vikesh","IT"]
# ]
# Age=[x[0] for x in user if x[1]=="IT"]
# print(Age)

# Filter valid phone numbers (10 digits).
# phoneno=[6363753781, 8277328017, 1234567]
# result=[x for x in phoneno if len(str(x))==10]
# print(result)

# Extract multiples of 5.
# Five=[1,5,15,20,25,26, 38,29,30]
# result=[x for x in Five if x%5==0]
# print(result)

# Filter scores above class average.
# scores = [50, 70, 80, 40, 60]
# average = sum(scores) / len(scores)
# result = [x for x in scores if x > average]
# print(result)

# Extract filenames with .csv extension.
# files=["Word.csv", "Name.pdf", "list.csv"]
# result=[x for x in files if x.endswith(".csv")]
# print(result)

# Filter numbers less than 100 and square them.
# square=[20, 40, 100, 120, 25]
# result=[x**2 for x in square if x<100]
# print(result)

# # Extract cities starting with “C”.
# cities=["Channai","Chitradurga", "Shivamogga", "Mysore"]
# result=[x for x in cities if x.startswith("C")]
# print(result)

# Filter passwords longer than 8 characters.
# passwords = ["abc123", "password123", "Deepak@123", "hello"]
# result = [x for x in passwords if len(x) > 8]
# print(result)

# Extract non-zero values.
# values = [0, 10, -5, 0, 20, -3]
# result = [x for x in values if x != 0]
# print(result)

# Filter dates from the year 2025.
# dates = ["2024-05-10", "2025-01-15", "2025-08-20", "2026-03-10"]
# result = [x for x in dates if x.startswith("2025")]
# print(result)

# Extract values greater than mean.
# values = [10, 20, 30, 40, 50]
# mean = sum(values) / len(values)
# result = [x for x in values if x > mean]
# print(result)

# Filter strings that are numeric.
# values = ["123", "hello", "45", "abc", "78"]
# result = [x for x in values if x.isnumeric()]
# print(result)

# Get valid discount coupons.
# coupons = ["SAVE10", "INVALID", "SAVE20", "EXPIRED", "SAVE30"]
# result = [x for x in coupons if x.startswith("SAVE")]
# print(result)

# Filter odd-indexed values.
# x = [10, 20, 30, 40, 50]
# result = [x[i] for i in range(len(x)) if i % 2 != 0]
# print(result)

# Extract uppercase letters from a string.
# text = "HeLLo WoRLd"
# result = [x for x in text if x.isupper()]
# print(result)

# Filter failed transactions.
# transactions = [100, 20, 75, 30, 90]
# result = [x for x in transactions if x < 50]
# print(result)

# Extract numbers divisible by both 2 and 3.
# numbers = [6, 8, 12, 15, 18, 20]
# result = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
# print(result)

# Filter prices with GST above threshold.
# prices = [500, 800, 1000, 2000]
# result = [x for x in prices if x * 0.18 > 100]
# print(result)

# Extract palindromes from word list.
# words = ["madam", "hello", "level", "python", "radar"]
# result = [x for x in words if x == x[::-1]]
# print(result)

# Filter salaries within tax slab.
# salaries = [300000, 500000, 700000, 1000000, 1200000]
# result = [x for x in salaries if 500000 <= x <= 1000000]
# print(result)

# Extract valid email IDs.
# emails = [
#     "abc@gmail.com",
#     "hello",
#     "test@yahoo.com",
#     "wrong@",
#     "user@outlook.com"
# ]
# result = [x for x in emails if "@" in x and "." in x]
# print(result)

# Filter marks between 60 and 80.
# marks = [45, 60, 65, 75, 80, 90]
# result = [x for x in marks if 60 <= x <= 80]
# print(result)

# Extract strings without special characters.
# words = ["hello", "hello123", "#python", "hello@", "world"]
# result = [x for x in words if x.isalnum()]
# print(result)

# Filter duplicate-free values.
# arr = [1, 2, 2, 3, 4, 4, 5]
# result = [x for x in arr if arr.count(x) == 1]
# print(result)

# Extract temperatures below freezing.
# temperatures = [10, -5, 0, -10, 20, -2]
# result = [x for x in temperatures if x < 0]
# print(result)

# Filter products in stock.
# stock = [0, 5, 10, 0, 3]
# result = [x for x in stock if x > 0]
# print(result)

# Extract employees with experience > 5 years.
# experience = [
#     ["Deepak", 2], 
#     ["Prajwal", 6]
#     ,["Bharath", 4],
#     ["Sachin", 8],
#     ["Gagan", 10],
#     ["Vikesh", 3]]
# result = [x for x in experience if x[1] > 5]
# print(result)

# Filter URLs starting with “https”.
# urls = [
#     "https://google.com",
#     "http://example.com",
#     "https://github.com",
#     "ftp://test.com"
# ]
# result = [x for x in urls if x.startswith("https")]
# print(result)

# Extract integers from mixed list.
# arr = [10, "hello", 20, 3.5, "python", 30]
# result = [x for x in arr if isinstance(x, int)]
# print(result)

# Filter words ending with “ing”.
# words = ["running", "hello", "walking", "python", "coding"]
# result = [x for x in words if x.endswith("ing")]
# print(result)

# Extract values less than median.
# arr = [10, 20, 30, 40, 50]
# median = 30
# result = [x for x in arr if x < median]
# print(result)

# Filter non-empty strings.
# words = ["hello", "", "python", "", "world"]
# result = [x for x in words if x != ""]
# print(result)