"""! @brief Определяет классы бинарного дерева"""
##
# @file bts.py
#
# @brief Определяет классы бинарного дерева
#
# @section description_sensors Описание
# Бинарное дерево поиска
print(aa)
class Node:
    """! Нода дерева """
    def __init__(self, val):
        """! Инициализатор класса ноды дерева
        @param val Значение элемента.
        @return Инициализованный элемент дерева.
        """
        ## Левый элемент
        self.l = None
        ## Правый элемент
        self.r = None
        ## Значение элемента
        self.v = val
        #
class Tree:
    """! Дерево бинарного поиска """
    def __init__(self):
        """! Инициализатор класса дерева поиска
        @return Дерево бинарного поиска с проинициализированным корнем.
        """
        self.root = None

    def add(self, val):
        """! Начальная функция добавления элемента в дерево бинарного поиска
        @param val Значение элемента.
        """
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        """! Основная функция добавления элемента в дерево бинарного поиска
        @param val Значение элемента.
        @param node Нода с данными.
        """
        if val.owner_name < node.v.owner_name:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        """! Начальная функция поиска элемента в дереве бинарного поиска
        @param val Искомое значение.
        """
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        """! Основная функция поиска элемента в дереве бинарного поиска
        @param val Значение элемента.
        @param node Нода с данными.
        """
        if val == node.v.owner_name:
            return node
        elif val < node.v.owner_name and node.l:
            return self._find(val, node.l)
        elif val > node.v.owner_name and node.r:
            return self._find(val, node.r)
        
    def creation(self, ticket_list):
        """! Функция инициализации дерева бинарного поиска из списка данных
        @param ticket_list Список значений.
        """
        for tic in ticket_list:
            self.add(tic)