import turtle
import random
import math

"""
CSCI-603 - Homework 3
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 3 to design "Paint Snake" using turtle library and recursive and iterative method.
"""

MAX_SEGMENT = 500  # Maximum number of Segments allowed in drawing the Snake
BOUNDING_BOX = 200  # Size of the Bounding box which acts as a Boundary to contain the Snake.
MAX_LENGTH = 20  # Upper limit for each Segment's length.
MAX_THICKNESS = 10  # Upper limit for each Segment's thickness
MAX_ANGLE = 30  # Absolute value of Maximum angle that turtle can turn after drawing each segment
DIST_BTW_WORLD_N_BOUNDING_BOX = 100  # Distance between world co-ordinates and
TURTLE_PARAMETERS = {'TOTAL_ANGLE_TURNED': 0}  # Parameters of turtle. Contains copy of total angle turned by turtle.
ANGLE_OF_ROTATION_ON_BORDER = 180  # Angle to rotate whenever the turtle movement is about to cross the bounding box.


def init():
    """
    Initialize for drawing.
    Draws the bounding box with co-ordinates - (-BOUNDING_BOX, -BOUNDING_BOX) & (BOUNDING_BOX, BOUNDING_BOX)
    (-DIST_BTW_WORLD_N_BOUNDING_BOX - BOUNDING_BOX, -DIST_BTW_WORLD_N_BOUNDING_BOX - BOUNDING_BOX) is the lower left.
    (DIST_BTW_WORLD_N_BOUNDING_BOX + BOUNDING_BOX, DIST_BTW_WORLD_N_BOUNDING_BOX + BOUNDING_BOX) is the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    corner_co_ordinate = DIST_BTW_WORLD_N_BOUNDING_BOX + BOUNDING_BOX
    turtle.setworldcoordinates(-corner_co_ordinate, -corner_co_ordinate, corner_co_ordinate, corner_co_ordinate)
    turtle.setheading(0)
    turtle.speed(8)
    turtle.up()
    draw_bounding_box()
    turtle.goto(0, 0)
    turtle.hideturtle()
    turtle.down()


def get_turtle_pen_details():
    """
    Function to get the turtle pen details selected at random.
    Pen size is the thickness of the segment drawn by the turtle.
    Pen color is tuple of (red, green, blue). Using random for each segment of the color to generate a random shade.
    :return: Tuple of pen size and pen color (pen size, pen color) for drawing the next line segment.
    """

    pen_size = random.randint(0, MAX_THICKNESS)
    pen_color = (random.random(), random.random(), random.random())
    return pen_size, pen_color


def check_if_turtle_goes_beyond(movement_length):
    """
    Function to check if the turtle will move out of the bounding box with if it moves by the distance 'movement_length'
    Takes the current position of the turtle(current_x,current_y), calculates proposed new position using below logic
    destination_x = current_x + proposed movement_length * cos(rotation_angle)
    destination_y = current_y + proposed movement_length * cos(rotation_angle)
    after calculating the destination co-ordinate, checks if it's still within the bounding box.
    :return: True if the new position after moving by movement_length makes turtle cross the bounding box.
    """
    current_x, current_y = turtle.position()
    angle_turned_from_north = (TURTLE_PARAMETERS['TOTAL_ANGLE_TURNED'] + 360) % 360
    destination_x = current_x + movement_length * math.cos(math.radians(angle_turned_from_north))
    destination_y = current_y + movement_length * math.sin(math.radians(angle_turned_from_north))
    return abs(destination_x) > BOUNDING_BOX or abs(destination_y) > BOUNDING_BOX


def move_to_left_corner_of_bounding_box():
    """
    Function to get to the corner of the bounding box from (0,0)
    pre: pos (0,0), heading (east), up
    post: pos (-BOUNDING_BOX, -BOUNDING_BOX), heading (east), up
    :return: None
    """
    turtle.back(BOUNDING_BOX)
    turtle.right(90)
    turtle.forward(BOUNDING_BOX)
    turtle.left(90)


def draw_bounding_box():
    """
    Function to draw the Bounding box which is used as the boundary while drawing the snake.
    :pre: pos (-BOUNDING_BOX,-BOUNDING_BOX), heading (east), up
    :post: post(-BOUNDING_BOX, -BOUNDING_BOX). heading (east), up
    :return: None
    """
    move_to_left_corner_of_bounding_box()
    turtle.down()
    for i in range(4):
        turtle.forward(2 * BOUNDING_BOX)
        turtle.left(90)
    turtle.up()


def get_next_segment_length():
    """
    Function to get the next segment length for the turtle while drawing the Snake segment.
    The value will be always between (0, MAX_LENGTH)
    :return: random integer between (0, Max length)
    """

    movement_length = random.randint(0, MAX_LENGTH)
    return movement_length


def get_next_segment_turn_angle():
    """
    Function to get the turn angle for the turtle while drawing the Snake segment.
    The value will always be between (-MAX_ANGLE, MAX_ANGLE)
    :return: random Integer between (-MAX_ANGLE, MAX_ANGLE
    """
    turn_angle = random.randint(-MAX_ANGLE, MAX_ANGLE)
    return turn_angle


def update_snake_parameters(turn_angle):
    """
    Function to update the Turtle parameters while drawing the snake segment.
    - Adds the current turn angle to the total angle turned by the turtle since the begin.
    :param turn_angle: angle that turtle has turned previously.
    :return: None
    """
    TURTLE_PARAMETERS['TOTAL_ANGLE_TURNED'] = TURTLE_PARAMETERS['TOTAL_ANGLE_TURNED'] + turn_angle


def reset_snake_parameters():
    """
    Function to reset the Turtle parameters while drawing the snake segment.
    - Resets Total Angle turned by the turtle to 0.
    :return: None
    """
    TURTLE_PARAMETERS['TOTAL_ANGLE_TURNED'] = 0


def drawSnakeRec(segments):
    """
    Function to draw the snake using recursion approach.
    - Performs segment check. If 0, sets the turtle tail position, and returns 0 as total length moved.
    - Gets random pen thickness and pen color.
    - Gets random segment length to draw, angle to turn.
    - Checks if the turtle goes beyond the bounding box with the new segment length and new angle.
    - If check fails, it keeps picking random segment length and 180 angle to change the direction.
    - Once check passes, turtle moves forward by segment length, turns by turn angle, updates total angle rotated.
    - Calls drawSnakeRec with segment-1 recurrsively to draw the remaining segments and adds total length to it.
    :param segments: Number of segments that needs to be drawn as part of the snake drawing.
    :return: Length of the segment drawn till the point.
    """
    if segments == 0:
        turtle.up()
        return 0
    pen_size, pen_color = get_turtle_pen_details()
    movement_length = get_next_segment_length()
    turn_angle = get_next_segment_turn_angle()

    while check_if_turtle_goes_beyond(movement_length):
        movement_length = get_next_segment_length()
        turn_angle = ANGLE_OF_ROTATION_ON_BORDER

    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.forward(movement_length)
    turtle.left(turn_angle)
    update_snake_parameters(turn_angle)
    return drawSnakeRec(segments - 1) + movement_length


def drawSnakeIter(segments):
    """
    Function to draw the snake using Iterative approach. Performs below steps iteratively for segment no of times.
    - Gets random pen thickness and pen color.
    - Gets random segment length to draw, angle to turn.
    - Checks if the turtle goes beyond the bounding box with the new segment length and new angle.
    - If check fails, it keeps picking random segment length and 180 angle to change the direction.
    - Once check passes, turtle moves forward by segment length, turns by turn angle, updates total angle rotated.
    :param segments: Number of segments that needs to be drawn as part of the snake drawing.
    :return: Length of all the segment drawn till the point.
    """

    total_movement_length = 0
    reset_snake_parameters()

    for i in range(segments):
        pen_size, pen_color = get_turtle_pen_details()
        segment_length = get_next_segment_length()
        turn_angle = get_next_segment_turn_angle()

        while check_if_turtle_goes_beyond(segment_length):
            segment_length = get_next_segment_length()
            turn_angle = ANGLE_OF_ROTATION_ON_BORDER

        turtle.pensize(pen_size)
        turtle.pencolor(pen_color)
        turtle.forward(segment_length)
        turtle.left(turn_angle)
        update_snake_parameters(turn_angle)
        total_movement_length += segment_length

    turtle.up()
    return total_movement_length


def get_user_input():
    """
    Function to get the user input segments. Checks if the user input is between [0, MAX_SEGMENT].
    Keeps waiting till correct input is entered by the user.
    :return: segment_count -> int.
    """
    segment_count = -1
    while segment_count < 0:
        input_from_user = int(input("Segments (0-500): "))
        if 0 <= input_from_user <= MAX_SEGMENT:
            segment_count = input_from_user
        else:
            print("Segments must be between 0 and 500 inclusive. Try again.")
    return segment_count


def main():
    """
    Main function. Simulates snake segment drawing using recursive and iterative methods.
    :return: None
    """
    init()
    segment_count = get_user_input()
    snake_length = drawSnakeRec(segment_count)
    print("The snake's length is {} units.".format(snake_length))
    _ = input("Snake is complete. Please press Enter to continue.")
    turtle.reset()
    init()
    snake_length = drawSnakeIter(segment_count)
    print("The snake's length is {} units.".format(snake_length))
    _ = input("Snake is complete. Please press Enter to exit.")


if __name__ == '__main__':
    main()
