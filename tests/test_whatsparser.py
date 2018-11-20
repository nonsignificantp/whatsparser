import random
from whatsparser import WhatsParser

class TestWhatsParser:
    FILE_PATH = './tests/test_data.txt'
    messages = WhatsParser(FILE_PATH)

    def test_get_item_as_dict(self):
        index = random.randrange(len(self.messages))
        assert isinstance(self.messages[index], dict)

    def test_get_authors(self):
        authors = self.messages.authors
        assert isinstance(authors, list)
        assert len(authors) == 2

    def test_len(self):
        length = len(self.messages)
        assert isinstance(length, int)
