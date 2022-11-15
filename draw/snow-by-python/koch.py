#koch.py
import turtle

def hua(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            hua(size/3, n-1)


def main():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.pensize(4)
    turtle.goto(-200, -50)
    turtle.pendown()
    num=5
    turtle.Turtle().screen.delay(0)
    hua(300, num)
    turtle.right(120)
    hua(300, num)
    turtle.right(120)
    hua(300, num)
    turtle.mainloop()
    # turtle.hideturtle()

main()
