import turtle

def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()

draw_square(alex, 20)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()

draw_square(alex, 40)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()

draw_square(alex, 60)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()

draw_square(alex, 80)

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()

draw_square(alex, 100)

wn.mainloop()
