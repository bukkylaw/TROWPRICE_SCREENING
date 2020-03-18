from src import Longest_Word_Length_Checker as wl
import unittest

class Test_short_wordlength(unittest.TestCase):

    def test_can_return_shortest_word_and_length(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "I am a short sentence"
        expected_length = [1, 'a']
        actual_shortest_length = length_checker.shortest_word_checker(sentence)
        self.assertEqual(expected_length, actual_shortest_length)

    def test_can_return_shortest_length(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "I am a short sentence"
        expected_length = 1
        actual_shortest_length = length_checker.shortest_word_checker(sentence)[0]
        self.assertEqual(expected_length, actual_shortest_length)

    def test_can_return_shortest_word(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "I am a long sentence"
        expected_word = 'a'
        actual_shortest_word = length_checker.shortest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_shortest_word)

    def test_can_return_blank_sentence(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = ""
        expected_word = ''
        actual_shortest_word = length_checker.shortest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_shortest_word)

    def test_can_return_shortest_word_when_2_words_with_same_length_exists(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "long bond"
        expected_word = 'bond'
        actual_shortest_word = length_checker.shortest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_shortest_word)

    def test_can_return_shortest_word_with_special_character(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = "#macdonald is* yummy"
        expected_word = 'is*'
        actual_shortest_word = length_checker.shortest_word_checker(sentence)[1]
        self.assertEqual(expected_word, actual_shortest_word)

    def test_can_return_shortest_length_of_a_zero_length_sentence(self):
        length_checker = wl.Longest_Word_Length_Checker()
        sentence = ""
        expected_length = 0
        actual_shortest_word = length_checker.shortest_word_checker(sentence)[0]
        self.assertEqual(expected_length, actual_shortest_word)





