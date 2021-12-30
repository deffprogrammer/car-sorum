print("========== Welcome to Car Sorum ==========")
print("1. Rent a car")
print("2. Return a car")
option = input("Enter your option (use number) : ")

total = 0
if option == "1":
    print("List car : ")
    print("1. Toyota")
    print("2. Daihatsu")
    print("3. Honda")
    print("4. Suzuki")
    car = input("Enter your option (use number) : ")
    how_long = int(input("How long do you want to rent a car? : "))
elif option == "2":
    print("List car ")
    print("1. Toyota")
    print("2. Daihatsu")
    print("3. Honda")
    print("4. Suzuki")
    car = input("Which car do you rent? (use number) : ")
    how_long = int(input("How long do you want to rent a car? : "))
    if car == "1":
        total = 1000 * how_long
        print("The car you rent is Toyota, for {} days".format(how_long))
    elif car == "2":
        total = 2000 * how_long
        print("The car you rent is Daihatsu, for {} days".format(how_long))
    elif car == "3":
        total = 3000 * how_long
        print("The car you rent is Honda, for {} days".format(how_long))
    elif car == "4":
        total = 4000 * how_long
        print("The car you rent is Suzuki, for {} days".format(how_long))
    else:
        print("The input you entered is wrong!!")
        exit()
    print("Total", total)
else:
    print("The input you entered is wrong")


