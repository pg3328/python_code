"""
CSCI-603 - Homework 7
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 7 to implement Node class used in "You are a Genetic Engineer" in DNAList class.
"""


class Node(object):

    def __init__(self, value, link=None):
        if len(value) > 1 or value not in ['A', 'C', 'G', 'T']:
            raise Exception("Invalid length or Invalid character provided as part of the function call")

        self.value = value
        self.link = link

    def __str__(self):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.value)

    def __repr__(self):
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr(self.value) + "," + repr(self.link) + ")"
