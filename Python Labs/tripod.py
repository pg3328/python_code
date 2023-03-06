from rit_sort import mergeSort
import sys

"""
CSCI-603 - Homework 2
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 5 to implement program to design "In the forest" using Turtle library
"""

CALC_DICTIONARY = {
    'E': [(0, 1), (-1, 0), (1, 0)],
    'W': [(0, -1), (-1, 0), (1, 0)],
    'N': [(-1, 0), (0, -1), (0, 1)],
    'S': [(1, 0), (0, -1), (0, 1)],
}


def read_grid_from_file(file_name):
    """
    Function to read the Rectangular grid from the file.
    :param file_name: Input file name which contains the Rectangular Grid.
    :return: Lists of Lists representing NxM Grid.
    """
    grid_list = []
    with open(file_name) as input_file:
        for line in input_file:
            row_values = list(map(int, line.strip().split()))
            grid_list.append(row_values)

    return grid_list


def get_row_and_column_count_of_grid(grid):
    """
    Function to get the Row and Column count from the Rectangular grid.
    :param grid: Rectangular grid.
    :return: Row count, Column count.
    """
    return len(grid), len(grid[0])


def get_requested_no_of_placements(tripod_list, input_count):
    """
    Function to get requested number of optimal tripod placement from the complete list.
    :param tripod_list: Sorted list of tripod placement.
    :param input_count: requested count of optimal tripod placement.
    :return: list of size input_count tripod placement.
    """
    return tripod_list[:input_count]


def validate_given_cl_arguments(argument_list):
    """
    Function to validate the given Command Line arguments. Expected Usage: python3 tripods.py filename
    :param argument_list: List of arguments given from Command Line.
    :return: Boolean indicating if correct number of arguments are given in Command line
    """
    return len(argument_list) == 2


def display_total_sum_of_placements(total):
    """
    Function to display the total sum of the all placements of the Tripod.
    :param total: Total sum of all the placements of the Tripod.
    :return: None.
    """
    print("Total: {}".format(total))


def get_user_request_count_of_tripods():
    """
    Function to get the user request count of the number of optimal tripods placements
    :return: Number of optimal tripods placements requested by the User.
    """
    number_of_tripods = input("Enter number of tripods:")
    return int(number_of_tripods)


def get_max_tripod_placement(row_count, column_count):
    """
    Function to calculate the maximum possible count of tripod placements.
    :param row_count: Number of rows in the rectangular puzzle grid.
    :param column_count: Number of columns in the rectangular puzzle grid.
    :return: Maximum possible count of tripod placements based on the row count and column count.
    """
    if row_count < 2 or column_count < 2:
        return 0
    else:
        return max((row_count * column_count) - 4, 0)


def get_total_sum_of_placements(requested_count_of_placements):
    """
    Function to get the total sum of all placements requested by the user.
    :param requested_count_of_placements: list of n top placement of tripods as requested by the user.
    :return: total sum of the all placements of tripods requested by the user.
    """
    total = 0
    print("Optimal placement:")
    for placement in requested_count_of_placements:
        print("loc: ({},{}), facing: {}, sum: {}".format(placement[0], placement[1], placement[3], placement[2]))
        total += placement[2]

    return total


def check_if_legs_are_in_grid(placement, row_count, column_count):
    """
    Check if the legs of the tripod placement is within the grid.
    :param placement: legs of the tripod placement.
    :param row_count: number of rows in the rectangular puzzle grid.
    :param column_count: number of column in the rectangular puzzle grid.
    :return: Boolean indicating if the point is within the rectangular puzzle grid.
    """
    for leg in placement:
        if (leg[0] >= row_count or leg[0] < 0) or (leg[1] >= column_count or leg[1] < 0):
            return False
    return True


