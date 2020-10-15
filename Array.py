class Array(object):
    """Array implementation based on tuple."""

    def __init__(self, *args):
        """
        Constructor of member of class.

        Can get multiple arguments of any type suitable for tuple.

        :param args: elements of array
        """
        self._data = tuple(args)
        self._ptr = 0

    def set_data(self, data_to_set):
        """
        Sets data of Array to some given tuple.

        :param data_to_set: elements to set
        """
        self._data = data_to_set

    def get_data(self):
        """
        Allows to get data of Array from outside.

        :return: tuple of data
        """
        return self._data

    def append(self, item_to_append):
        """
        Appends new item in the end of an Array.

        :param item_to_append: item to append
        """
        self._data = self._data + (item_to_append, )

    def __add__(self, other):
        """
        Overrides plus operator for two Arrays.

        :param other: another element of Array class to add with
        """
        result_array = Array()
        result_array.set_data(self._data + other.get_data())
        return result_array

    def __len__(self):
        """
        Overrides len() function for Array.

        :return: length of self._data tuple
        """
        return len(self._data)

    def index(self, item_to_find):
        """
        Gives index of item in Array.

        :param item_to_find: item to find in array
        :return: index in tuple or -1, if such element does not exist
        """
        try:
            return self._data.index(item_to_find)
        except ValueError:
            return -1

    def __iter__(self):
        """
        Sets iterator pointer to the beginning of an Array.

        Overrides 'for' with '__next__' function.
        :return: self as an iterable
        """
        self._ptr = 0
        return self

    def __next__(self):
        """
        Gives next element of an Array after the current one.

        Overrides 'for' with '__next__' function.
        :return: current element in Array
        """
        if self._ptr == len(self._data):
            raise StopIteration
        cur = self._data[self._ptr]
        self._ptr += 1
        return cur

    def __getitem__(self, pos):
        """
        Gets item in array by its position.

        Position must lie in range [0,...,len(self._data)).
        :param pos: position in tuple
        :return: item in array by its position
        """
        return self._data[pos]

    def pop(self, item_index):
        """
        Removes item from an Array by its index.

        Index must lie in range [0,...,len(self._data)).
        :param item_index: index of item to be removed
        """
        if 0 <= item_index < len(self._data):
            self._data = self._data[:item_index] + self._data[item_index + 1:]

    def remove(self, rem_item):
        """
        Removes item from an Array by its value.

        If there are multiple items with such value,
        the one with the smallest index will be removed
        :param rem_item: value of item to be removes
        """
        self.pop(self.index(rem_item))


if __name__ == '__main__':
    array_example = Array()
