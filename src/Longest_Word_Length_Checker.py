class Longest_Word_Length_Checker:

    def longest_word_checker(self,sentence):
        longest_word = ''
        for word in sentence.split(' '):
            if len(word) >= len(longest_word):
                longest_word = word
                longest_length = len(longest_word)
        long_word = [longest_length, longest_word]
        return long_word

    def shortest_word_checker(self, sentence):
        shortest_word = sentence
        for word in sentence.split(' '):
            if len(word) < len(shortest_word):
                shortest_word = word
                shortest_length = len(shortest_word)
        short_word = [shortest_length, shortest_word]
        return short_word
