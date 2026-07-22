import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.pensize(2)
t.color("green")
t.left(90)
t.speed(50)
t.penup()
t.goto(0, -250)
t.pendown()

def tree(i):
    if i < 10:
        t.color("pink")
        t.dot(6)
        return
    else:
        t.color("brown")
        t.forward(i)

        t.left(25)
        tree(3*i/4)

        t.right(50)
        tree(3*i/4)

        t.left(25)
        t.backward(i)

tree(100)
turtle.done()
