import turtle

def FractalTriangle(aTurtle, depth, maxdepth):
    if depth > maxdepth:
        return
    else:
        for i in range(3):
            aTurtle.forward(256/(2**depth))
            FractalTriangle(aTurtle, depth+1, maxdepth)
            aTurtle.forward(256/(2**depth))
            aTurtle.left(120)
        return

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    harsh = turtle.Turtle()
    harsh.shape("turtle")
    harsh.color('red')
    harsh.penup()
    harsh.goto(-50, -200)
    harsh.pendown()
    harsh.hideturtle()
    harsh.speed(0)
    harsh.right(180)
    harsh.forward(256)
    harsh.right(180)
    FractalTriangle(harsh, 0, 8)
    window.exitonclick()

draw_art()
