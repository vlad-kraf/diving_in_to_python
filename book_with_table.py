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

    def read(self, *args, **kwargs):
        raise NotImplementedError

    def write(self, *args, **kwargs):
        raise NotImplementedError


class Novel(Book):
    def __init__(self, author, year, title, content=None):
        super().__init__(title, content)
        self.author = author  # автор
        self.year = year  # год издания
        self.bookmark = {}  # словарь: ключ-читатель,значение-номер страницы

    def read(self, page):
        """возвращает страницу"""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, *args, **kwargs):
        raise PermissionDeniedError

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if person in self.bookmark:
            return self.bookmark[person]
        raise PageNotFoundError

    def del_bookmark(self, person):
        if person in self.bookmark:
            del self.bookmark[person]


class Notebook(Book):
    def __init__(self, title, size=12, max_sign=2000, content=None):
        content = content if content else ['', ] * size
        super().__init__(title, content)
        self.max_sign = max_sign  # максимальное количество символов на странице

    def read(self, page):
        """возвращает страницу"""
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        return self.content[page]

    def write(self, page, text):
        if page < 0 or page >= len(self.content):
            raise PageNotFoundError
        if len(self.content[page]) + len(text) > self.max_sign:
            raise TooLongTextError
        self.content[page] += text


class Person:
    """класс описывающий человека"""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def read(book, page):
        """читаем страницу page в книге book"""
        return book.read(page)

    @staticmethod
    def write(book, page, text):
        """пишем на страницу page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливает закладку в книгу book"""
        if hasattr(book, 'set_bookmark'):
            book.set_bookmark(self, page)
            return
        raise NotExistingExtensionError

    def get_bookmark(self, book):
        """получает номер страницы установленной закладки в книге book"""
        if hasattr(book, 'get_bookmark'):
            return book.get_bookmark(self)
        raise NotExistingExtensionError

    def del_bookmark(self, book):
        """удаляет закладку читателя person, если она установлена"""
        if hasattr(book, 'get_bookmark'):
            book.del_bookmark(self)
            return
        raise NotExistingExtensionError


class AdvancedPerson(Person):

    def __init__(self, name):
        super().__init__(name)

    def search(self, book, name_page):
        """возвращает номер страницы name_page из книги book"""
        if name_page in book.table:
            return book.table[name_page]
        raise PageNotFoundError

    def read(self, book, page):
        # переопределите метод
        if type(page) == int:
            if page < 0 or page >= len(book.content):
                raise PageNotFoundError
            return book.read(page)
        elif type(page) == str:
            page_number = book.search(page)
            if page_number < 0 or page_number >= len(book.content):
                raise PageNotFoundError
            return book.read(page_number)

    def write(self, book, page, text):
        # переопределите метод
        if type(page) == int:
            if page < 0 or page >= len(book.content):
                raise PageNotFoundError
            book.write(page, text)
        elif type(page) == str:
            page_number = book.search(page)
            if page_number < 0 or page_number >= len(book.content):
                raise PageNotFoundError
            book.write(page_number, text)


class NovelWithTable(Novel):
    """класс - книга с оглавлением"""

    def __init__(self, author, year, title, content=None, table={}):
        super().__init__(author, year, title, content)
        self.table = table  # словарь: ключ-название главы,значение-номер страницы

    def search(self, name_page):
        # напишите вашу реализацию метода здесь
        if name_page in self.table:
            return self.table[name_page]
        raise PageNotFoundError

    def add_chapter(self, chapter, page):
        # напишите вашу реализацию метода здесь
        self.table[chapter] = page

    def remove_chapter(self, chapter):
        # напишите вашу реализацию метода здесь
        if chapter in self.table:
            del self.table[chapter]
        else:
            raise PageNotFoundError