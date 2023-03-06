import turtle

wn = turtle.Screen()
wn.title("Jakup Clicker")
wn.bgcolor("Orange")

wn.register_shape("jakup.gif")

jakup = turtle.Turtle()
jakup.shape("jakup.gif")
jakup.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x,y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))


    jakup.onclick(clicked)

wn.mainloop()