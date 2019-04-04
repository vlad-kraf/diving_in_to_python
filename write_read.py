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


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        bookmark = {}
        super().__init__(title, content)
        self.size = len(self.content)
        self.author = author
        self.year = year
        self.bookmark = bookmark

    def read(self, page):
        """возвращает страницу"""
        return self.content[page]

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        return self.bookmark[person]

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        del self.bookmark[person]

    def write(self, page, text):
        """делает запись текста text на страницу page """
        self.content[page] = text


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size, max_sign, content):
        """конструктор"""
        super().__init__(title, content)
        self.size = len(self.content)
        self.max_sign = max_sign


    def read(self, page):
        """возвращает страницу с номером page"""
        return self.content[page]

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        z = self.content[page]
        self.content[page] = z + text


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
        book.set_bookmark(self.name, page)

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        return book.get_bookmark(self.name)

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        book.del_bookmark(self.name)
