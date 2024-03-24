"""! @brief Файл класса хеш-таблицы"""
##
# @file hash_table.py
#
# @brief Определяет класс хеш-таблицы
#
# @section description_sensors Описание
# Бинарное дерево поиска
print(aa)
class HashTable:
    """! Хеш-таблица """
    def __init__(self, _list):
        """! Инициализатор класса хеш-таблицы
        @param _list Список значений для инициализации.
        @return Инициализованная хеш-таблица.
        """
        ## Делитель для определения хеша
        self.factor = 870977
        ## Сама таблица
        self.table = [None]*self.factor
        #
        for i in _list:
            self.add_elem(f"{i.owner_name[0]} {i.owner_name[1]} {i.owner_name[2]}", i)

    def add_elem(self, key, value):
        """! Функция добавления элемента в хеш-таблицы
        @param value Значение элемента.
        @param key Ключ для поиска.
        """
        self.table[hash(key) % self.factor] = value

    def get(self, key):
        """! Функция получения элемента из хеш-таблицы
        @param key Ключ для поиска.
        """
        return self.table[hash(key) % self.factor]

    def remove(self, key):
        """! Функция удаления элемента из хеш-таблицы
        @param key Ключ для поиска.
        """
        self.table[hash(key) % self.factor] = None

