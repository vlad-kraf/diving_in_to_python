import calendar

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
        
        if len(self) + len(other) > self.max_sign:
            raise TooLongTextError
        
        self._text = self._text + other

        return self

    def __radd__(self, other):
        other = other + self._text
        return other

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
    
    def __eq__(self, other):
        if len(self) == len(other):
            return True
        return False
    
    def __str__(self):
        return self._text

    def __repr__(self):
        return self._text
    
    def __len__(self):
        return len(self._text)


class Book(object):
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __len__(self):
        return len(self._content)
    
    def __getitem__(self, key):
        if key < 1 or key > len(self._content):
            raise PageNotFoundError
        return self._content[key-1]

    def __setitem__(self, key, value):
        self._content[key-1] = Page(str(value))


    def __gt__(self, other):
        if len(self._content) > len(other._content):
            return True
        return False

    def __le__(self, other):
        if len(self._content) <= len(other._content):
            return True
        return False

    def __ge__(self, other):
        if len(self._content) >= len(other._content):
            return True
        return False
    
    def __eq__(self, other):

        if type(self) != Book or type(other) != Book:
            raise TypeError
        
        if len(self._content) == len(other._content):
            return True
        return False


class CalendarBookmark:
    """класс дескриптор - закладка для ежедневника"""
    def __init__(self, value=0):
        self.value = int(value)

    def __get__(self, instance, instance_class):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    



# часть 3 --------------------------------------------------------------------------------------------------------------

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
    """класс книги - ежедневник с закладкой"""

    bookmark = CalendarBookmark() # присваиваем дескриптор переменной с закаладками

    def __init__(self, title, content=None):
        super(CalendarBook, self).__init__(title, content)
        table_of_contents = 'TABLE OF CONTENT\n'

        #генерируем страницы жедневника на заданный год.
        for month in range(1, 13):
            #Добавляем календарь на первую страницу для каждого месяца в ежедневнике.
            self._content.append(Page(str(calendar.TextCalendar(calendar.SUNDAY).formatmonth(int(self.title), month))))
            table_of_contents += calendar.month_name[month] + ':' + str(len(self._content)) + '\n'
            for date in calendar.Calendar().itermonthdates(int(self.title), month):
                #Проверяем соответствует ли номер месяца месяцу для которого нужно создать страницы
                # по дням в ежедневнике
                if date.month == month:
                    #создаем страницы дней по датам в ежедневнике
                    self._content.append(Page(str(date)))
        self._content.append(table_of_contents)