#Anthony Love
#04/28/2024
#P4HW2_Salary_LoveAnthony
#Salary Again but better


overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0
 


while True:

    name = input("Enter employee's name or Done to terminate: ")
    if name == "done":
        print()
        print(f"Total number of employees entered: {num_employees}")
        print(f"Total amount paid for overtime: ${overtime_total}")
        print(f"Total amouunt paid for regular hours ${regular_pay_total}")
        print(f"Total amount paid in gross: ${gross_pay_total}")
        break
    num_employees += 1
    hours = float(input(f"How many hours did {name} work? "))
    pay = float(input(f"What is {name}'s pay rate?: "))
    print()
    print(f"Employee name:      {name} ")

    if hours <= 40:
        regular_pay = pay * hours
        overtime = 0
        overtime_pay = 0
        gross_pay = regular_pay + overtime_pay

    else:
        regular_pay = pay * 40
        overtime = hours - 40
        overtime_pay = (overtime) * (pay * 1.5)
        gross_pay = regular_pay + overtime_pay
    
    print("Hours Worked    Pay Rate       OverTime        Overtime Pay      RegHour Pay      Gross pay")
    print("---------------------------------------------------------------------------------------------------------")
    print(f"{hours:<15,.2f} {pay:<16,.2f}{overtime:<16,.2f}{overtime_pay:<18,.2f}{regular_pay:<18,.2f}{gross_pay:<15,.2f}")


    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay


 
#Once you've gathered all your inputs, implement a While loop to continuously check if the user has entered "done". 
# If the user hasn't finished collecting all the data, store each input in separate variables and calculate the total for each employee.
# When "done" is entered, halt the program and display the combined employee data.
