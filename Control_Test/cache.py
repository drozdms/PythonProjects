class LRUCache(object):

    _default_ttl = None

    def __init__(self, n, default_ttl=600):
        self._N = n
        self._default_ttl = default_ttl
        self._dict = {}
        self._list = LRUCache.Node()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val

    def clear(self):
        self._dict.clear()
        self._list = None

    def is_empty(self):
        return not self._dict

    @property
    def N(self):
        return self._N

    @property
    def size(self):
        return len(self._dict)

    @property
    def default_ttl(self):
        return self._default_ttl

    def get_value(self, key):
        if key not in dict:
            return None
        if not self._dict[key].is_expired():
            self._list.move_to_end(self._dict[key])

    @default_ttl.setter
    def default_ttl(self, new_ttl):
        self._default_ttl = new_ttl

    def __is_expired(self, key):
        return self._dict[key].is_expired()

    class Node(object):
        def __init__(self, value=None, key=None, TTL= None, next_ = None):
            self._TTL = LRUCache.DEFAULT_TTL if TTL is None else TTL
            self._key = key
            self._value = value
            self._next = next_

        @property
        def is_expired(self):
            return self._TTL <= 0

        def move_to_end(self, obj):
            iterator = self
            prev = iterator
            while iterator != obj:
                prev = iterator
                iterator = iterator._next
            prev._next = iterator._next
            it = iterator
            prev = it
            while it:
                prev = it
                it = it._next
            prev._next = it
            it._next = None

        def __iter__(self):
            iterator = self
            while iterator:
                yield iterator
                iterator = iterator._next
