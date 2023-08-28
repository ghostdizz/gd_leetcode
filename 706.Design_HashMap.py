class MyHashMap:

    def __init__(self):
        self.my_dict = {}

    def put(self, key: int, value: int) -> None:
        self.my_dict[key] = value

    def get(self, key: int) -> int:
        if key in self.my_dict:
            return self.my_dict[key]
        return -1
    def remove(self, key: int) -> None:
        if key in self.my_dict:
            self.my_dict.pop(key)
        else:
            return None
