class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())   # {'a': 1, 'b': 2} => dict_items([('a', 1), ('b', 2)])
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.items):
            return self.items[self.index]
        raise StopIteration


#class dictionary_iter:
#
#    def __init__(self, dictionary: dict):
#        self.items = list(dictionary.items())   # {'a': 1, 'b': 2} => dict_items([('a', 1), ('b', 2)])
#
#    def __iter__(self):
#        return iter(self.items)