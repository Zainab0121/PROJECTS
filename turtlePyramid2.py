import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green",  "orange"]
for i in range(300):
    t.pencolor(colors[i % 4])
    t.circle(i * 2)
    t.left(50)
turtle.done()