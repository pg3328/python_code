import turtle
import math

"""
 * This programme can draws a playing cards of different suits
 * such as hearts,diamonds. 
 * @author Pradeep Kumar Gontla"""


def card_borders():
    """
    used to draw the borders of the playing card.
    :return: NA
    """
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.up()
    turtle.forward(120)


def position(suit, flag):
    """
    used to position the turtle at appropriate points
    in order to complete the suit diagram
    :param suit: user input of the playing card
    :param flag: used to understand the position of suit
                 bottom: Have to draw suit shape at the left bottom of the card
                 middle: Have to draw suit shape at the middle of the card
                 top: Have to draw suit shape at the top of the card
    :return: NA
    """
    if suit == 'diamond':
        # used for positioning the turtle to draw the suit.
        if flag == "bottom":
            turtle.up()
            turtle.forward(10)
            scale = 2
            diamond(scale)
            turtle.right(225)
        elif flag == "top":
            scale = 2
            diamond(scale)
            turtle.right(45)
        elif flag == "middle":
            scale = 8
            diamond(scale)
            turtle.left(135)
    if suit == "heart":
        if flag == "bottom":
            turtle.forward(30)
            turtle.right(180)
            turtle.down()
            heart(2)
            turtle.up()
            turtle.right(210)
            turtle.forward(20)
            turtle.right(180)
        elif flag == "top":
            heart(2)
            turtle.right(30)
        elif flag == "middle":
            heart(8)
            turtle.left(150)


def heart(scale):
    """
    Used to draw a heart suit
    :param scale: used to scale the size of heart as desired
    :return: NA
    """
    turtle.up()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.right(30)
    turtle.forward(5 * scale * math.sqrt(2))
    turtle.left(30)
    turtle.circle(1.8 * scale, 180)
    turtle.right(180)
    turtle.circle(1.8 * scale, 180)
    turtle.left(30)
    turtle.forward(5 * scale * math.sqrt(2))
    turtle.end_fill()


def diamond(scale):
    """
    Used to draw a diamond suit
    :param scale:scales the size of heart as on when desired
    :return: NA
    """
    turtle.up()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(5 * math.sqrt(2) * scale)
    turtle.left(90)
    turtle.forward(5 * math.sqrt(2) * scale)
    turtle.left(90)
    turtle.forward(5 * math.sqrt(2) * scale)
    turtle.left(90)
    turtle.forward(5 * math.sqrt(2) * scale)
    turtle.end_fill()


def write(rank):
    """
    Used to write the rank of the card
    :param rank: User defined rank value of the card.
    :return: NA
    """
    turtle.color('red')
    turtle.write(rank, font=('Arial', 26, 'bold'), align='center')
    turtle.up()
    turtle.color('black')
    turtle.back(130)
    turtle.right(90)
    turtle.forward(80)
    turtle.down()


def pos(suit, rank):
    """
    Used to position the turtle inside a box with the universal reference
    and works as navigator for turtle.
    :param suit: User input of desired suit.
    :param rank: User input of desired rank
    :return: NA
    """
    card_borders()
    turtle.back(20)
    turtle.left(90)
    flag = "bottom"
    position(suit, flag)
    flag = "top"
    turtle.up()
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.down()
    position(suit, flag)
    flag = "middle"
    turtle.up()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.down()
    position(suit, flag)
    turtle.up()
    turtle.forward(80)
    turtle.down()
    write(rank)


def main():
    """
    Used for calling the functions and giving the user
    desired values to draw a card
    :return: NA
    """
    turtle.speed(5)
    turtle.setup(450,250)
    turtle.setworldcoordinates(-35,-5,250,150)
    pos('diamond', 'K')
    pos('heart', 'K')
    turtle.done()


if __name__ == "__main__":
    main()
