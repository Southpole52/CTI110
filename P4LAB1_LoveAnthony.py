#Anthony Love
#04/28/2024
#P4LAB1_LoveAnthony
#Use Turtle and loops to draw


import turtle


win = turtle.Screen()
pen = turtle.Turtle()

pen.pensize(3)
pen.pencolor("green")
pen.shape("arrow")

for side in range(4):
    pen.forward(100)
    pen.left(90)

sides = 3
while sides > 0 :
    pen.forward(100)
    pen.left(120)
    sides = sides - 1


win.mainloop()
