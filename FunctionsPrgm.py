

# Write a program that uses three functions to print information about a laundromat, Liam's Laundry:
# laundromat_info(): Prints the name, Liam's Laundry, and hours of operation, 7a - 11p, and calls washers_open() and dryers_open().
# washers_open(): Reads an integer, assigns washer_count with the value, and prints washer_count.
# dryers_open(): Reads an integer, assigns dryer_count with the value, and prints dryer_count.

# def washers_open():
#     washer_count = int(input())
#     print("Open washers:", washer_count)

# def dryers_open():
#     dryer_count = int(input())
#     print("Open dryers:", dryer_count)

# def laundromat_info():
#     print("Liam's Laundry")
#     print("7a - 11p")
#     washers_open()
#     dryers_open()
# laundromat_info()


# Write an updated function, terms(), that asks the user to accept the terms and conditions, reads in Y/N,
# and outputs a response by calling accepted() or rejected().
# accepted() prints "Thank you for accepting the terms." and rejected() prints "You have rejected the terms. Thank you."

# def accepted():
#     print("Thank you for accepting the terms.")
# def rejected():
#     print("You have rejected the terms.")
# def terms():
#     check_box=input("Do you accept the terms and conditions?(y/n):")
#     if check_box=="y":
#         accepted()
#     elif check_box=="n":
#         rejected()
# terms()



# Write a function, print_area(), that takes in the base and height of a right triangle and
# prints the triangle's area. The area of a right triangle is bh/2, where b is the base and h is the height.
# def area():
#     print("Enter a height and breadth to calculate area of triangle")
#     a =int(input("Base:"))
#     b=int(input("Height:"))
#     print(f"{a*b/2}")
# area()

##Another method
# def print_area(base, height):
#     area =(base*height)/2
#     print("Triangle area", area)
# print_area(3,4)


# Write a function, print_scores(), that takes in a 
# list of test scores and a number representing how many points to add. For each score,
# print the original score and the sum of the score and bonus. Make sure not to change the list.

# def total(score, bonus):
#     for value in score:
#         updated_score= value+bonus
#         print(f"{score} be updated to {updated_score}")
# total([67, 68, 72, 71, 69], 10)