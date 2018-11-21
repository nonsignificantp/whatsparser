import random
import copy
from whatsparser import WhatsParser, Message


class TestWhatsParser:

    FILE_PATH = './tests/test_data.txt'
    messages = WhatsParser(FILE_PATH)

    def test_get_authors(self):
        authors = self.messages.authors
        assert isinstance(authors, list)
        assert len(authors) == 6

    def test_len(self):
        length = len(self.messages)
        assert isinstance(length, int)

    def test_filter(self):
        fil = filter(lambda m: m.author == 'Alejandro Casco', self.messages)
        assert all((m.author == 'Alejandro Casco' for m in list(fil)))

    def test_list_comprehension(self):
        def change(m):
            m.content = 'NEW CONTENT'
            return m

        new_content = [change(m) for m in self.messages]

        # Assert that content has changed in new list
        assert all((m.content == 'NEW CONTENT' for m in new_content))
        # Assert that content remains the same in original list
        assert new_content[0] != self.messages[0]

    def test_map(self):
        def change(m):
            m.content = 'NEW CONTENT'
            return m

        new_content = list(map(change, self.messages))

        # Assert that content has changed in new list
        assert all((m.content == 'NEW CONTENT' for m in new_content))
        # Assert that content remains the same in original list
        assert new_content[0] != self.messages[0]

    def test_modify_message(self):
        new_message = Message('13/1/2018 20:12:43',
                              'Agustin Rodriguez',
                              'Que mensajuli eh!')
        self.messages[0] = new_message
        assert self.messages[0] == new_message

    def test_modify_message_datetime(self):
        pass

    def test_modify_message_author(self):
        pass

    def test_modify_message_content(self):
        pass
