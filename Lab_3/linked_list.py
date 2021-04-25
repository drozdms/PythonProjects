class Node(object):
    def __init__(self, value, next_=None):
        assert isinstance(next_, Node) or next_ is None
        self._value = value
        self._next = next_

    def __iter__(self):
        iterator = self
        while iterator:
            yield iterator
            iterator = iterator._next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


def flatten_linked_list(linked_list):
    if not isinstance(linked_list, Node):
        return [linked_list]
    flattened_list = []
    for i in linked_list:
        flattened_list.extend(flatten_linked_list(i.value))
    return flattened_list
