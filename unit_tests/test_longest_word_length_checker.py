from src import Longest_Word_Length_Checker as wl
import unittest


class test_wordlength(unittest.TestCase):

    def test_can_return_longest_word_and_length(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "I am a long sentence"
        expected_length = [8, 'sentence']
        actual_longest_length = length_checker.longest_word_checker(sentence)
        self.assertEqual(expected_length, actual_longest_length)

    def test_can_return_longest_length(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "I am a long sentence"
        expected_length = 8
        actual_longest_length = length_checker.longest_word_checker(sentence)[0]
        self.assertEqual(expected_length, actual_longest_length)

    def test_can_return_longest_word(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "I am a long sentence"
        expected_word = 'sentence'
        actual_longest_word = length_checker.longest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_longest_word)

    def test_can_return_blank_sentence(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = ""
        expected_word = ''
        actual_longest_word = length_checker.longest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_longest_word)

    def test_can_return_longest_word_when_2_words_with_same_length_exists(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "long bond"
        expected_word = 'bond'
        actual_longest_word = length_checker.longest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_longest_word)

    def test_can_return_longest_word_with_special_character(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "#macdonald is yummy"
        expected_word = '#macdonald'
        actual_longest_word = length_checker.longest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_longest_word)

    def test_can_return_longest_length_of_a_zero_length_sentence(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = ""
        expected_length = 0
        actual_longest_length = length_checker.longest_word_checker(sentence)[0]
        self.assertEqual(expected_length, actual_longest_length)

