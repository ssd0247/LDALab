"""Helper function for preprocessing raw text data into well-structured
input expected by the complex, downstream algorithms."""
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