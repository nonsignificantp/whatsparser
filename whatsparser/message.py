from dateutil.parser import parse

class Message:

    def __init__(self, datetime, author, content):
        self._datetime = self._parse_datetime(datetime)
        self._author = author
        self._content = content

    def _add_content(self, line):
        self._content += f' {line.strip()}'

    @staticmethod
    def _parse_datetime(datetime):
        if isinstance(datetime, str):
            return parse(datetime)
        return datetime

    @property
    def size(self):
        return len(self._content)

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, new_value):
        self._datetime = new_value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_value):
        self._author = new_value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_value):
        self._content = new_value

    def __str__(self):
        return f"{self._datetime} - {self._author}: {self._content}"

    def __repr__(self):
        return f"{self._datetime} - {self._author}: {self._content}"

    def __dict__(self):
        return {'datetime': self._datetime,
                'author': self._author,
                'content': self._content}