def get_valid_tripod_placements(row_idx, column_idx, row_count, column_count):
    """
    Function to get valid tripod placements for a given point at (row_idx, column_idx)
    There are four possible values for tripod placements for every point.
    All four can be valid or invalid or any one point can be valid.
    :param row_idx: row index of the point
    :param column_idx: column index of the point.
    :param row_count: number of rows in the rectangular puzzle grid.
    :param column_count: number of column in the rectangular puzzle grid.
    :return: dictionary of valid direction and corresponding points in the rectangular puzzle grid.
    """
    valid_points = {}
    for direction in CALC_DICTIONARY:
        points_for_direction = CALC_DICTIONARY.get(direction)
        placement_points = [(row_idx + x[0], column_idx + x[1]) for x in points_for_direction]
        if check_if_legs_are_in_grid(placement_points, row_count, column_count):
            valid_points[direction] = placement_points

    return valid_points


def get_sum_for_placement(grid, placement):
    """
    Function to calculate sum of the legs for a given placement.
    :param grid: Rectangular puzzle grid.
    :param placement: placement of three legs for tripod.
    :return: sum of the values corresponding to three legs of the tripod placement.
    """
    value = 0
    for legs in placement:
        value += grid[legs[0]][legs[1]]
    return value


def find_optimal_placement_for_point(grid, row_idx, column_idx):
    """
    Function to find the optimal placement for the given point at (row_idx, column_idx)
    :param grid: Rectangular puzzle grid.
    :param row_idx: index of the row in the rectangular puzzle grid.
    :param column_idx: index of the column in the rectangular puzzle grid.
    :return: tuple of maximum value of the sum of the legs and corresponding direction.
    """
    max_value = -1
    max_value_direction = None
    row_count, column_count = get_row_and_column_count_of_grid(grid)
    valid_direction_points = get_valid_tripod_placements(row_idx, column_idx, row_count, column_count)
    for direction in valid_direction_points:
        point_value = get_sum_for_placement(grid, valid_direction_points[direction])
        if point_value > max_value:
            max_value = point_value
            max_value_direction = direction

    return max_value, max_value_direction


def get_optimal_place_for_grid(grid):
    """
    Function to get the optimal placement for all the points in the grid.
    :param grid: Rectangular puzzle grid.
    :return: List containing the optimal placement for all the points in the grid.
    """
    row_count, column_count = get_row_and_column_count_of_grid(grid)
    optimal_placement_list = []
    for row_idx in range(row_count):
        for column_idx in range(column_count):
            max_value, direction = find_optimal_placement_for_point(grid, row_idx, column_idx)
            optimal_placement_list.append((row_idx, column_idx, max_value, direction))
    return optimal_placement_list


def solve_tripod_puzzle(grid, user_input):
    """
    Function to solve the Tripod puzzle. Performs below steps -
    Calculates optimal tripod placement for all the points in the grid if any exists.
    Sorts the optimal tripod placement based on the sum for each point.
    Selects requested count of top tripod placements as per user's request and displays them and the total sum.
    :param grid: Rectangular puzzle grid.
    :param user_input: requested number of top tripod placements
    :return: None
    """
    optimal_placement_list = get_optimal_place_for_grid(grid)
    list_of_max_tripod_position = mergeSort(optimal_placement_list)
    requested_count_of_placements = get_requested_no_of_placements(list_of_max_tripod_position, user_input)
    total = 0
    if len(requested_count_of_placements) > 0:
        total = get_total_sum_of_placements(requested_count_of_placements)
    display_total_sum_of_placements(total)


def main():
    """
    Main function.
    :return: None
    """

    if not validate_given_cl_arguments(sys.argv):
        print("Usage: python3 tripods.py filename")
        return

    file_name = sys.argv[1]
    grid = read_grid_from_file(file_name)
    row_count, column_count = get_row_and_column_count_of_grid(grid)
    no_of_tripods_requested = get_user_request_count_of_tripods()
    max_tripod_possible = get_max_tripod_placement(row_count, column_count)

    if no_of_tripods_requested > max_tripod_possible:
        print("Too many tripods to place!")
        return

    solve_tripod_puzzle(grid, no_of_tripods_requested)


if __name__ == '__main__':
    main()
