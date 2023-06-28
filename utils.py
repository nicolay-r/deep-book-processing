import os
from os.path import join

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
RANK_DATASET_DIR = join(PROJECT_DIR, "data/hla_books")


def cat_files(source_filepaths, target_filepath):
    assert(isinstance(source_filepaths, list))

    with open(target_filepath, 'w') as outfile:
        for fname in source_filepaths:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


class Paragraph:
    """ Description of the paragraph.
    """

    def __init__(self, line_ind):
        """ Create emtpy paragraph.
        """
        self.__line_from = line_ind
        self.__line_to = line_ind
        self.__text = ""

    @property
    def DisplayBounds(self):
        return "[{}-{}]".format(self.__line_from, self.__line_to)

    @property
    def Text(self):
        return self.__text

    @property
    def LineFrom(self):
        return self.__line_from

    @property
    def LineTo(self):
        return self.__line_to

    def extend(self, line, line_ind):
        assert(line_ind >= self.__line_from)
        self.__text += line
        self.__line_to = line_ind

    def num_words(self):
        return len(self.__text.split())

    def modify_text(self, f):
        assert(callable(f))
        self.__text = f(self.__text)

    def __contains__(self, item):
        return item in self.__text
