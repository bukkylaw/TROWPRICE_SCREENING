class Longest_Word_Length_Checker:

    def longest_word_checker(self,sentence):

        longest_word = ''
        for word in sentence.split(' '):
            if len(word) >= len(longest_word):
                longest_word = word
                longest_length = len(longest_word)
        a = [longest_length, longest_word]
        return a
