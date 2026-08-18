class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dictionary = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.dictionary:
            self.dictionary.move_to_end(key)
            return self.dictionary[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.dictionary[key] = value
        self.dictionary.move_to_end(key)
        if (len(self.dictionary) > self.cap):
            self.dictionary.popitem(last=False)
            print(self.dictionary)