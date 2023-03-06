import sys
import math

"""
CSCI-603 - Homework 9
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 9 to implement program to design "Holi Cow!" using Graph Concepts.
"""

# Run related messages
HOLI_COW_START_MSG = "Field of Dreams\n---------------\n"

# Simulation related messages
SIMULATION_START_MSG = "\nBeginning simulation..."
PAINTBALL_TRIGGER_MSG = "Triggering {} paint ball..."
COW_PAINTED_MSG = '\t{} is painted {}!'
PAINTBALL_TRIGGERED_FROM_OTHER_MSG = "\t{} paint ball is triggered by {} paint ball"

# Results related messages
RESULTS_MSG = "\nResults: "
BEST_CHOICE_INFO_MSG = "Triggering the {} paint ball is the best choice with {} total paint on the cows:"
COW_PAINT_INFO_MSG = "\t{} colors: {}"
NO_COWS_PAINTED_MSG = "No cows were painted by any starting paint ball!"


def create_holi_cow_field(lines):
    """
    Create graph representing holi cow from the information lines about cows and paintball read from the file.
    :param lines: list of string information about cows and paintball.
    :return: Graph Object representing holi cow field.
    """

    graph_obj = Graph()
    total_length = len(lines)
    for src in range(0, total_length):

        src_info = split_lines_and_format(lines[src])
        graph_obj.add_vertex((src_info[0], src_info[1]))

        if src_info[0] == 'cow':
            continue

        for dest in range(0, total_length):
            if src == dest:
                continue

            dest_info = split_lines_and_format(lines[dest])
            if validate_points(src_info[2], src_info[3], dest_info[2], dest_info[3], src_info[4]):
                graph_obj.add_edge((src_info[0], src_info[1]), (dest_info[0], dest_info[1]), 1)

    return graph_obj


def get_count_of_cows_painted(color_dict):
    """
    Get total number of cows painted in the current trigger.
    :param color_dict: dictionary of cows painted.
    :return: number of cows painted in the current trigger.
    """

    count = 0
    for cow in color_dict:
        count += len(color_dict[cow])
    return count


def trigger_paint_balls_in_field(graph):
    """
    Trigger the chain reaction from all the paintball present in the holi cow field.
    :param graph: graph object representing holi cow field.
    :return: Tuple of info about maximum number of cows painted, maximum number of cows painted and color.
    """

    max_painted_cows_count = 0
    max_painted_color = None
    max_painted_cows_info = {}

    print(SIMULATION_START_MSG)
    for vertex in graph.vertices:
        if vertex[0] == 'cow':
            continue

        print(PAINTBALL_TRIGGER_MSG.format(vertex[1]))
        visited_nodes = graph.depth_first_traversal(vertex)
        current_painted_cows_count = get_count_of_cows_painted(visited_nodes)

        if current_painted_cows_count > max_painted_cows_count:
            max_painted_cows_count = current_painted_cows_count
            max_painted_color = vertex[1]
            max_painted_cows_info = visited_nodes

    return max_painted_cows_info, max_painted_cows_count, max_painted_color


def start_holi_cow(lines_list):
    """
    Runs holi cow simulation. Creates holi cow field, triggers paint balls and display simulation results
    :param lines_list: List of paint balls and cows information read from the file.
    :return: None.
    """

    print(HOLI_COW_START_MSG)
    holi_cow_field = create_holi_cow_field(lines_list)
    display_field_information(holi_cow_field)

    painted_cows_info, painted_cows_count, most_painted_color = trigger_paint_balls_in_field(holi_cow_field)
    print_simulation_results(painted_cows_info, painted_cows_count, most_painted_color)


def split_lines_and_format(line):
    """
    Extract information of cow or paintball from line string read from the file.
    :param line: information of cow or paintball read from the file.
    :return: tuple of { category(cow or paintball), name, x co-ordinate, y co-ordinate, radius(only for paintball) }
    """
    raw_values = line.strip().split()
    if raw_values[0] == 'cow':
        return [raw_values[0], raw_values[1], float(raw_values[2]), float(raw_values[3])]
    else:
        return [raw_values[0], raw_values[1], float(raw_values[2]), float(raw_values[3]), float(raw_values[4])]


