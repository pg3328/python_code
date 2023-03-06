from node import Node

"""
CSCI-603 - Homework 7
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 7 to implement program to design "You are a Genetic Engineer" using Linked Lists.
"""


class DNAList(object):

    def __init__(self, gene=""):
        if not gene:
            self.head = None
            self.back = None
        else:
            self.head = Node(gene[0])
            temp = self.head
            for nucleotide in gene[1:]:
                next_node = Node(nucleotide)
                temp.link = next_node
                temp = next_node
            self.back = temp

    def is_empty(self):
        """
        Function to check if the current DNAList is empty.
        :return: boolean indicating if the list is empty.
        """
        return self.head is None

    def append(self, item):
        """
        Function to append one character to the gene.
        If the item is empty string or None, the function does nothing.
        :param item: Item to add to the back of the DNAList.
        :return: None
        """
        if not item:
            raise Exception("No valid character provided")

        new_node = Node(item)
        if self.is_empty():
            self.head = self.back = new_node
        else:
            self.back.link = new_node
            self.back = new_node

    def join(self, other):
        """
        Function to join the other gene to the DNAList.
        Creates a circular reference and behaves in unexpected if function is called repeatedly using same 'other'
        The code is not taking a copy of other.
        The solution might be changed to take a copy of 'other' at the beginning of the function to avoid this,
        but time complexity will be O(len(other)) instead of O(1).
        :param other: Other gene to join to the DNAList.
        :return: None
        """
        if self.is_empty():
            self.head = other.head
            self.back = other.back
        elif other.is_empty():
            return
        else:
            self.back.link = other.head
            self.back = other.back

    def splice(self, ind, other):
        """
        Function to insert the other DNAList immediately after the given index.
        1. If the index is less than or equal to 0, the other DNAList is inserted at the beginning.
        1. If the Index is greater the length of the current DNAList, the other DNAList is inserted at the end.
        2. If the DNAList is empty, the function adds the other DNAList
        :param ind: Index where the other DNAList needs to be inserted.
        :param other: DNAList which needs to be inserted.
        :return: None
        """

        if other.is_empty():
            return

        if self.is_empty():
            self.head = other.head
            self.back = other.back

        elif ind < 0:
            other.back.link = self.head
            self.head = other.head
        else:
            node_at_given_index = self.get_node_at_given_index(ind)
            if not node_at_given_index or node_at_given_index == self.back:
                self.back.link = other.head
                self.back = other.back
            else:
                other.back.link = node_at_given_index.link
                node_at_given_index.link = other.head

    def get_node_at_given_index(self, index):
        """
        Function to get the node at the given index
        :param index: integer representing the index value of the required node
        :return: Node object at the given the index
        """
        traverse_count = 0
        temp_node = self.head
        while traverse_count < index and temp_node is not None:
            traverse_count += 1
            temp_node = temp_node.link

        return temp_node

    @staticmethod
    def validate_indexes_for_snip(index_1, index_2):
        """
        Function to validate Indexes provided for snip function.
        1. If the index_1 is greater than index_2, it's considered as invalid.
        2. If the index_2 is <= 0, it's considered as invalid.
        3. If the index_1 == index_2, it's considered as invalid.
        :param index_1: starting position of the snipping. (Inclusive).
        :param index_2: ending position of the snipping. (Exclusive).
        :return: Boolean indicating whether the input indexes are valid.
        """
        if index_1 > index_2:
            return False
        if index_2 <= 0:
            return False
        if index_1 == index_2:
            return False
        return True

    def snip(self, index_1, index_2):
        """
        Function to remove the portion of the gene from index_1 till index_2.
        1. If the index_1 is greater than index_2, it's considered as invalid.
        2. If the index_2 is <= 0, it's considered as invalid.
        3. If the index_1 == index_2, it's considered as invalid.
        4. If the either of the index cross on either side of the List, it's considered as invalid.
        :param index_1: starting position of the snipping. (Inclusive).
        :param index_2: ending position of the snipping. (Exclusive).
        :return: None
        """
        if not self.validate_indexes_for_snip(index_1, index_2):
            raise ValueError("Invalid Indexes entered. Please provide valid inputs")

        traverse_count = 0
        temp_node = self.head
        while traverse_count < index_1-1 and temp_node is not None:
            traverse_count += 1
            temp_node = temp_node.link
        node_at_index_1 = temp_node

        while traverse_count < index_2-1 and temp_node is not None:
            traverse_count += 1
            temp_node = temp_node.link

        node_at_index_2 = temp_node

        if not node_at_index_1 or not node_at_index_2:
            raise ValueError("Invalid Index entered. Please provide valid inputs")

        if index_1 <= 0:
            self.head = node_at_index_2.link
            if node_at_index_2 == self.back:
                self.back = None
        else:
            node_at_index_1.link = node_at_index_2.link
            if node_at_index_2 == self.back:
                self.back = node_at_index_1

    def find_substring_in_dna(self, dna, rep_str):
        """
        Function to find substring in the dna
        :param dna: Strand of the DNA which needs to be searched.
        :param rep_str: substring which needs to be searched
        :return: boolean, DNA nucleotide marking the end of string match
        """
        if not rep_str or (len(rep_str) == 1 and dna.value == rep_str):
            return True, dna

        elif dna.value != rep_str[0]:
            return False, None
        else:
            return self.find_substring_in_dna(dna.link, rep_str[1:])

    def replace(self, rep_str, other):
        """
        Function to replace the the given part of the DNA with the other.
        1. If the rep_str is empty and current DNA Strand is not empty, Exception is raised.
        2. If the DNA Strand is empty, function returns without doing anything.
        3. If the DNA Strand and rep_str are equal, other is assigned directly to the current DNA strand.
        Else, first occurrence is marked and replaced with the other DNA Strand.
        :param rep_str: DNA string which needs to be replaced in the current DNA strand.
        :param other: the other DNA strand which replaces the substring
        :return: None
        """

        if not rep_str and not self.is_empty():
            raise Exception("Empty string replace is not allowed when the DNAList is not empty.")

        if self.is_empty() and rep_str:
            return

        if str(self) == rep_str:
            self.head = other.head
            self.back = other.back
            return

        # Check if the substring is found at the start
        temp = self.head
        found_flag, end_node = self.find_substring_in_dna(temp, rep_str)
        if found_flag:
            if other.is_empty():
                self.head = end_node.link
            else:
                self.head = other.head
                other.back.link = end_node.link
            if end_node == self.back:
                self.back = other.back

            return

        while temp.link is not None:
            found_flag, end_node = self.find_substring_in_dna(temp.link, rep_str)

            if not found_flag:
                temp = temp.link
                continue

            if other.is_empty():
                temp.link = end_node.link
                if end_node == self.back:
                    self.back = temp
            else:
                temp.link = other.head
                other.back.link = end_node.link

                if end_node == self.back:
                    self.back = other.back
            break

    def copy(self):
        """
        Function to return a new list same as the current one
        :return: DNAList same with same content as self.
        """
        return DNAList(str(self))

    def get_str_representation(self, node):
        """
        Function to get the string representation of the DNA
        :param node: start node.
        :return: String representation of the DNA.
        """

        if node is None:
            return ""
        else:
            return str(node.value) + self.get_str_representation(node.link)

    def __str__(self):
        """
        String Representation of the objects of the class.
        :return: string representation of the objects of the class.
        """
        return self.get_str_representation(self.head)


def main():
    """
    Main function
    """
    dna_obj = DNAList('GCT')
    print(dna_obj)


if __name__ == '__main__':
    main()
