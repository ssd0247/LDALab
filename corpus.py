"""
Helper function for preprocessing text in the format: 

    {word_id :word_count}

into the Document() and Corpus() objects.

These objects are the models for `document` and `object`,
in the sense they are used in Latent Dirichlet Allocation (LDA).
"""

import re
# read and organize data

#3 2:3 4:5 5:3 --- document info (word:count)
class Document:
    """The class for a single document."""
    def __init__(self):
        self.words = []
        self.counts = []
        self.length = 0
        self.total = 0

class Corpus:
    """The class for the whole corpus."""
    def __init__(self):
        self.size_vocab = 0
        self.docs = []
        self.num_docs = 0

    def read_data(self, filename):
        """Reads in the data from a file."""
        pass

def read_stream_data(f, num_docs):
    """Convert a dynamic stream of data into a static corpus."""
    

def read_data(filename):
    """Convert the raw file having lines as ``wordid : wordcnt`` into
    the ``Document()`` and ``Corpus()`` objects.
    """
    pass

def count_tokens(filename):
    """Given the filename, find the total number of unique tokens."""
    pass

