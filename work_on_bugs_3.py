class Person:
    """класс описывающий человека"""

    def __init__(self, name):
        self.name = name

    def set_bookmark(self, *args, **kwargs):
        pass

    def get_bookmark(self, *args, **kwargs):
        pass

    def del_bookmark(self, *args, **kwargs):
        pass


class Reader:
    def read(self, book, num_page):
        pass


class Writer:
    def write(self, book, num_page, text):
        pass


class AdvancedPerson(Person, Reader, Writer):
    """класс человека умеющего читать, писать, пользоваться закладками"""

    def set_bookmark(self, book, num_page):
        pass

    def get_bookmark(self, book):
        pass

    def del_bookmark(self, book, person):
        pass

    def search(book, page):
        pass

    def read(self, book, page):
        pass

    def write(self, book, page, text):
        pass


class PageTableContents(Page):

    def __init__(self, text=None, max_sign=2000):
        pass

    def search(self, chapter):
        pass


class CalendarBook(Book):
    """класс ежедневник с закладкой"""

    def __init__(self, title, content=None):
        pass