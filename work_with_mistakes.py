class Page:
    """класс страница"""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    # напишите вашу реализацию методов здесь   
    def __iadd__(self, other):
        if type(self) and type(other) in (Page, str):
                if type(self) == Page:
                    return str(self + other._text)
                    

                elif type(self) == 'str':
                    

                    temp = self._text + other

                    if len(temp) > self.max_sign:
                        raise TooLongTextError
                    self._text = temp
                    
                    return self 

        else: raise TypeError ('zxczxc')


    def __add__(self, other):
        print('2')
        if type(self) and type(other) in (Page, str):
            if type(self) == Page:
                temp = self._text + other

                if len(temp) > self.max_sign:
                    raise TooLongTextError
                self._text = temp
                
                return self._text

            elif type(self) == str:
                return str(self + other._text)

        else: raise TypeError

    def __lt__(self, other):
        if len(self._text) < len(other):
            return True
        return False

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


class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __iter__(self):
        for page in self.content:
            yield page

    def __len__(self):
        return len(self._content)
    
    def __getitem__(self, key):
        return self._content[key-1]

    def __setitem__(self, key):
        return self._content[key-1]
        
    
    

    # напишите вашу реализацию методов здесь