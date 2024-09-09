# Unit tests for the count_palindromic_substrings function
import unittest

class TestCountPalindromicSubstrings(unittest.TestCase):
    def test_example(self):
        self.assertEqual(count_palindromic_substrings("abba"), 6)

    def test_single_character(self):
        self.assertEqual(count_palindromic_substrings("a"), 1)

    def test_no_palindromes(self):
        self.assertEqual(count_palindromic_substrings("abc"), 3)

    def test_all_same_characters(self):
        self.assertEqual(count_palindromic_substrings("aaaa"), 10)

    def test_mixed_characters(self):
        self.assertEqual(count_palindromic_substrings("racecar"), 10)

if __name__ == '__main__':
    unittest.main()