class BookIOErrors(Exception):
    pass


class PageNotFoundError(BookIOErrors):
    pass


class TooLongTextError(BookIOErrors):
    pass


class PermissionDeniedError(BookIOErrors):
    pass


class NotExistingExtensionError(BookIOErrors):
    pass


class Book(object):
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        super(Novel, self).__init__(title, content)
        bookmark = {}
        self.size = len(self.content)
        self.author = author
        self.year = year
        self.bookmark = bookmark

    def read(self, page):
        """возвращает страницу"""
        if 0 <= page < len(self.content):
            try:
                return self.content[page]
            except IndexError:
                raise PageNotFoundError
        else:
            raise PageNotFoundError

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if person in self.bookmark.keys():
            return self.bookmark[person]
        else:
            raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        del self.bookmark[person]

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size=12, max_sign=2000, content=None):
        """конструктор"""
        super(Notebook, self).__init__(title, content)
        self.max_sign = max_sign
        if not content:
            self.size = size
            """инициализируется список пустых строк длины size"""
            self.content = ['' for _ in range(self.size)]
        else:
            self.size = len(self.content)

    def read(self, page):
        """возвращает страницу с номером page"""
        if 0 <= page < len(self.content):
            try:
                return self.content[page]
            except IndexError:
                raise PageNotFoundError
        else:
            raise PageNotFoundError

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        if 0 <= page < len(self.content):
            if len(text) >= self.max_sign:
                raise TooLongTextError
            else:
                try:
                    self.content[page] = self.content[page] + text
                except IndexError:
                    raise PageNotFoundError
        else:
            raise PageNotFoundError


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        if type(book).__name__ == 'Novel':
            book.set_bookmark(self, page)
        elif type(book).__name__ == 'Notebook':
            raise NotExistingExtensionError

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        if type(book).__name__ == 'Novel':
            return book.get_bookmark(self)
        elif type(book).__name__ == 'Notebook':
            raise NotExistingExtensionError

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        if type(book).__name__ == 'Novel':
            book.del_bookmark(self)
        elif type(book).__name__ == 'Notebook':
            raise NotExistingExtensionError
