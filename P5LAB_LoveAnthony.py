#Anthony Love
#5/5/2024
#P5LAB_LoveAnthony
#User Defined Functions

import random 
def main():
    owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe: ${owed:.2f}")

    deposit = float(input("How much cash will you put in the self-checkout?"))
    
    change = deposit - owed
    print(f"Change is: ${change:.2f}")

    disperse_change(change)


def disperse_change(change):
    
    
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

main()



