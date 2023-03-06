import unittest
from trie import Trie

"""
CSCI-603 - Homework 8
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 7 to test all possible cases in "Longest Prefix Matching" assignment. 
"""


class MyTestCase(unittest.TestCase):

    def test_insert(self):
        # Base Case - 1 - Trying to insert None and empty('') string -> Returns False
        trie = Trie()
        self.assertFalse(trie.insert(''))
        self.assertFalse(trie.insert(None))

        # Base Case - 2 - Adding one element and check if the root value is the string.
        trie = Trie()
        trie.insert('001010')
        self.assertEqual(trie.root.value, '001010')

        # Base Case - 3 - Adding one element by passing list during object creation and checking if root is the string.
        trie = Trie(['001010'])
        self.assertEqual(trie.root.value, '001010')

        # Base Case - 4 - Adding 0 and 1 and checking if the elements are left and right to the root.
        trie = Trie(['0'])
        trie.insert('1')
        self.assertEqual(trie.root.left.value, '0')
        self.assertEqual(trie.root.right.value, '1')

        # Base Case - 5 - Adding 00, 01, 10, 11 and checking if elements are inserted at level 2 in increasing order.
        trie = Trie(['00', '01', '10', '11'])
        self.assertEqual(trie.root.left.left.value, '00')
        self.assertEqual(trie.root.left.right.value, '01')
        self.assertEqual(trie.root.right.left.value, '10')
        self.assertEqual(trie.root.right.right.value, '11')

        # Base Case - 6 - Checking all combinations by inserting repeatedly various strings.
        trie = Trie(["001010", "000111", "111000", "111000", "010000", '110001'])
        self.assertEqual(trie.root.left.left.right.value, '001010')
        self.assertEqual(trie.root.left.left.left.value, '000111')
        self.assertEqual(trie.root.right.right.right.value, '111000')
        self.assertEqual(trie.root.left.right.value, '010000')
        self.assertEqual(trie.root.right.right.left.value, '110001')

    def test_height(self):
        # Base Case - 1 - Trying to insert empty('') string and check if height is -1 as root is None -> Returns -1.
        trie = Trie()
        trie.insert('')
        self.assertEqual(trie.height(), -1)

        # Base Case - 2 - Adding one element and check if the height is zero - just the root case -> returns 0.
        trie = Trie(['001010'])
        self.assertEqual(trie.height(), 0)

        # Base Case - 3 - Adding 0 and 1 and checking if the height is 1.
        trie = Trie(['0', '1'])
        self.assertEqual(trie.height(), 1)

        # Base Case - 4 - Adding 00, 01, 10, 11 and checking if elements are inserted at level 2 in increasing order.
        trie = Trie(['00', '01', '10', '11'])
        self.assertEqual(trie.height(), 2)

        # Base Case - 5 - Checking all combinations by inserting repeatedly various strings.
        trie = Trie(["001010", "000111", "111000", "111000", "010000", '110001'])
        self.assertEqual(trie.height(), 3)

        # Base Case - 6 - Checking all combinations by inserting repeatedly various strings.
        trie = Trie(["001010", "000111", "111000", "111000", "010000"])
        self.assertEqual(trie.height(), 3)

    def test_size(self):
        # Base Case - 1 - Trying to insert empty('') string and check if height is -1 as root is None -> Returns -1.
        trie = Trie()
        trie.insert('')
        self.assertEqual(trie.size(), 0)

        # Base Case - 2 - Adding one element and check if the height is zero - just the root case -> returns 0.
        trie = Trie(['001010'])
        self.assertEqual(trie.size(), 1)

        # Base Case - 3 - Adding 0 and 1 and checking if the height is 1.
        trie = Trie(['0', '1'])
        self.assertEqual(trie.size(), 2)

        # Base Case - 4 - Adding 00, 01, 10, 11 and checking if the size is correctly matching to 4.
        trie = Trie(['00', '01', '10', '11'])
        self.assertEqual(trie.size(), 4)

        # Base Case - 5 - Adding 5 strings not in a balanced Trie to see if size is handling this case and matching to 5.
        trie = Trie(["001010", "000111", "111000", "010000", '110001'])
        self.assertEqual(trie.size(), 5)

        # Base Case - 6 - Inserting duplicates and checking if the size matches with the node count in the Trie to 4.
        trie = Trie(["001010", "000111", "111000", "111000", "010000"])
        self.assertEqual(trie.size(), 4)

    def test_get_all(self):
        # Base Case - 1 - Trying to insert empty('') and check if the get_all also returns empty list.
        trie = Trie()
        trie.insert('')
        self.assertEqual(trie.get_all(), [])

        # Base Case - 2 - Adding one element which is present at root and checking if only one element is returned correctly.
        trie = Trie(['001010'])
        self.assertEqual(trie.get_all(), ['001010'])

        # Base Case - 4 - Adding 0 and 1 and checking if the balanced Trie gives the output in correct increasing order.
        trie = Trie(['0', '1'])
        self.assertEqual(trie.get_all(), ['0', '1'])

        # Base Case - 4 - checking against height - 2 Trie to make sure order of the strings are expected.
        trie = Trie(['10', '01', '00', '11'])
        self.assertEqual(trie.get_all(), ['00', '01', '10', '11'])

        # Base Case - 5 - checking against Trie which is not balanced and have multiple internal node to make sure internal node is not added in the output.
        trie = Trie(["001010", "000111", "111000", "010000", '110001'])
        self.assertEqual(trie.get_all(), ['000111', "001010", "010000", "110001", "111000"])

    def test_largest(self):
        # Base Case - 1 - Trying to get largest from empty Trie and checking if the output is None.
        trie = Trie()
        trie.insert('')
        self.assertEqual(trie.largest(), None)

        # Base Case - 2 - Trying to get the largest from Trie which has only one value and checking if the output is same string.
        trie = Trie(['001010'])
        self.assertEqual(trie.largest(), '001010')

        # Base Case - 4 - Adding 0 and 1 and checking if the balanced Trie gives the expected output.
        trie = Trie(['0', '1'])
        self.assertEqual(trie.largest(), '1')

        # Base Case - 4 - checking against height - 2 Trie to make sure output is the right-most node.
        trie = Trie(['10', '01', '00', '11'])
        self.assertEqual(trie.largest(), '11')

        # Base Case - 5 - checking against Trie with only left node at root level to see if no-right case is handled.
        trie = Trie(["001010", "000111", ])
        self.assertEqual(trie.largest(), "001010")

        # Base Case - 6 - checking against Trie which has only one node on right at root Level.
        trie = Trie(["001010", "000111", "111000"])
        self.assertEqual(trie.largest(), "111000")

        # Base Case - 5 - checking against Trie which is not balanced and have multiple internal node to make sure internal node is not added in the output.
        trie = Trie(["001010", "000111", "111000", "010000", '110001'])
        self.assertEqual(trie.largest(), "111000")

    def test_smallest(self):
        # Base Case - 1 - Trying to get smallest from empty Trie and checking if the output is None.
        trie = Trie()
        trie.insert('')
        self.assertEqual(trie.smallest(), None)

        # Base Case - 2 - Trying to get the smallest from Trie which has only one value and checking if the output is same string.
        trie = Trie(['001010'])
        self.assertEqual(trie.smallest(), '001010')

        # Base Case - 4 - Adding 0 and 1 and checking if the balanced Trie gives the expected output.
        trie = Trie(['0', '1'])
        self.assertEqual(trie.smallest(), '0')

        # Base Case - 4 - checking against height - 2 Trie to make sure output is the left-most node.
        trie = Trie(['10', '01', '00', '11'])
        self.assertEqual(trie.smallest(), '00')

        # Base Case - 5 - checking against Trie with only left node at root level to see if no-right case is handled.
        trie = Trie(["111000", "110001"])
        self.assertEqual(trie.smallest(), "110001")

        # Base Case - 6 - checking against Trie which has only one node on right at root Level.
        trie = Trie(["001010", "000111", "111000"])
        self.assertEqual(trie.smallest(), "000111")

        # Base Case - 5 - checking against Trie which is not balanced and have multiple internal node to make sure internal node is not added in the output.
        trie = Trie(["001010", "000111", "111000", "010000", '110001'])
        self.assertEqual(trie.smallest(), "000111")

    def test_search(self):
        # Base Case - 1 - Trie is empty
        trie = Trie()
        self.assertIsNone(trie.search('00110'))

        # Base Case - 2 - Only one string in the Trie. Returns the same string irrespective of search String.
        trie = Trie(['11'])
        self.assertEqual(trie.search('00'), '11')

        # Base Case - 3 - Balanced Trie - Search on the left side of the Trie. Returns leftmost available value.
        trie = Trie(['11', '10'])
        self.assertEqual(trie.search('00'), '10')

        # Base Case - 4 - Balanced Trie - Search on the right side of the Trie. Returns rightmost available value.
        trie = Trie(['11', '10'])
        self.assertEqual(trie.search('11'), '11')

        # Base Case - 5 - Test the corner cse - search the lexicographically smallest possible string. The output should be smallest value in the Trie.
        trie = Trie(["001010", "000111" ])
        self.assertEqual(trie.search('000000'), "000111")

        # Base Case - 6 - Test the corner case - search the lexicographically largest possible string. The output should be largest value in the Trie.
        trie = Trie(["001010", "000111"])
        self.assertEqual(trie.search('111111'), "001010")

        # Base Case - 7 - Test the corner case - search a string on the left side of the root but not present in the Trie.The output should be largest value in the Trie.
        trie = Trie(["001010", "000111"])
        self.assertEqual(trie.search('010000'), "001010")

        # Base Case - 8 - Test the corner case - search a string on the right side of the root but not present in the Trie.The output should be smallest nearest value in the Trie.
        trie = Trie(["001010", "000111", "111000", "010000", '110001'])
        self.assertEqual(trie.search('100010'), "110001")


if __name__ == '__main__':
    unittest.main()
