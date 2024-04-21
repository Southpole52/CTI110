#Anthony Love
#04/21/2024
#P3HW2_Salary_LoveAnthony
#Salary Calculator

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))

reg_hours = 40
overtime_pay_rate = (1.5 * pay)

if hours > 40:
    overtime = hours - reg_hours
    reg_pay = reg_hours * pay
    overtime_pay = overtime_pay_rate * overtime
    gross_pay = overtime_pay + reg_pay
else :
    overtime = 0
    reg_pay = reg_hours * pay
    overtime_pay = 0
    gross_pay = overtime_pay + reg_pay


    


print("----------------------------------------")
print(f"Employee name:  {name}" )
print()
print("Hours Worked    Pay Rate       OverTime        Overtime Pay      RegHour Pay      Gross pay")
print("---------------------------------------------------------------------------------------------------------")
print(f"{hours:<15,.2f} {pay:<16,.2f}{overtime:<16,.2f}{overtime_pay:<18,.2f}{reg_pay:<18,.2f}{gross_pay:<15,.2f}")