def validate_points(x_1, y_1, x_2, y_2, radius):
    """
    Function to check if the points are within the given radius.
    :param x_1: x co-ordinate of the first point in the field.
    :param y_1: x co-ordinate of the first point in the field.
    :param x_2: x co-ordinate of the first point in the field.
    :param y_2: x co-ordinate of the first point in the field.
    :param radius: radius of the impact area.
    :return: boolean indicating the point 1 is within radius distance of point 2.
    """

    distance = math.sqrt(math.pow((y_2 - y_1), 2) + math.pow((x_2 - x_1), 2))
    return distance <= radius


def display_field_information(holi_cow_field):
    """
    Display details of the holi cow field.
    :param holi_cow_field: graph containing all the paint balls and cows.
    :return: None
    """

    for vertex in holi_cow_field.vertices:
        print(holi_cow_field.vertices.get(vertex))


def validate_given_cl_arguments(argument_list):
    """
    Function to validate the given Command Line arguments. Expected Usage: python3 holicow.py filename
    :param argument_list: List of arguments given from Command Line.
    :return: Boolean indicating if correct number of arguments are given in Command line.
    """
    return len(argument_list) == 2


def read_data_from_file(file_name):
    """
    Read data from file.
    :param file_name: file name to be read.
    :return: List of Lines.
    """
    all_lines = []
    with open(file_name) as input_file:
        for line in input_file:
            all_lines.append(line.strip())

    return all_lines


def print_simulation_results(painted_cows_info, painted_cows_count, most_painted_color):
    """
    Display simulation results for the run. Based on the painted cows count, two different messages can be displayed.
    :param painted_cows_info: dictionary containing information about the cows painted.
    :param painted_cows_count: number of cows painted.
    :param most_painted_color: color that resulted in most cows getting painted.
    :return: None
    """

    print(RESULTS_MSG)
    if painted_cows_count == 0:
        print(NO_COWS_PAINTED_MSG)
    else:
        print(BEST_CHOICE_INFO_MSG.format(most_painted_color, painted_cows_count))
        for cow in painted_cows_info:
            print(COW_PAINT_INFO_MSG.format(cow, painted_cows_info[cow]))


class Graph(object):

    def __init__(self):
        self.vertices = {}
        self.number_of_vertices = 0

    def add_edge(self, source, destination, cost=0):
        if source not in self.vertices:
            self.vertices[source] = Vertex(source)
            self.number_of_vertices += 1
        if destination not in self.vertices:
            self.vertices[destination] = Vertex(destination)

        self.vertices[source].add_neighbor(self.vertices[destination], cost)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
            self.number_of_vertices += 1

    def __depth_first_traversal(self, src_node, visited_nodes, cow_paint_dict):

        if src_node is None:
            return

        visited_nodes.add(src_node)
        for neighbor in src_node.get_connections():
            if neighbor.key[0] == 'cow' or neighbor not in visited_nodes:
                if neighbor.key[0] == 'cow':
                    print(COW_PAINTED_MSG.format(neighbor.key[1], src_node.key[1]))
                    if neighbor.key[1] not in cow_paint_dict:
                        cow_paint_dict[neighbor.key[1]] = {src_node.key[1]}
                    else:
                        cow_paint_dict[neighbor.key[1]].add(src_node.key[1])
                else:
                    print(PAINTBALL_TRIGGERED_FROM_OTHER_MSG.format(neighbor.key[1], src_node.key[1]))
                self.__depth_first_traversal(neighbor, visited_nodes, cow_paint_dict)

    def depth_first_traversal(self, src_node):

        visited_nodes = set()
        cow_paint_dict = {}
        self.__depth_first_traversal(self.vertices[src_node], visited_nodes, cow_paint_dict)
        return cow_paint_dict


class Vertex(object):

    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, neighbor):
        return self.connected_to.get(neighbor, "Neighbor not found")

    def __str__(self):
        if isinstance(self.key, tuple):
            return str(self.key[1]) + " connectedTo: " + str([str(x.key[1]) for x in self.connected_to])
        else:
            return str(self.key) + " connectedTo: " + str([str(x.key) for x in self.connected_to])


def main():
    """
    Main function. Checks few requirements and triggers holi cow simulation.
    :return: status of the execution
    """
    if not validate_given_cl_arguments(sys.argv):
        print("Usage: python3 holicow.py filename")
        return

    file_name = sys.argv[1]
    try:
        lines_list = read_data_from_file(file_name)
    except FileNotFoundError as _:
        print("File not found: {}".format(file_name))
        return

    start_holi_cow(lines_list)


if __name__ == '__main__':
    main()
