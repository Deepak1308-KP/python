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





#1. add sales data 
#2. view all sales data 
#3. view total and avg sales data 
#4. hieghest and lowest sales
#5. sort sales data 
#6. search sales by amount 
#7. generate business insights
   # total sales
   # avg daily sales
   #   heighst sales
    #   lowest sales
    #   sales above avg 
    #   sales below avg
    #   growth rate(1st-last)
    #   buisiness growth
# 8. monthly summary report
# 9. backup the data
# 10. clear sales data 
import random
import json

sales_data = []
backup_data = []


def has_data():
    if not sales_data:
        print("No sales data. Add data first (option 1).")
        return False
    return True


# 1. Add sales data
def add_sales():
    global sales_data
    try:
        n = int(input("Enter the number of data: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    sales_data = [round(random.uniform(30000.00, 150000.00), 2) for _ in range(n)]
    print(f"{n} records added.")


# 2. View all
def view_all():
    if has_data():
        for day, amt in enumerate(sales_data, 1):
            print(f"Day {day}: {amt}")


# 3. Total and average
def view_total_and_average():
    if has_data():
        print(f"Total: {sum(sales_data):.2f} | Average: {sum(sales_data)/len(sales_data):.2f}")


# 4. Highest and lowest
def highest_and_lowest():
    if has_data():
        hi, lo = max(sales_data), min(sales_data)
        print(f"Highest: {hi} (day {sales_data.index(hi) + 1})")
        print(f"Lowest:  {lo} (day {sales_data.index(lo) + 1})")


# 5. Sort
def sort_sales():
    if not has_data():
        return
    while True:
        choice = input("1. Ascending\n2. Descending\n3. Exit\nChoice: ")
        if choice == "1":
            print(sorted(sales_data)); break
        elif choice == "2":
            print(sorted(sales_data, reverse=True)); break
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# 6. Search by amount
def search_by_amount():
    if not has_data():
        return
    try:
        amt = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    days = [i + 1 for i, x in enumerate(sales_data) if x == amt]
    print(f"Found on day(s): {days}" if days else "This amount is not in the sales data.")


# 7. Business insights
def insights():
    if not has_data():
        return
    total = sum(sales_data)
    avg = total / len(sales_data)
    first, last = sales_data[0], sales_data[-1]
    growth = (last - first) / first * 100

    if growth > 0:
        status = "Growing"
    elif growth < 0:
        status = "Declining"
    else:
        status = "Stable"

    print(f"Total sales:         {total:.2f}")
    print(f"Avg daily sales:     {avg:.2f}")
    print(f"Highest sale:        {max(sales_data)}")
    print(f"Lowest sale:         {min(sales_data)}")
    print(f"Days above average:  {sum(1 for x in sales_data if x > avg)}")
    print(f"Days below average:  {sum(1 for x in sales_data if x < avg)}")
    print(f"Growth rate (1st-last): {growth:.2f}%")
    print(f"Business status:     {status}")


# 8. Monthly summary (30-day blocks)
def monthly_summary():
    if not has_data():
        return
    for i in range(0, len(sales_data), 30):
        chunk = sales_data[i:i + 30]
        print(f"Month {i // 30 + 1} ({len(chunk)} days): "
              f"total={sum(chunk):.2f}, avg={sum(chunk)/len(chunk):.2f}, "
              f"high={max(chunk)}, low={min(chunk)}")


# 9. Backup
def backup():
    global backup_data
    if not has_data():
        return
    backup_data = sales_data.copy()          # in-memory backup
    with open("sales_backup.json", "w") as f:  # file backup
        json.dump(sales_data, f)
    print("Backup saved (memory + sales_backup.json).")


# 10. Clear
def clear_data():
    global sales_data
    if input("Clear all sales data? (y/n): ").lower() == "y":
        sales_data = []
        print("Sales data cleared.")


MENU = {
    "1": add_sales, "2": view_all, "3": view_total_and_average,
    "4": highest_and_lowest, "5": sort_sales, "6": search_by_amount,
    "7": insights, "8": monthly_summary, "9": backup, "10": clear_data,
}

while True:
    print("\n1.Add 2.View 3.Total/Avg 4.High/Low 5.Sort 6.Search "
          "7.Insights 8.Monthly 9.Backup 10.Clear 0.Exit")
    ch = input("Choice: ")
    if ch == "0":
        break
    MENU.get(ch, lambda: print("Invalid choice."))()