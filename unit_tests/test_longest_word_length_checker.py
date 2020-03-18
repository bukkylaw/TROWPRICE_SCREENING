from src import Longest_Word_Length_Checker as wl
import unittest


class test_wordlength(unittest.TestCase):

    def test_can_return_longest_length(self):
        length_checker = wl.WordLength()
        sentence = "I am a long sentence"
        expected_length = 8
        actual_longest_length = length_checker.longest_word_checker(sentence)[0]
        self.assertEqual(expected_length, actual_longest_length)

    def test_can_return_longest_word(self):
        length_checker = wl.WordLength()
        sentence = "I am a long sentence"
        expected_word = 'sentence'
        actual_longest_word = length_checker.longest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_longest_word)