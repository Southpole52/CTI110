#Anthony Love
#04/14/2024
#P2HW1_LoveAnthony
#Travel Expense Calculator Updated with float and strings

print("This program calculates and displays travel expenses")
print("Enter Budget:" , end = " " )
bud = float(input())
print()
print("Enter your travel destination:" , end = " ")
des = input()
print()
print("How much do you think you will spend on gas?" , end = " " )
gas = float(input())
print()
print("Approximately, how much will you need for accomodation/hotel?" , end = " ")
hotel = float(input())
print()
print("Last, how much do you need for food?" , end = " ")
food = float(input())
print("------------Travel Expenses------------")
print("Location:           " +  des)
print(f"Inital Budget:      ${bud:.2f} ")
print(f"Fuel:               ${gas:.2f}")
print(f"Accomodation:       ${hotel:.2f} ")
print(f"Food:               ${food:.2f} " )
print("----------------------------------------")
bal = float(bud-gas-hotel-food)
print(f"Remaining Balance:  ${bal:.2f}")
