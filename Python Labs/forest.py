import turtle
import random
import math

"""
CSCI-603 - Homework 2
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 2 to implement program to design "In the forest" using Turtle library
"""

PINE_TREE_MAX_TRUNK_LENGTH = 200
PINE_TREE_TOP_LENGTH = 25
MAPLE_TREE_MAX_TRUNK_LENGTH = 150
MAPLE_TREE_TOP_RADIUS = 20
SPECIAL_TREE_MAX_TRUNK_LENGTH = 150
SPECIAL_TREE_TOP_LENGTH = 20

DISTANCE_BETWEEN_TWO_OBJECTS = 100
MINIMUM_TRUNK_LENGTH = 50

NIGHT_HOUSE_WALL_LENGTH = 100
STAR_LENGTH = 15
STAR_POSITION_FROM_MAX_TREE = 10
SUN_DISTANCE_FROM_HOUSE = 40
SUN_POSITION_FROM_ROOF = 20
SUN_RADIUS = 30


def init():
    """
    Initialize for drawing.  (-50, -100) is in the lower left and
    (500, 450) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-50, -100, 500, 450)
    turtle.up()
    turtle.setheading(0)
    turtle.speed(5)


def get_side_count_and_length(tree_type):
    """
    Function to get the side count, and side length based on the Tree Type(Pine, Maple, Special)
    :param tree_type: Type of the tree(Pine, Maple, Special)
    :return: Side count, Tree top length
    """
    if tree_type == 'Pine':
        return 3, PINE_TREE_TOP_LENGTH
    elif tree_type == 'Maple':
        return 0, MAPLE_TREE_TOP_RADIUS
    elif tree_type == 'Special':
        return 4, SPECIAL_TREE_TOP_LENGTH
    else:
        return -1, 0


def wood_available_from_night(tree_height_list, house_present_in_night):
    """
    Function to calculate wood available from Night. It involves two parts wood from trees and wood from house.
    Wood from house is constant since wall length does not change.
    :param tree_height_list: List containing trunk length of all the trees present during the night (list[int]).
    :param house_present_in_night: If there was a house during the night (bool).
    :return: Total wood available from Night (float).
    """
    if house_present_in_night:
        wood_from_house = (2 * NIGHT_HOUSE_WALL_LENGTH) + (NIGHT_HOUSE_WALL_LENGTH * math.sqrt(2))
    else:
        wood_from_house = 0

    wood_from_trees = sum(tree_height_list)
    return wood_from_house + wood_from_trees


def calculate_length_of_walls(available_wood):
    """
    Function to calculate length of the walls for house in the morning based on wood available from night.
    calculation details - available_wood = 2* wall + wall * root(2)
                        - available_wood = wall (2 + root(2))
                        - wall = available/(2+root(2))
    :param available_wood: total available wood from the night (float).
    :return: Length of the Walls for the house during morning (float).
    """
    wall_length = available_wood / (2 + math.sqrt(2))
    return wall_length


def draw_polygon(side_count, side_length):
    """
    Function to draw the Regular polygon of n sides or circle.
    :pre: pos (distance * number_of_objects, trunk_length - side_length/2), heading (east), up
    :post: pos (distance * number_of_objects, trunk_length), heading (east), up
    :param side_count: Number of sides in the polygon. 0 in case of circle.
    :param side_length: Length of each side of the polygon. Radius in case of Circle
    :return: None
    """

    turtle.down()
    # Case for the circle
    if side_count == 0:
        turtle.circle(side_length)
    else:
        interior_angle = ((side_count - 2) * 180)/side_count
        for _ in range(side_count):
            turtle.forward(side_length)
            turtle.left(180 - interior_angle)
    turtle.up()


def draw_night_scene(tree_count, draw_house_confirmation):
    """
    Function to draw the Night scene. It draws N number of Trees, House if needed, and a Star.
    :pre: pos (0, 0), heading (east), up
    :post: pos (DISTANCE_BETWEEN_TWO_OBJECTS * ( n -1) objects, 0), heading (east), up
    :return: List of tree trunk length
    """
    tree_trunk_length_list = []
    house_position = 0 if tree_count == 1 else random.randint(1, tree_count - 1)
    total_number_of_objects_to_draw = tree_count + 1 if draw_house_confirmation else tree_count
    max_trunk_length = 0
    for i in range(total_number_of_objects_to_draw):
        if i == house_position and draw_house_confirmation:
            draw_house(NIGHT_HOUSE_WALL_LENGTH)
            turtle.down()
            turtle.forward(DISTANCE_BETWEEN_TWO_OBJECTS)
            turtle.up()
            continue

        tree_type, max_trunk_length = get_tree_type_and_max_length()
        random_trunk_length = random.randint(MINIMUM_TRUNK_LENGTH, max_trunk_length)
        tree_trunk_length_list.append(random_trunk_length)
        draw_trees(tree_type, random_trunk_length)
        turtle.down()
        if i != total_number_of_objects_to_draw-1:
            turtle.forward(DISTANCE_BETWEEN_TWO_OBJECTS)
        turtle.up()

    draw_star(max_trunk_length)
    return tree_trunk_length_list


def draw_house(wall_length):
    """
    Function to draw the house with 2 walls and 2 roofs.
    The two roofs are part of pentagon at 45 degree angle.
    :pre: pos (distance * number_of_objects, 0), heading (east), up
    :post: pos (distance * (number_of_objects + 1), 0), heading (east), up
    :param wall_length: length of each walls.
    :return: None
    """
    roof_length = (wall_length/2) * (math.sqrt(2))
    turtle.down()
    turtle.left(90)
    turtle.forward(wall_length)
    turtle.right(45)
    turtle.forward(roof_length)
    turtle.right(90)
    turtle.forward(roof_length)
    turtle.right(45)
    turtle.forward(wall_length)
    turtle.right(90)
    turtle.forward(wall_length)
    turtle.left(180)
    turtle.up()
    turtle.forward(wall_length)


def draw_trees(tree_type, trunk_length):
    """
    Function to draw the Trees. Based on Tree type, different shapes of tree tops are drawn.
    :pre: pos (distance * number_of_objects, 0), heading (east), up
    :post: pos (distance * (number_of_objects + 1), 0), heading (east), up
    :param tree_type: Type of the Tree (Pine, Maple, Special)
    :param trunk_length: Trunk length of the tree
    :return: None
    """
    side_count, side_length = get_side_count_and_length(tree_type)
    turtle.left(90)
    turtle.down()
    turtle.forward(trunk_length)
    turtle.up()
    turtle.right(90)
    if side_count != 0:
        turtle.back(side_length/2)

    draw_polygon(side_count, side_length)

    if side_count != 0:
        turtle.forward(side_length/2)

    turtle.right(90)
    turtle.forward(trunk_length)
    turtle.left(90)


def get_tree_type_and_max_length():
    """
    Function to pick a Tree in random and send the maximum trunk length details of the Tree.
    :return: Tree Type(Pine, Maple, Special) and MAX Trunk length
    """
    random_tree_type = random.choice(['Pine', 'Maple', 'Special'])

    if random_tree_type == 'Pine':
        max_length = PINE_TREE_MAX_TRUNK_LENGTH
    elif random_tree_type == 'Maple':
        max_length = MAPLE_TREE_MAX_TRUNK_LENGTH
    else:
        max_length = SPECIAL_TREE_MAX_TRUNK_LENGTH
    return random_tree_type, max_length


def draw_morning_scene(wall_length):
    """
    Function to draw the Morning scene. It draws a house, and a Sun.
    :pre: pos (0, 0), heading (east), up
    :post: pos (house_wall_length + distancesun radius, 0), heading (east), up
    :return: None
    """
    draw_house(wall_length)
    turtle.forward(SUN_DISTANCE_FROM_HOUSE)
    draw_sun(wall_length)


def draw_sun(wall_length):
    """
    Function to draw the Sun for morning scene.
    :pre: pos (wall_length + SUN_DISTANCE_FROM_HOUSE, 0), heading (east), up
    :post: pos (wall_length + SUN_DISTANCE_FROM_HOUSE, 0), heading (east), up
    :return: None
    """
    turtle.left(90)
    turtle.forward(wall_length + wall_length/2 + SUN_POSITION_FROM_ROOF + SUN_RADIUS)
    draw_polygon(0, SUN_RADIUS)
    turtle.back(wall_length + wall_length/2 + SUN_POSITION_FROM_ROOF + SUN_RADIUS)
    turtle.right(90)


def draw_star(tallest_tree_trunk_length):
    """
    Function to draw the Star for night scene.
    pre: pos (DISTANCE_BETWEEN_TWO_OBJECTS * ( n -1) objects, 0), heading (east), up
    :post: pos (DISTANCE_BETWEEN_TWO_OBJECTS * ( n -1) objects, 0), heading (east), up
    :param tallest_tree_trunk_length: Tallest of all the tree trunk drawn in night scene.
    :return: None
    """
    turtle.left(90)
    turtle.forward(tallest_tree_trunk_length + STAR_POSITION_FROM_MAX_TREE + STAR_LENGTH)
    turtle.down()
    for _ in range(8):
        turtle.forward(STAR_LENGTH)
        turtle.back(STAR_LENGTH)
        turtle.right(45)
    turtle.up()
    turtle.left(180)
    turtle.forward(tallest_tree_trunk_length + STAR_POSITION_FROM_MAX_TREE + STAR_LENGTH)
    turtle.left(90)


def get_night_scene_details():
    """
    Function to get the night scene details from the User.
    Get the details of how many trees and whether house needs to be drawn.
    :return: tree_count, draw_house_input
    """
    tree_count = int(input("How many trees in your forest?"))
    draw_house_input = input("Is there a house in the forest (y/n)?")
    draw_house_input = True if draw_house_input == "y" else False
    return tree_count, draw_house_input


def draw_forest():
    """
    Function to draw the "In the Forest". Draws the night scene, resets the screen and then draws the morning scene.
    :return: None
    """

    tree_count, draw_house_input = get_night_scene_details()
    tree_length_list = draw_night_scene(tree_count, draw_house_input)
    wood_from_night = wood_available_from_night(tree_length_list, draw_house_input)

    _ = input("Night is done, press enter for day")
    turtle.reset()

    print("We have {} units of lumber for building.".format(wood_from_night))
    morning_house_wall_length = calculate_length_of_walls(wood_from_night)
    print("We will build a house with walls {} tall.".format(morning_house_wall_length))
    draw_morning_scene(morning_house_wall_length)
    _ = input("Day is done, house is built, press enter to quit")


def main():
    """
    The main function
    :return: None
    """
    init()
    draw_forest()


if __name__ == '__main__':
    main()
