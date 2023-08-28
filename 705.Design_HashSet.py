class MyHashSet:

    def __init__(self):
        self.my_dict = {}

    def add(self, key: int) -> None:
        self.my_dict[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.my_dict.pop(key)

    def contains(self, key: int) -> bool:
        if key in self.my_dict:
            return True
        return False
    