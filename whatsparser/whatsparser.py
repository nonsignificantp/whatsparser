import re
import os
import copy
import pandas as pd
from .message import Message
from dateutil.parser import parse

class WhatsParser:

    def __init__(self, file_path):
        self.header = []
        self.messages = self._get_messages_from_file(file_path)

    def _get_absolute_file_path(self, file_path):
        '''Returns the absolute path for the target .txt file'''
        return os.path.abspath(file_path)

    def _get_messages_from_file(self, file_path):
        '''Iterates trough all messages inside .txt file and creates messages
        instances that are loaded inside self.messages. All the first lines
        inside the file that are not messanges are considered as headers.'''

        messages = []
        path_to_file = self._get_absolute_file_path(file_path)

        with open(path_to_file) as file:

            for line in file:
                if self._is_start_of_new_message(line):
                    message = self._construct_message(line)
                    messages.append(message)
                elif any(messages):
                    messages[-1]['content'] += f' {line.strip()}'
                else:
                    self.header.append(line.strip())

        return messages

    def _construct_message(self, line):
        '''Removes data from each line inside the file and returns a Message'''
        datetime = self._get_datetime_from_line(line)
        author = self._get_author_from_line(line)
        content = self._get_content_from_line(line, author)
        return {'datetime': datetime, 'author': author, 'content': content}

    def to_dataframe(self):
        '''Converts the WhatsParser object into a pandas dataframe'''
        messages = [item for item in self.messages]
        return pd.DataFrame(messages)

    @staticmethod
    def _is_start_of_new_message(line):
        '''All lines starting with a datetime are considered the beginnig of
        a new messange'''
        if re.match(r'^\d+/\d+/\d+\s\d+:\d+:\d+\s(AM|PM)', line):
            return True
        return False

    @staticmethod
    def _get_datetime_from_line(line):
        '''Extracts datetime data from a line'''
        datetime = re.search(r'^.+(AM|PM)(?=:)', line).group()
        return parse(datetime)

    @staticmethod
    def _get_author_from_line(line):
        '''Extracts author data from a line'''
        author = re.search(r'(?<=:\s)(.*?)(?=:)', line).group()
        return author

    @staticmethod
    def _get_content_from_line(line, author):
        '''Extracts content data from a line'''
        start = re.search(author, line).span()[1]
        content = re.search(r'(?<=:\s).*$', line[start:]).group().strip()
        return content

    @property
    def authors(self):
        '''Returns an array listing all unique authors of all messages'''
        return list(set([msg['author'] for msg in self.messages]))

    def __getitem__(self, position):
        '''Returns a dictionary with all message public properties'''
        return self.messages[position]

    def __setitem__(self, position, value):
        self.messages[position] = value

    def __iter__(self):
        '''Makes object iterable'''
        msgs = copy.deepcopy(self.messages)
        count = 0
        while count < len(msgs):
            yield msgs.pop(0)
            count += 1

    #def __next__(self):
    #    self.count += 1
    #    if self.count > len(self.messages):
    #        self.count = 0
    #        raise StopIteration
    #    return self.messages[self.count-1]

    def __len__(self):
        '''Returns total number of messages'''
        return len(self.messages)
