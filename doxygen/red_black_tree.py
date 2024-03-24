"""! @brief Определяет классы красно-чёрного бинарного дерева"""
##
# @file red_black_tree.py
#
# @brief Определяет классы красно-чёрного бинарного дерева
#
# @section description_sensors Описание
# Красно-чёрное дерево бинарного поиска
print(aa)
class Node:
    """! Нода дерева """
    def __init__(self, key, data=None, color="RED"):
        """! Инициализатор класса ноды дерева
        @param key Ключ для поиска.
        @param data Что элемент должен содержать в себе.
        @param color Цвет элемента.
        @return Инициализованный элемент дерева.
        """
        ## Ключ для поиска.
        self.key = key
        ## Значение элемента
        self.data = data
        ## Цвет элемента
        self.color = color
        ## Ссылка на родителя
        self.parent = None
        ## Левый элемент
        self.left = None
        ## Правый элемент
        self.right = None
        #

class RedBlackTree:
    """! Красно-чёрное дерево бинарного поиска """
    def __init__(self):
        """! Инициализатор класса дерева поиска
        @return Красно-чёрное дерево бинарного поиска с проинициализированным корнем.
        """
        ## Инициализация начального содержимого дерева.
        self.NIL = Node(None)
        ## Корень дерева.
        self.root = self.NIL
        #

    def insert(self, key, data=None):
        """! Функция добавления элемента в красно-чёрное дерево бинарного поиска
        @param data Значение элемента.
        @param key Ключ для поиска.
        """
        node = Node(key, data, color="RED")
        node.parent = self.NIL
        node.left = self.NIL
        node.right = self.NIL

        current = self.root
        parent = None

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _fix_insert(self, node):
        """! Функция балансировки красно-чёрного дерева бинарного поиска
        @param node Главный элемент, участвующий в балансировке.
        """
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = "BLACK"

    def _left_rotate(self, x):
        """! Функция левого поворота красно-чёрного дерева бинарного поиска"""
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """! Функция правого поворота красно-чёрного дерева бинарного поиска"""
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def find_element(self, ptr, key):
        """! Функция поиска элемента в красно-чёрном дереве бинарного поиска
        @param key Ключ для поиска.
        @param ptr Элемент, с которого будет начат поиск.
        """
        if ptr is not None:
            if key == ptr.key:
                return ptr.data
            elif key < ptr.key:
                return self.find_element(ptr.left, key)
            else:
                return self.find_element(ptr.right, key)
        else:
            print()
            print(f"""Element {key} is {'not found'.upper()} in the tree""")
            return None

    def build_from_list(self, ticket_list):
        """! Функция инициализации красно-чёрного дерева бинарного поиска из списка данных
        @param ticket_list Список значений.
        """
        for ticket in ticket_list:
            self.insert(ticket.owner_name, ticket)