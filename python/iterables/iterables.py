"""Sentence

Created custom type to manipulate with sentences like with usual lists.
"""
import re


class MultipleSentencesError(Exception):
    """ Custom exception occurs when the count of sentences more than 1. """

    def __init__(self, count: int):
        self.__message = f"Expected 1 sentence, got {count}"

    def __str__(self):
        return self.__message


class SentenceIterator:
    """ Makes the sentence possible to iterate. """

    def __init__(self, text: str):
        self._text = text
        self._star_with = 0

    def __iter__(self):
        return self

    def __next__(self):
        found_word = re.search(r"[A-z]+", self._text[self._star_with:])

        if found_word is None:
            raise StopIteration

        self._star_with += found_word.end()

        return found_word.group()


class Sentence:
    """ A type that provides some operations on a sentence and its words. """

    def __init__(self, text: str):
        """ Initiate if the text is valid. """
        self._is_valid(text)
        self.__text = text

    @staticmethod
    def _is_valid(text: str) -> None:
        """Check is the text valid.

        Requirements:
            -it should be str
            -sentence should be completed
            -it should contain only 1 sentence
        """
        if type(text) is not str:
            raise TypeError
        sentence_count = len(re.findall(r"[.!?]+", text))
        if sentence_count == 0:
            raise ValueError
        if sentence_count > 1:
            raise MultipleSentencesError(sentence_count)

    def __iter__(self):
        return SentenceIterator(self.__text)

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def _words(self):
        """ Get generator """
        for _word in self.__iter__():
            yield _word

    @property
    def words(self) -> [str]:
        """ Get list of all words. """
        return list(self._words())

    @property
    def other_chars(self) -> [str]:
        """ Get list of all non-word characters. """
        other_chars_template = f"[^A-z]"
        return re.findall(other_chars_template, self.__text)

    def __getitem__(self, item):
        words_count = len(self.words)

        if isinstance(item, slice):

            start = 0 if item.start is None else item.start
            stop = words_count if item.stop is None else item.stop
            step = 1 if item.step is None else item.step

            # TODO: implement negative slice validation

            _slice = ""
            for num in range(start, stop, step):
                _slice += self.words[num] + self.other_chars[num]
            return _slice

        if item >= words_count or item < -words_count:
            raise IndexError
        return self.words[item]


def main():
    """Show how it works: """

    sentence_1 = Sentence("Hello world!")

    print(sentence_1)
    print(sentence_1.words)
    print(sentence_1.other_chars)
    print(sentence_1[0])
    print(sentence_1[:])

    for word in sentence_1:
        print(word)


if __name__ == "__main__":    main()
