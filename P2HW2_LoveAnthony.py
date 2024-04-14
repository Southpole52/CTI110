#Anthony Love
#04/14/2024
#P2HW2_LoveAnthony
#Average Grade Calculator

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

mod_list = [mod1 , mod2 , mod3 , mod4 , mod5 , mod6]

mins = min(mod_list)
maxs = max(mod_list)
sums = sum(mod_list)
ave = (sum(mod_list)/6 )


print()


print("------------Results------------")
print(f"Lowest Grade:      {mins:.2f}")
print(f"Highest Grade:     {maxs:.2f}")
print(f"Sum of grades:     {sums:.2f}")
print(f"Average:           {ave:.2f}")



