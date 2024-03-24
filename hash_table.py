# Хеш-таблица

class HashTable:
    def __init__(self, _list):
        self.factor = 870977
        self.table = [None]*self.factor

        for i in _list:
            self.add_elem(f"{i.owner_name[0]} {i.owner_name[1]} {i.owner_name[2]}", i)

    def add_elem(self, key, value):
        self.table[hash(key) % self.factor] = value

    def get(self, key):
        return self.table[hash(key) % self.factor]

    def remove(self, key):
        self.table[hash(key) % self.factor] = None

