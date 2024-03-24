class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
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
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.v.owner_name:
            return node
        elif val < node.v.owner_name and node.l:
            return self._find(val, node.l)
        elif val > node.v.owner_name and node.r:
            return self._find(val, node.r)
        
    def creation(self, ticket_list):
        for tic in ticket_list:
            self.add(tic)