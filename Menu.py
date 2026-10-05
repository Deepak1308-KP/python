# total_bill = 0
# while True:
#     print("\n--- Menu ---")
#     print("1. Idli       - ₹40")
#     print("2. Dosa       - ₹60")
#     print("3. Poori      - ₹50")
#     print("4. Rice Bath  - ₹70")
#     print("5. Coffee     - ₹30")
#     print("6. Tea        - ₹20")
#     print("7. Exit & Generate Bill")
#     choice = int(input("\nEnter your choice: "))
#     if choice == 1:
#         item = "Idli"
#         price = 40
#     elif choice == 2:
#         item = "Dosa"
#         price = 60
#     elif choice == 3:
#         item = "Poori"
#         price = 50
#     elif choice == 4:
#         item = "Rice Bath"
#         price = 70
#     elif choice == 5:
#         item = "Coffee"
#         price = 30
#     elif choice == 6:
#         item = "Tea"
#         price = 20
#     elif choice == 7:
#         print("\nThank you for visiting Pradeep Hotel!")
#         print("Your total bill is: ", total_bill)
#         break
#     else:
#         print("Invalid choice! Please select 1 to 7.")
#         continue
#     quantity = int(input("Enter quantity: "))
#     amount = price * quantity
#     total_bill = total_bill + amount
#     print("\nItem      : ", item)
#     print("Price     : ", price)
#     print("Quantity  : ", quantity)
#     print("Amount    : ", amount)
#     print("Total  :", total_bill)


# balance=1000
# while True:
#     print("\n-------Welcome to Karnataka Bank---------------")
#     print("1. Check Balance")
#     print("2. Deposite")
#     print("3. Withdraw")
#     print("4.exit")
    
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         print("\n Your current account balnace",balance)
        
#     elif choice==2:
#         amount=int(input("Enter your deposite amount: "))
#         if amount > 0:
#             balance = balance + amount
#             print("\nSuccessfully deposited: ₹", amount)
#             print("Updated Balance       : ₹", balance)
#         else:
#             print("\nInvalid deposit amount!")
            
#     elif choice==3:
#         amount=int(input("Enter a your withdraw amount:"))
#         if amount<=0:
#             print("\nInvalid withdrawal amount!")
#         elif amount>balance:
#             print("\n invalid balance")
#         else:
#             balance=balance-amount
#             print("\nSuccessfully withdrawn: ₹", amount)
#             print("\n your account balance is :" ,balance)
#     elif choice==4:
#         print("\nThank you for using our ATM service. Have a great day!")
#         break
#     else:
#         print("\nInvalid choice! Please select 1 to 4.")
#         continue