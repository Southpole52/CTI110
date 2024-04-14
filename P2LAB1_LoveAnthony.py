#Anthony Love
#04/14/2024
#P2LAB1_LoveAnthony
#Using math expressions

import math

radius = float(input("Enter the radius: "))

cir = 2 * math.pi*radius
diam = 2 * radius
area = math.pi * (radius ** 2)

print(f"The diameter of the circle is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")
