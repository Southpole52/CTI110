#Anthony Love
#04/20/2024
#P3LAB_LoveAnthony
#If Else Statements

change = float(input("Enter an amount of money: $"))

change = round(change * 100)


dollars = change // 100
change = change - (dollars * 100)

quarters = change // 25
change = change - (quarters * 25)

dimes = change // 10
change = change - (dimes * 10)

nickels = change // 5
change = change - (nickels * 5)

pennies = change // 1
change = change - (pennies * 1)

if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print(f"{nickels} Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    else:
        print(f"{pennies} Pennies")



