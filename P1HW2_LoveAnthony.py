#Anthony Love
#04/07/2024
#P1HW2_LoveAnthony
#Travel Expense Calculator

print("This program calculates and displays travel expenses")
print("Enter Budget:" , end = " " )
bud = int(input())
print()
print("Enter your travel destination:" , end = " ")
des = input()
print()
print("How much do you think you will spend on gas?" , end = " " )
gas = int(input())
print()
print("Approximately, how much will you need for accomodation/hotel?" , end = " ")
hotel = int(input())
print()
print("Last, how much do you need for food?" , end = " ")
food = int(input())
print("------------Travel Expenses------------")
print("Location: " , des)
print("Inital Budget: " , bud)
print()
print("Fuel:" , gas)
print("Accomodation: " , hotel)
print("Food: " , food)
print()
print("Remaining Balance:" , bud-gas-hotel-food)

#The logic would be to just subtract all of the expenses from the inital value of the budget. 
