import copy
from emoji import get_emoji_regexp
from whatsparser import WhatsParser


class TestWhatsParser:

    FILE_PATH = './test_data/data.txt'
    messages = WhatsParser(FILE_PATH)

    def test_get_authors(self):
        '''Asserts total number of different authors'''
        authors = self.messages.authors
        assert isinstance(authors, list)
        assert len(authors) == 5

    def test_len(self):
        '''Asserts total number of mesanges'''
        length = len(self.messages)
        assert isinstance(length, int)
        assert length == 200

    def test_filter(self):
        '''Asserts if it works with the filter function'''
        fil = filter(lambda m: m['author'] == 'Odile Pema', self.messages)
        assert any(fil)
        assert all((m['author'] == 'Odile Pema' for m in list(fil)))

    def test_list_comprehension(self):
        '''Asserts if it works with list comprehension'''
        def change(m):
            m['content'] = 'NEW CONTENT'
            return m

        new_content = [change(m) for m in self.messages]

        # Assert that content has changed in new list
        assert all((m['content'] == 'NEW CONTENT' for m in new_content))
        # Assert that content remains the same in original list
        assert new_content[0] != self.messages[0]

    def test_map(self):
        '''Asserts if it works with map function. Map function should not modify
        the original data unless the new array is assign to messages.data'''
        def change(m):
            m['content'] = 'NEW CONTENT'
            return m

        new_content = list(map(change, self.messages))

        # Assert that content has changed in new list
        assert all((m['content'] == 'NEW CONTENT' for m in new_content))
        # Assert that content remains the same in original list
        assert new_content[0] != self.messages[0]

    def test_modify_message(self):
        '''Assigning by indexing'''
        new_message = {'datetime': '13/1/2018 20:12:43',
                       'author': 'Agustin Rodriguez',
                       'content': 'Que mensajuli eh!'}
        self.messages[0] = new_message
        assert self.messages[0] == new_message

    def test_change_original(self):
        '''Asserts if it is possible to loop though the data and assign the
        new array to override the old data'''
        def remove_emojis(m):
            m['content'] = get_emoji_regexp().sub(r'', m['content'])
            return m

        self.messages.data = list(map(remove_emojis, self.messages))

        assert not all(
            [get_emoji_regexp().match(m['content']) for m in self.messages]
        )

    def test_for_looping(self):
        '''Tests for both looping modalities, the one that changes data and
        the one that doen't'''
        for m in self.messages.data:
            # This loop should modify data
            m['content'] = 'TEST'

        for m in self.messages:
            # This loop shouldn't modify data
            m['content'] = 'NOT A TEST'

        for m in self.messages:
            # Test for loop
            assert m['content'] == 'TEST'
