import turtle
import math

def getPointPosition(radius, points, num):
    #calculate the position of each point on the circle
    xPosition = radius * math.cos(((2 * math.pi) / points) * num)
    yPosition = radius * math.sin(((2 * math.pi) / points) * num)

    yield (xPosition, yPosition) #generator

def drawCircleWithPoints(points, radius, dots, turtle):

    turtle.circle(radius)
    turtle.penup()

    #draw each point we want on the circle and store them in a list
    for i in range(points):
        position = getPointPosition(radius, points, i)

        for pos in position:
            turtle.goto(pos[0], pos[1] + radius)
            turtle.dot()
            dots.append(turtle.position())

def timesTableCircle(points, radius, multiplier, dots, turtle):

    #draw a circle with some dots
    drawCircleWithPoints(points, radius, dots, turtle)

    #do the timetable
    for i in range(points):

        #goto the dot to draw from
        turtle.penup()
        turtle.goto(dots[i])

        #calculate and go to the dot to draw to
        turtle.pendown()
        turtle.goto(dots[(i * multiplier) % points])

def main():
    radius = 200
    points = 52
    multiplier = 2

    # make a turtle
    t= turtle.Turtle()
    t.color("red")
    t.pensize(2)
    t.speed(20)

    window = turtle.Screen()
    window.setup(1000, 1000)

    dots = []

    #do the thing
    timesTableCircle(points, radius, multiplier, dots, t)
    window.exitonclick()

if __name__ == '__main__':
    main()
