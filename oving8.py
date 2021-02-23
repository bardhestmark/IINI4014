import random
import turtle
import math


class Dice:
    # default values
    dicecolor = 'white'
    dotcolor = 'black'
    current_value = None

    def __init__(self, size, position):
        self.size = size  # length of one side
        self.position = position  # a tuple consisting of posx and posy

        self.t = turtle.Turtle()  # a die has it's own turtle
        self.t.pensize(2)
        self.t.speed(6)

    # getter
    def get_size(self):
        return self.size

    #  some setters
    def set_dice_color(self, newdicecolor):
        self.dicecolor = newdicecolor

    def set_dot_color(self, newdotcolor):
        self.dotcolor = newdotcolor

    def set_size(self, newsize):
        self.size = newsize

    # the roll/throw dice method
    def roll(self):
        self.current_value = random.randint(1, 6)

    #  draw the die using turtle, given it has been rolled
    def draw(self):
        if self.current_value is None:
            raise Exception("Dice must be thrown before it is drawn")

        self.t.penup()
        self.t.setposition(self.position)  # move to position specified by user
        self.t.pendown()

        self.t.fillcolor(self.dicecolor)  # make a square and fill it
        self.t.begin_fill()
        self.t.forward(self.size)
        self.t.right(90)
        self.t.forward(self.size)
        self.t.right(90)
        self.t.forward(self.size)
        self.t.right(90)
        self.t.forward(self.size)
        self.t.end_fill()

        self.draw_dots()
        self.t.hideturtle()

    #  helper for draw
    def draw_dots(self):
        diag = self.size * math.sqrt(2)  # the diagonal of the die
        self.t.penup()
        self.t.right(135)  # given we're on the upper left corner of the die facing north
        self.t.fd(diag / 4)  # now at upper left "dot position" where 5/6 possible values has a dot

        dotsize = self.size / 6  # set the dotsize relative to the size of the die
        val = self.current_value

        if val == 1:  # the possible throws, harcoded
            self.t.fd(diag / 4)
            self.t.dot(dotsize, self.dotcolor)
        elif val == 2:
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(diag / 2)
            self.t.dot(dotsize, self.dotcolor)
        elif val == 3:
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(diag / 4)
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(diag / 4)
            self.t.dot(dotsize, self.dotcolor)
        elif val == 4:
            self.t.dot(dotsize, self.dotcolor)
            self.t.left(45)
            self.t.fd(self.size / 2)
            self.t.dot(dotsize, self.dotcolor)
            self.t.right(90)
            self.t.fd(self.size / 2)
            self.t.dot(dotsize, self.dotcolor)
            self.t.right(90)
            self.t.fd(self.size / 2)
            self.t.dot(dotsize, self.dotcolor)
        elif val == 5:  # it would probably be easier to use 4 as a starting point for 5 & 6
            self.t.dot(dotsize, self.dotcolor)
            self.t.left(45)
            self.t.fd(self.size / 2)
            self.t.dot(dotsize, self.dotcolor)
            self.t.right(90)
            self.t.fd(self.size / 2)
            self.t.dot(dotsize, self.dotcolor)
            self.t.right(90)
            self.t.fd(self.size / 2)
            self.t.dot(dotsize, self.dotcolor)
            self.t.right(135)
            self.t.fd(diag / 4)
        elif val == 6:
            self.t.right(45)
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(self.size / 4)
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(self.size / 4)
            self.t.dot(dotsize, self.dotcolor)
            self.t.left(90)
            self.t.fd(self.size / 2)
            self.t.left(90)
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(self.size / 4)
            self.t.dot(dotsize, self.dotcolor)
            self.t.fd(self.size / 4)
            self.t.dot(dotsize, self.dotcolor)


def draw_a_die():
    size = window.numinput("Dice", "What size do you want your die?", default=200)
    posx = window.numinput("Dice", "What is the x-position of your die?", default=0)
    posy = window.numinput("Dice", "What is the y-position of your die?", default=0)

    die = Dice(int(size), (int(posx), posy))
    print("Die position: x: %d y: %d \nDie size: %d" % (die.position[0], die.position[1], die.size))
    die.roll()
    print("Roll: ", die.current_value)
    # die.set_dice_color('black')
    # die.set_dot_color('white')
    die.draw()


if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(1000, 1000)
    window.bgcolor("#CFD8DC")

    draw_a_die()
    window.exitonclick()
