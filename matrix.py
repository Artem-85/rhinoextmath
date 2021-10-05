"""
Rhino Extended Math/Matrix

A very simple alternative to numpy for using in Rhino Python

Module for basic operations on vectors and matrices.
"""

import math

__ERRORS_LIST = {
    "wrong_argument": "Wrong type of the argument ({})",
    "wrong_type": "Wrong type"
}

def is_iterable(item):
    """ Check an item for iterability """
    return (isinstance(item, list) or isinstance(item, tuple))

def is_number(item):
    """ Check if an item is a number (int or float) """
    return (isinstance(item, int) ^ isinstance(item, float))

def matmul(matrA, matrB):
    # check types:
    if (isinstance(matrA, Matrix) and isinstance(matrB, Matrix)):
        pass # TODO: check sizes!!
    elif (isinstance(matrA, Matrix) and isinstance(matrB, Vector)):
        if matrB.is_transposed():
            raise Exception(__ERRORS_LIST["wrong_argument"].format(2))
    elif (isinstance(matrA, Vector) and isinstance(matrB, Matrix)):
        if not matrA.is_transposed():
            raise Exception(__ERRORS_LIST["wrong_argument"].format(1))
    else:
        raise Exception(__ERRORS_LIST["wrong_type"])
    print("checks passed")
    #TODO main implementation

class _DataCell(object):
    """ Parent "abstract" class for vectors and matrices.
        Used to store the lowermost element in a hierarchical structure (Vector, Matrix etc.)
    """

    _ERRORS_LIST = {
        "access": "Incorrect attempt to access to private functions",
        "not_iterable": "The input data ({}) for Matrix class is not a list nor a tuple",
        "overnested": "The input data ({}) for Matrix contains too many nested levels (expected: {}, maximum: {})",
        "wrong_type": "The input data ({}) for Matrix contains wrong format (must be int or float)",
        "wrong_index": "Wrong item index ({})",
        "nonuniform": "Inconsistent dimensions of the rows in the matrix"
        }

    def __init__(self, data = None, data_type = None, nested_level = 0, dimensions = 0):
        # empty data is not allowed
        if (data == None):
            raise Exception(self._ERRORS_LIST["access"])
        # a tuple of nested objects
        self._data_row = []
        # a values of the lowest-level object
        self._data_value = None
        # by default, the element is not on the top
        # self._top_level = False
        # current hierarchy level (0 is on the top)
        self._current_nested_level = nested_level
        # start index for iterator
        self.__index = -1
        self.__data_type = data_type
        self.__dimensions = dimensions
        # start processing the input data
        self.__process_input(data, data_type)
        self.__length = len(self._data_row)

    def __process_input(self, data, data_type = None):
        if is_iterable(data):
            # print("current level",self._current_nested_level,"data",data,"dimensions",self.__dimensions)
            self._current_nested_level += 1
            for item in data:
                if is_iterable(item):
                    # print("iterate on current level",self._current_nested_level,"data",data,"dimensions",self.__dimensions)
                    if (self._current_nested_level >= self.__dimensions):
                        raise Exception(self._ERRORS_LIST["overnested"].format(data, self._current_nested_level + 1, self.__dimensions))
                self._data_row.append(_DataCell(item, data_type, 
                    self._current_nested_level, self.__dimensions))
        elif not is_number(data):
            raise Exception(self._ERRORS_LIST["wrong_type"].format(data))
        else:
            if (data_type == "float"):
                self._data_value = float(data)
            elif (data_type == "int"):
                self._data_value = int(data)
            else:
                self._data_value = data

    def __getitem__(self, index):
        try:
            self._data_row[index]
        except IndexError:
            raise Exception(self._ERRORS_LIST["wrong_index"].format(index))
        if not self._data_row[index]._data_row:
            return self._data_row[index]._data_value
        else:
            ret = []
            for item in self._data_row[index]:
                ret.append(item._data_value)
            return ret

    def __str__(self):
        if (self._data_value == None):
            ret = self._get_data()
        else:
            ret = str(self._data_value)
        return ret

    def __repr__(self):
        if (self._data_value == None):
            ret = self._get_data(True)
        else:
            ret = str(self._data_value)
        return ret

    def __iter__(self):
        return self

    def next(self):
        self.__index += 1
        max = self.__length
        if (self.__index >= max):
            self.__index = -1
            raise StopIteration
        return self._data_row[self.__index]

    # def prev(self):
    #     self.__index -= 1
    #     if self.__index < 0:
    #         raise StopIteration
    #     return self._data_row[self.__index]

    # think more about that
    def __reversed__(self):
        return self._get_data(reversed = True, list = True)

    def _get_data(self, repr = False):
        if repr:
            # seems like this option is not employed anywhere
            ret = "["
            template = "{:12f}" if self.__data_type == "float" else "{:12d}"
            for i in range(self.__length):
                ret += template.format(self._data_row[i]._data_value)
                if (i < self.__length - 1):
                    ret += ","
            ret += "]"
        else:
            ret = []
            for i in range(self.__length):
                ret.append(self._data_row[i]._data_value)
            ret = str(ret)
        return ret

