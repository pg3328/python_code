import unittest
from dnalist import DNAList

"""
CSCI-603 - Homework 7
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 7 to test all possible cases in "You are a Genetic Engineer". 
"""


class MyTestCase(unittest.TestCase):

    def test_is_empty(self):
        """Function to test DNAList.is_empty function"""

        # Case - 1 -> Single Character DNAList
        original_dna = DNAList('G')
        self.assertFalse(original_dna.is_empty())

        # Case - 2 -> Multiple Character DNAList
        original_dna = DNAList('GCT')
        self.assertFalse(original_dna.is_empty())

        # Case - 3 -> Empty DNAList
        original_dna = DNAList('')
        self.assertTrue(original_dna.is_empty())
        original_dna = DNAList()
        self.assertTrue(original_dna.is_empty())

    def test_append(self):
        """Function to test DNAList.append function"""

        # Case - 1 -> Append a character to a single character DNA
        original_dna = DNAList('A')
        original_dna.append('C')
        self.assertEqual(str(original_dna), 'AC')

        # Case - 2 -> Append a character to a bigger DNA
        original_dna = DNAList('ACGT')
        original_dna.append('C')
        self.assertEqual(str(original_dna), 'ACGTC')

        # Case - 3 -> Append a single character DNA to a empty DNA
        original_dna = DNAList()
        original_dna.append('C')
        self.assertEqual(str(original_dna), 'C')

        # Case - 4 -> Append a empty character to an empty DNA
        original_dna = DNAList()
        self.assertRaises(Exception, original_dna.append, '')

        # Case - 5 -> Multiple Append in sequence to empty DNA
        original_dna = DNAList()
        original_dna.append('G')
        original_dna.append('C')
        original_dna.append('T')
        self.assertEqual(str(original_dna), 'GCT')

    def test_join(self):
        """Function to test DNAList.join function"""

        # Case - 1 -> Join a single character DNA to a single character DNA
        original_dna = DNAList('G')
        other_dna = DNAList('C')
        original_dna.join(other_dna)
        self.assertEqual(str(original_dna), 'GC')

        # Case - 2 -> Join a single character DNA to multiple character DNA
        original_dna = DNAList('G')
        other_dna = DNAList('CT')
        original_dna.join(other_dna)
        self.assertEqual(str(original_dna), 'GCT')

        # Case - 3 -> Join a multiple character DNA to multiple character DNA
        original_dna = DNAList('GCT')
        other_dna = DNAList('CT')
        original_dna.join(other_dna)
        self.assertEqual(str(original_dna), 'GCTCT')

        # Case - 4 -> Join an empty DNA to an empty DNA
        original_dna = DNAList('')
        other_dna = DNAList('')
        original_dna.join(other_dna)
        self.assertEqual(str(original_dna), '')

        # Case - 5 -> Join an empty DNA to a non-empty DNA
        original_dna = DNAList('GCT')
        other_dna = DNAList('')
        original_dna.join(other_dna)
        self.assertEqual(str(original_dna), 'GCT')

        # Case - 6 -> Join a non-empty DNA to a empty DNA
        original_dna = DNAList('')
        other_dna = DNAList('GCT')
        original_dna.join(other_dna)
        self.assertEqual(str(original_dna), 'GCT')

        # Case - 7 -> Join multiple times same non-empty DNA in sequence to an empty DNA
        original_dna = DNAList('')
        other_dna = DNAList('GCT')
        original_dna.join(other_dna)
        original_dna.join(DNAList('GCT'))
        original_dna.join(DNAList('GCT'))
        self.assertEqual(str(original_dna), 'GCTGCTGCT')

    def test_splice(self):
        """Function to test DNAList.splice function"""

        # Case - 1 -> Splicing an empty DNAList to an empty DNAList.
        original_dna = DNAList('')
        other_dna = DNAList('')
        original_dna.splice(0, other_dna)
        self.assertEqual(str(original_dna), '')

        # Case - 2 -> Splicing an empty DNAList at beginning non-empty DNAList
        original_dna = DNAList('GCTA')
        other_dna = DNAList('')
        original_dna.splice(0, other_dna)
        self.assertEqual(str(original_dna), 'GCTA')

        # Case -3 -> Splicing an empty DNAList at end of an non-empty DNAList
        original_dna = DNAList('GCTA')
        other_dna = DNAList('')
        original_dna.splice(4, other_dna)
        self.assertEqual(str(original_dna), 'GCTA')

        # Case - 4 -> Splicing a non-empty DNAList at the beginning of an empty DNAList
        original_dna = DNAList('')
        other_dna = DNAList('GCTA')
        original_dna.splice(0, other_dna)
        self.assertEqual(str(original_dna), 'GCTA')

        # Case - 5 -> Splicing a non-empty DNAList at the beginning of a non-empty DNAList
        original_dna = DNAList('CTA')
        other_dna = DNAList('GCTA')
        original_dna.splice(0, other_dna)
        self.assertEqual(str(original_dna), 'CGCTATA')

        # Case - 6 -> Splicing a non-empty DNAList at the end of a DNAList
        original_dna = DNAList('GTA')
        other_dna = DNAList('GCTA')
        original_dna.splice(2, other_dna)
        self.assertEqual(str(original_dna), 'GTAGCTA')

        # Case - 7 -> Splicing an empty DNAList at negative Index of an non-empty DNAList
        original_dna = DNAList('GCTA')
        other_dna = DNAList('')
        original_dna.splice(-1, other_dna)
        self.assertEqual(str(original_dna), 'GCTA')

        # Case - 8 -> Splicing a non-empty DNAList at negative Index of an non-empty DNAList
        original_dna = DNAList('GCTA')
        other_dna = DNAList('GCTA')
        original_dna.splice(-1, other_dna)
        self.assertEqual(str(original_dna), 'GCTAGCTA')

        # Case - 9 -> Splicing a non-empty DNAList at the middle of an non-empty DNAList
        original_dna = DNAList('GCTA')
        other_dna = DNAList('GCTA')
        original_dna.splice(2, other_dna)
        self.assertEqual(str(original_dna), 'GCTGCTAA')

    def test_snip(self):
        """Function to test DNAList.snip function"""

        # Case - 1 -> Snip start index and end index both greater than length of the DNAList
        original_dna = DNAList('GCTA')
        self.assertRaises(ValueError, original_dna.snip, 4, 10)

        # Case - 2 -> Snip start index is less than length and end index is greater than length of the DNAList.
        original_dna = DNAList('GCTA')
        self.assertRaises(ValueError, original_dna.snip, 2, 10)

        # Case - 3 -> Snip start index and end index both less than 0.
        original_dna = DNAList('GCTA')
        self.assertRaises(ValueError, original_dna.snip, -3, -1)

        # Case - 4 -> Snip start index less than 0 and end index greater than 0 and less than length of the DNAList
        original_dna = DNAList('GCTA')
        original_dna.snip(-3, 2)
        self.assertEqual(str(original_dna), 'TA')

        # Case - 5 -> Snip start index less than 0 and end index greater than length of the DNAList
        original_dna = DNAList('GCTA')
        self.assertRaises(ValueError, original_dna.snip, -3, 7)

        # Case - 6 -> Snip with start and end index equal.
        original_dna = DNAList('GCTA')
        self.assertRaises(ValueError, original_dna.snip, 0, 0)

        # Case - 7 -> Snip start index is 0 and end index in total length of the DNAList.
        original_dna = DNAList('GCTA')
        original_dna.snip(0, 4)
        self.assertEqual(str(original_dna), '')

        # Case - 8 -> Snip start index is 0 and end index in total length-1 of the DNAList.
        original_dna = DNAList('GCTA')
        original_dna.snip(0, 3)
        self.assertEqual(str(original_dna), 'A')

    def test_replace(self):
        """Function to test DNAList.replace function"""

        # Case - 1 -> Replace empty string with empty DNAList in an empty DNAList.
        original_dna = DNAList('')
        replace_dna = DNAList('')
        original_dna.replace('', replace_dna)
        self.assertEqual(str(original_dna), '')

        # Case - 2 -> Replace empty string with single character DNAList in an empty DNAList.
        original_dna = DNAList('')
        replace_dna = DNAList('G')
        original_dna.replace('', replace_dna)
        self.assertEqual(str(original_dna), 'G')

        # Case - 3 -> Replace non-empty string with single character DNAList in an empty DNAList.
        original_dna = DNAList('')
        replace_dna = DNAList('GCT')
        original_dna.replace('G', replace_dna)
        self.assertEqual(str(original_dna), '')

        # Case - 4 -> Replace one existing character with empty DNAList in a single strand DNAList
        original_dna = DNAList('G')
        replace_dna = DNAList('')
        original_dna.replace('G', replace_dna)
        self.assertEqual(str(original_dna), '')

        # Case - 5 -> Replace empty string with a non-empty DNAList in a non-empty DNAList
        original_dna = DNAList('GCT')
        replace_dna = DNAList('ACT')
        self.assertRaises(Exception, original_dna.replace, '', replace_dna)

        # Case - 7 -> Replace a single character with a single strand DNAList in a single strand DNAList
        original_dna = DNAList('G')
        replace_dna = DNAList('C')
        original_dna.replace('G', replace_dna)
        self.assertEqual(str(original_dna), 'C')

        # Case - 8 -> Replace a single character with a single strand DNAList in a single strand DNAList
        original_dna = DNAList('G')
        replace_dna = DNAList('C')
        original_dna.replace('G', replace_dna)
        self.assertEqual(str(original_dna), 'C')

        # Case - 9 -> Replace starting character DNAList in a longer strand DNAList
        original_dna = DNAList('GCT')
        replace_dna = DNAList('CTA')
        original_dna.replace('G', replace_dna)
        self.assertEqual(str(original_dna), 'CTACT')
        self.assertEqual(original_dna.back.value, 'T')

        # Case - 10 -> Replace ending character with a DNAList in a longer strand DNAList
        original_dna = DNAList('GCT')
        replace_dna = DNAList('CTA')
        original_dna.replace('T', replace_dna)
        self.assertEqual(str(original_dna), 'GCCTA')
        self.assertEqual(original_dna.back.value, 'A')

        # Case 11 -> Replace substring towards the end of DNA List with another DNA Strand
        original_dna = DNAList('GCT')
        replace_dna = DNAList('TAG')
        original_dna.replace('CT', replace_dna)
        self.assertEqual(str(original_dna), 'GTAG')
        self.assertEqual(original_dna.back.value, 'G')

        # Case 11 -> Replace substring towards the beginning of DNA List with another DNA Strand
        original_dna = DNAList('GCT')
        replace_dna = DNAList('TAG')
        original_dna.replace('GC', replace_dna)
        self.assertEqual(str(original_dna), 'TAGT')
        self.assertEqual(original_dna.back.value, 'T')

        # Case 11 -> Replace entire string with empty DNA Strand
        original_dna = DNAList('GCT')
        replace_dna = DNAList('')
        original_dna.replace('GCT', replace_dna)
        self.assertEqual(str(original_dna), '')
        self.assertIsNone(original_dna.back)

    def test_copy(self):
        """Function to test DNAList.copy function"""

        # Case - 1 -> Check if the objects are not equal.
        original_dna = DNAList('GCTA')
        duplicate_dna = original_dna.copy()
        self.assertTrue(original_dna != duplicate_dna)

        # Case - 2 -> Update the duplicate_dna and compare both again to make sure they are completely independent.
        duplicate_dna.append('G')
        self.assertEqual(str(original_dna), 'GCTA')
        self.assertEqual(str(duplicate_dna), 'GCTAG')

    def test_str(self):
        """Function to test __str__ of the DNAList class"""

        # Case - 1 -> Check the case for non-empty DNAList.
        original_dna = DNAList('GCT')
        self.assertEqual(str(original_dna), 'GCT')

        # Case - 2 -> Check the case for empty DNAList.
        original_dna = DNAList('')
        self.assertEqual(str(original_dna), '')
        original_dna = DNAList()
        self.assertEqual(str(original_dna), '')

    def test_find_substring_in_dna(self):
        """Function to test DNAList.find_substring_in_dna function"""

        # Case  - 1 - Check if the substring is part of the DNAList or not.
        original_dna = DNAList('GCTATT')
        self.assertTrue(original_dna.find_substring_in_dna(original_dna.head, 'GCT')[0])
        self.assertFalse(original_dna.find_substring_in_dna(original_dna.head, 'ATTA')[0])


if __name__ == '__main__':
    unittest.main()
