class CustomNestedObject:
    """Custom weird class to handle __getitem__

    TODO: add error handling for strings and other non list/tuple objects
    """

    ERRORS = {
        'element_doesnt_exist': "You don't have element with such index"
    }

    def __init__(self, obj):
        self._nested = []       # will store nested recursive CustomNestedObject(s)
        self._value = None      # will store value (for example integer or string)
        # recursively parse obj to CustomNestedObject
        self._parse_to_self(obj)
        print("nested: ",self._nested)

    def __repr__(self):
        """Method which will return string representation for the nested objects or self._value"""
        if not self._nested:
            return str(self._value)
        else:
            return str([x._value for x in self._nested])

    def __str__(self):
        return 'return of str'

    def __getitem__(self, index):
        # handle error
        try:
            self._nested[index]
        except IndexError:
            raise Exception(self.ERRORS['element_doesnt_exist'])
        if not self._nested[index]._nested:
            # it means that returned object will be self.value
            # print(f'trying to access {self._nested[index]._value}')
            return self._nested[index]._value
        else:
            # print('trying to access nested object')
            return self._nested[index]

    def _parse_to_self(self, obj):
        if isinstance(obj, list) or isinstance(obj, tuple):
            for item in obj:
                self._nested.append(CustomNestedObject(item))
        else:
            # save as number if obj is not a list or tuple
            self._value = obj


if __name__ == '__main__':
    x = CustomNestedObject([1, 2, 3, [4, 5]])
    print(x[3][0])
    print(x[3][1])
    print(x[0])
    print(repr(x))
    print(x)
    # print(x[9])