class Vector(_DataCell):
    """
    Class for operations on vectors.

    Parameters
    ----------
    data 
        (list or tuple of ints or floats)
        A list or a tuple of ints or floats
        Example: [1, 4, 6]

    transposed 
        (optional, bool, default: false)
        Flag to distinguish normal ("vertical") or transposed ("horizontal") vectors
    
    data_type 
        (optional, str [ 'int' (default) | 'float' ])
        Data type for further operations and representation

    """

    def __init__(self, data = None, transposed = False, data_type = 'float'):
        if not is_iterable(data):
            raise Exception(self._ERRORS_LIST["not_iterable"].format(data))
        else:
            self.__dimensions = 1
            self._data_type = data_type
            super(Vector, self).__init__(data, data_type, dimensions = self.__dimensions)
            # self._top_level = True
            self.__length = len(self._data_row)
            self.__transposed = transposed

    def __len__(self):
        return self.__length

    def _get_data(self, repr = False, reversed = False, list = False):
        if list:
            ret = []
            for i in range(self.__length):
                ret.append(self._data_row[i]._data_value)
            ret = str(ret)
        else:
            if repr:
                ret = "Transposed v" if self.__transposed else "V" 
                ret += "ector of {}s [".format(self._data_type)
            else:
                ret = "["
            template = "{:12f}" if self._data_type == "float" else "{:12d}"
            if reversed:
                start = self.__length - 1
                stop = -1
                inc = -1
                last = 0
            else:
                start = 0
                stop = self.__length
                inc = 1
                last = self.__length - 1
            for i in range(start, stop, inc):
                ret += template.format(self._data_row[i]._data_value)
                if (i != last):
                    ret += "\t" if self.__transposed else "\n"
            ret += "]"
        return ret

    """ Whether the vector is transposed or not"""
    def is_transposed(self):
        return self.__transposed
    
    def set_transposed(self, status = False):
        self.__transposed = True if status else False

class Matrix(_DataCell):
    """
    Class for operations on matrices.

    Parameters
    ----------
    data
        tuple (list) of lines of a matrix (represented as tuples or lists) (example: [[2, 7], [8, 5]])
    
    """
    def __init__(self, data = None, data_type = 'float'):
        if not is_iterable(data):
            raise Exception(self._ERRORS_LIST["not_iterable"].format(data))
        else:
            # number of dimensions
            self.__dimensions = 2
            # initial horizontal dimension
            self._size_h = -1
            for row in data:
                if not is_iterable(row):
                    raise Exception(self._ERRORS_LIST["not_iterable"].format(row))
                else:
                    if (self._size_h == -1):
                        # we always accept the length of the first row as the intended horizontal dimension
                        self._size_h = len(row)
                    elif (self._size_h != len(row)):
                        raise Exception(self._ERRORS_LIST["nonuniform"])
            # vertical dimension
            self._size_v = len(data)
            self._data_type = data_type
            super(Matrix, self).__init__(data, data_type, dimensions = self.__dimensions)

    def __len__(self):
        return len(self._data_row)

    def _get_data(self, repr = False):
        if repr:
            ret = []
            for row in self._data_row:
                ret.append([])
                for item in row:
                    ret[-1].append(item)
            return "Matrix of {}s ".format(self._data_type) + str(ret) 
        else:
            ret = "["
            template = "{:12f}" if self._data_type == "float" else "{:12d}"
            for i in range(self._size_v):
                if (i != 0):
                    ret += " "
                ret += "["
                for j in range(self._size_h):
                    ret += template.format(self._data_row[i]._data_row[j]._data_value)
                    if (j < self._size_h - 1):
                        ret += ", " if repr else "\t"
                ret += "]"
                if (i < self._size_v - 1):
                    ret += "," if repr else "\n"
            ret += "]"
        return str(ret)

    def get_row(self, index):
        ret = []
        for item in self._data_row[index]:
            ret.append(item)
        return ret
    
    def get_column(self, index):
        ret = []
        for row in self._data_row:
            ret.append(row[index])
        return ret

    def get_size_vert(self):
        return self._size_v
    
    def get_size_hor(self):
        return self._size_h

__all__ = ["Matrix", "Vector"]