#Anthony Love
#04/28/2024
#P4LAB2_LoveAnthony
#For and While Loop Together




run = "yes"

while run != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for item in range(1 , 13):
            print(f"{user_num} * {item} = {user_num * item} ")

    else:
            print("This program does not handle negative values")


    run = input("Would you like to run again? ")

print("Program is ending....")
       
        
