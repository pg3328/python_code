"""
CSCI-603 - Homework 8
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 8 to implement program to design "Longest Prefix Matching" using Binary Tree.
"""


class TrieNode(object):
    def __init__(self, val, left=None, right=None):
        """
        Initialization of the Trie Node. left and right holds the "pointer" to the left TrieNode and rightNode in Tree.
        :param val: Value of the TrieNode.
        :param left: TrieNode to the left of the current node. Default value is None.
        :param right: TrieNode to the left of the current node. Default value is None.
        """

        self.value = val
        self.left = left
        self.right = right

    def is_leaf_node(self):
        """
        Checks if the TrieNode is a leaf node or not.
        :return: boolean indicating if the TrieNode is a leaf node.
        """

        return self.left is None and self.right is None


class Trie(object):

    def __init__(self, col=None):
        """
        Initialization of the Trie Data structure.
        :param col: List of Strings that needs to be inserted as part of the Trie during the initialization.
        """
        self.root = None
        if col is not None:
            for string in col:
                self.insert(string)

    def insert(self, value):
        """
        Insert a new String into the Trie. Please refer to __insert method description for further details.
        :param value: String value that needs to be inserted to the Trie.
        :return: boolean indicating if the insert was successful. False if the String is already present or null.
        """

        if not value:
            return False

        if self.root is None:
            self.root = TrieNode(value)
            return True

        return self.__insert(self.root, value, self.root.value, 0)

    def __insert(self, node, string1, string2, index):
        """
        Helper function for the insert.
        :param node: Current Node in the iteration.
        :param string1: String that needs to be inserted to the Trie
        :param string2: String value corresponding to the node.
        :param index: index in the String. Indicates the depth in the Trie.
        :return: boolean Indicating if the insert was successful.
        """

        if string1 == string2:
            return False

        if string2 is None:
            if string1[index] == "0":
                if node.left is None:
                    node.left = TrieNode(string1)
                    return True
                else:
                    return self.__insert(node.left, string1, node.left.value, index + 1)
            else:
                if node.right is None:
                    node.right = TrieNode(string1)
                    return True
                else:
                    return self.__insert(node.right, string1, node.right.value, index + 1)
        else:

            if string1[index] == string2[index]:
                node.value = None
                newnode = TrieNode(None)
                if string1[index] == "0":
                    node.left = newnode
                    a = self.__insert(node.left, string1, string2, index + 1)
                    if a is True:
                        return True
                else:
                    node.right = newnode
                    a = self.__insert(node.right, string1, string2, index + 1)
                    if a is True:
                        return True
            else:
                node.value = None
                if string1[index] == "0":
                    node.left = TrieNode(string1)
                    node.right = TrieNode(string2)
                else:
                    node.right = TrieNode(string1)
                    node.left = TrieNode(string2)
                return True

    @staticmethod
    def __get_all(node, string_list):
        """
        Helper function for get_all. If the node is None, no action is performed.
        Adds the leaf node recursively to the string_list in in-order fashion.
        :param node: Node of the Trie.
        :param string_list: Mutable object used to gather all the strings present in the Trie.
        :return: None.

        """

        if node is not None:
            Trie.__get_all(node.left, string_list)
            if node.value is not None:
                string_list.append(node.value)
                return
            Trie.__get_all(node.right, string_list)

    def get_all(self):
        """
        Function to get all the Strings present in the Trie.
        Refer to documentation of the helper function __get_all for details.
        :return: List of Strings present in the Trie.
        """
        string_list = []
        temp = self.root
        self.__get_all(temp, string_list)
        return string_list

    @staticmethod
    def __largest(node):
        """
        Helper function to find lexicographically largest String in the Trie.
        if the node is None, there are no more nodes.
        If there's a right Node or path, that is chosen to continue the search.
        If there's no right path and there's a left path, that is chosen to continue the search.
        If the node is the leaf node, we have reached the maximum. The value is returned
        :param node: Node in the Trie.
        :return: lexicographically largest String or None.
        """
        if node is None:
            return None

        if node.is_leaf_node():
            return node.value

        if node.right:
            return Trie.__largest(node.right)
        else:
            return Trie.__largest(node.left)

    def largest(self):
        """
        Function to get the lexicographically largest String in the Trie.
        Refer to documentation of the helper function __largest for details.
        :return: Lexicographically largest string in the Trie.
        """
        return self.__largest(self.root)

    @staticmethod
    def __smallest(node):
        """
        Helper function to find lexicographically smallest String in the Trie.
        if the node is None, there are no more nodes to search for. returns None.
        If there's a left node or path, that is chosen to continue the search.
        If there's no left path and there's a left path, that is chosen to continue the search.
        If the node is the leaf node, we have reached the minimum. The value is returned.
        :param node: Node in the Trie.
        :return: lexicographically largest String or None.
        """

        if node is None:
            return None

        if node.is_leaf_node():
            return node.value

        if node.left:
            return Trie.__smallest(node.left)
        else:
            return Trie.__smallest(node.right)

    def smallest(self):
        """
        Function to get the lexicographically smallest String in the Trie.
        Refer to documentation of the helper function __smallest for details.
        :return: Lexicographically largest string in the Trie.
        """
        return self.__smallest(self.root)

    def __search(self, node, value, index):
        """
        Helper function for search.
        If the Leaf Node is reached, that's the nearest string possible and value is returned.
        If there's no available node on left on seeing a '0', it picks up the smallest string available from that node.
        If there's no available node on right on seeing a '1', it picks up the largest string available from that node.
        :param node: Node in the Trie.
        :param value: String value that needs to be searched.
        :param index: index in the String. Indicates the depth in the Trie.
        :return: Lexicographically nearest string.
        """
        if node.value is not None:
            return node.value

        if value[index] == '0':
            if node.left is not None:
                return self.__search(node.left, value, index + 1)
            else:
                return self.__smallest(node)
        else:
            if node.right is not None:
                return self.__search(node.right, value, index + 1)
            else:

                return self.__largest(node)

    def search(self, st):
        """
        Function to search a String in the Trie. Returns Lexicographically nearest string.
        Returns None only if the Trie is empty. Refer to documentation of the helper function __search for details.
        :param st: Search String.
        :return: Lexicographically nearest string.

        """
        if self.root is None:
            return None
        if not st:
            return self.smallest()

        return self.__search(self.root, st, 0)

    @staticmethod
    def __size(node):
        """
        Helper function to get the size of the Trie.
        If the node is None, returns 1 else adds itself and recursively goes one level down.
        :param node: Node of Trie
        :return: size of the Trie.
        """

        if node is None:
            return 0
        if node.value is not None:
            return 1
        return Trie.__size(node.left) + Trie.__size(node.right)

    def size(self):
        """
        Function to get the size of the Trie. Refer to documentation of the helper function __size for details.
        :return: size of the Trie.
        """
        return self.__size(self.root)

    @staticmethod
    def __height(node):
        """
        Helper function to get the Height of the Trie. If the node is None, -1 is returned.
        Else, it adds itself and recursively calculates the maximum height of the left Trie or right Trie.
        :param node: Node of the Trie.
        :return: Height of the Trie
        """
        if node is None:
            return -1
        else:
            return 1 + max(Trie.__height(node.left), Trie.__height(node.right))

    def height(self):
        """
        Function to get the height of the Trie. Refer to documentation of the helper function __height for details.
        :return: Height of the Trie.
        """
        return self.__height(self.root)

    def __print_trie(self, node):
        """
        Helper function to Print the Trie in Pre-order format.
        :param node:
        :return: None
        """

        if node is not None:
            print(node.value)
            self.__print_trie(node.left)
            self.__print_trie(node.right)

    def print_trie(self):
        """
        Prints the Trie in Pre-Order format.
        :return: None
        """
        temp = self.root
        self.__print_trie(temp)


def main():
    trie = Trie(['00', '01', '10', '11'])
    trie.print_trie()


if __name__ == '__main__':
    main()
