class TooLongTextError(Exception):
    pass


class PageNotFoundError(Exception):
    pass


class Page:
    """класс страница"""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    # напишите вашу реализацию методов здесь   
    def __iadd__(self, other):

        if type(self) not in (Page, str) or type(other) not in (Page, str):
            raise TypeError

        if len(self) + len(other) > self.max_sign:
            raise TooLongTextError

        return self + other

    def __add__(self, other):
        self._text = self._text + other
        return self

    def __radd__(self, other):
        self._text = other + self._text
        return self._text

    def __gt__(self, other):
        if len(self._text) > len(other):
            return True
        return False

    def __le__(self, other):
        if len(self._text) <= len(other):
            return True
        return False

    def __ge__(self, other):
        if len(self._text) >= len(other):
            return True
        return False

    def __str__(self):
        return self._text

    def __repr__(self):
        return self._text
    
    def __len__(self):
        return len(self._text)

    def __eq__(self, other):
        if len(self) == len(other):
            return True
        return False


class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __len__(self):
        return len(self._content)
    
    def __getitem__(self, key):
        if key < 0 or key > len(self._content):
            raise PageNotFoundError
        return self._content[key-1]

    def __setitem__(self, key, value):
        self._content[key-1].text = value
        return self
