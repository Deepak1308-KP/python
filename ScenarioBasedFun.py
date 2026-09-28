# def calculate_total(maths, science, physics,Biology, English):
#     return maths+science+physics+Biology+English
# def calculate_percentage(total):
#     return total/5
# def check_result(percentage):
#     if percentage>=40:
#         return "Pass"
#     else:
#         return "Fail"
# total=calculate_total(20, 20, 20,60,78)
# percentage=calculate_percentage(total)
# result=check_result(percentage)
# print("total:", total)
# print("percentage:", percentage)
# print("Result:", result)

# Priya has joined a software company as a fresher. At the end of the month, the 
# HR department needs to calculate her salary. 
# Her salary contains Basic Salary, HRA, DA, and PF. 
# The company follows these rules: 
#  HRA = 20% of Basic Salary  
#  DA = 10% of Basic Salary  
#  PF = 12% of Basic Salary  
# The HR manager wants the program to calculate both Gross Salary and Net 
# Salary. 
# Task: 
# Create separate functions to calculate HRA, DA, PF, Gross Salary, and Net 
# Salary. 

# def basic_salary(salary):
#     return salary
# def HRA(salary):
#     return salary * 0.20
# def DA(salary):
#     return salary * 0.10
# def pf(salary):
#     return salary * 0.12
# def gross_salary(salary):
#     return salary + HRA(salary) + DA(salary)

# def net_salary(salary):
#     return gross_salary(salary)-pf(salary)

# salary = 20000

# print("Basic Salary:",basic_salary(salary))
# print("HRA:",HRA(salary))
# print("DA:",DA(salary))
# print("PF:",pf(salary))
# print("Gross Salary:",gross_salary(salary))
# print("Net Salary:",net_salary(salary))

# 3. Online Shopping Story 
# Arjun is shopping on an online shopping website. He adds a Laptop, Mouse, 
# Keyboard, and Monitor to his cart. 
# The shopping website needs to calculate the total amount and apply a discount. 
# The website has the following discount rules: 
#  If the total is ₹50,000 or more → 10% discount  
#  If the total is ₹20,000 or more → 5% discount  
#  Otherwise → No discount  
# Task: 
# Create functions to display the products, calculate the total, calculate the 
# discount, and calculate the final bill. 

# def products(Laptop, Mouse, Keyboard, Monitor):
#     print("Laptop", "Mouse", "Keyboard", "Monitor")
    
# def total(Laptop, Mouse, Keyboard, Monitor):
#     return Laptop + Mouse + Keyboard + Monitor

# def discount():
#     amount = total(5000, 2000, 3000, 40000)
#     if amount >= 50000:
#         return amount * 0.10
#     elif amount >= 20000:
#         return amount * 0.05
#     else:
#         return 0
# def final_bill():
#     amount = total(5000, 2000, 3000, 40000)
#     dis = discount()
#     return amount - dis
# products(5000, 2000, 3000, 40000)
# print("Total:", total(5000, 2000, 3000, 40000))
# print("Discount:", discount())
# print("Final Bill:", final_bill())

# Ravi goes to an ATM to withdraw money from his bank account. His current 
# balance is ₹50,000. 
# The ATM should allow him to perform three operations: 
#  Check balance  
#  Deposit money  
#  Withdraw money  
# Ravi should not be allowed to withdraw more money than his available balance. 
# Task: 
# Create separate functions for checking balance, depositing money, and 
# withdrawing money.

# def atm():
#     return balance
# def deposite_amount(deposite):
#     return balance+deposite
# def withdraw_amount(withdraw):
#     if withdraw <= balance:
#         return balance - withdraw
#     else:
#         return "Insufficient Balance"
# balance = 50000
# print("Current Balance:",atm())
# print("Deposite:",deposite_amount(5000))
# print("Withdraw:",withdraw_amount(3000))

# 5. Electricity Bill Story 
# Lakshmi receives her monthly electricity bill. The electricity department 
# calculates the bill based on the number of units consumed. 
# The department follows these rates: 
# First 100 units       
# Next 100 units        
# Next 100 units        
# Above 300 units       
# → ₹2 per unit 
# → ₹3 per unit 
# → ₹5 per unit 
# → ₹7 per unit 
# Lakshmi's house consumed 250 units this month. 
# Task: 
# Create a function that calculates her electricity bill based on the units consumed. 




# 6. Restaurant Story 
# One evening, Sameer goes to a restaurant with his friends. 
# They order: 
# Pizza      
# → ₹250 
# Burger     → ₹150 
# Coffee     → ₹80 
# Task: 
# The restaurant adds 5% GST to the food bill. 
# The restaurant owner wants a program that automatically calculates the bill. 
# Create functions to calculate: 
#  Food total  
#  GST  
#  Final amount
#  Display the complete bill  

# def restaurant():
#     print("Good Evening! Welcome to restaurant..")
# def food():
#     return Pizza+Burger+Coffee
# def GST():
#     return food()*0.05
# def Final_amount():
#     return food()+GST() 
# Pizza=250
# Burger=150
# Coffee=80
# restaurant()
# print("Food Amount: ",food())
# print("GST Amount:",GST())
# print("Total Amount:",Final_amount())

# 7. Bank Loan Story 
# Suresh wants to take a personal loan from a bank. 
# The bank has certain eligibility conditions. Before processing his application, 
# the bank's computer system checks: 
#  Age must be between 21 and 60  
#  Monthly salary must be at least ₹25,000  
#  Credit score must be 700 or above  
# The bank wants to check each condition separately. 
# Task: 
# Create functions to check age eligibility, salary eligibility, and credit-score 
# eligibility. Then create a final function that displays whether Suresh is eligible. 

# def Bank_Loan():
#     return "Welcome to Bank!..."
# def eligibility():
#     if age>=21 and age<=60:
#         return "Eligible"
#     else:
#         return "Not Eligible"
# def salary():
#     if sal>=25000:
#         return "Eligible"
#     else:
#         return "Not Eligible"
# def credit_score():
#     if score>=700:
#         return "Eligible"
#     else:
#         return "Not Eligible"
# def final():
#     if eligibility() == "Eligible" and salary() == "Eligible" and credit_score() == "Eligible":
#         return "Suresh is eligible to take loan"
#     else:
#         return "Suresh is not eligible to take loan"
# age=21
# sal=25000
# score=700
# print(Bank_Loan())
# print("Age:",eligibility())
# print("Salary:",salary())
# print("Credit Score:",credit_score())
# print("Final Decision:",final())


# 8. Food Delivery Story 
# Anjali orders food using a food-delivery application. 
# Her food costs ₹600, and the restaurant is 5 km away. 
# The application calculates delivery charges according to the distance: 
# Up to 3 km       → ₹30 
# 4–7 km            
# → ₹50 
# Above 7 km        
# → ₹80 
# The application also adds 5% GST on the food amount. 
# Task: 
# Create functions to calculate the delivery charge, GST, and final amount 
# payable by Anjali.

# def FoodApp():
#     return "Welcome to Food Delivery Application!..."
# def delivery_charge(distance):
#     if distance <= 3:
#         return 30
#     elif distance >=4 and distance <=7:
#         return 50
#     else:
#         return 80
# def GST(food):
#     return food * 0.05
# def Final_amount(food, distance):
#     return food + delivery_charge(distance) + GST(food)
# food = 600
# distance = 5
# print(FoodApp())
# print("Delivery Charge:", delivery_charge(distance))
# print("GST:", GST(food))
# print("Final Amount:", Final_amount(food, distance))