print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height >= 100:
    print("You can ride the roller coaster!")
    if age < 12:
        print("Please pay Rs.5")
        bill = 5
    elif age <= 18:
        print("Please pay Rs.7")
        bill = 7
    elif 40 <= age <= 60:
        print("Enjoy Your Free Ride")
    else:
        print("Please pay Rs.12")
        bill = 12
    print("Do You want to Take Photos For Extra Rs.3 ? Y or N")
    answer = input()
    if answer == "Y":
        print("Great! Let's go!")
        print(f"Your bill is Rs. {bill + 3}")
    elif answer == "N":
        print("Okay, maybe next time!")

else:
    print("You are too young to ride the roller coaster!")
