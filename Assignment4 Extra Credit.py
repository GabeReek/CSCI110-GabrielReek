import turtle

def draw_bar(t, height):
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")

    t.begin_fill()

    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)

    t.end_fill()

    t.penup()
    t.forward(10)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

draw_bar(alex, 48)
draw_bar(alex, 117)
draw_bar(alex, 200)
draw_bar(alex, 240)
draw_bar(alex, 160)
draw_bar(alex, 260)
draw_bar(alex, 220)

wn.mainloop()
