from util import warning

class Tree:
    """
    Class for representing a tree
    """
    def __init__(self):
        self.root = None
        self.symbols = {}
        self.links = {}

    def set_root(self, symbol):
        self.root = symbol

    def add_symbol(self, symbol, value):
        """
        Adds a symbol to the tree.

        :param symbol: the 'key'
        :param value: the 'value'
        """
        if symbol in self.symbols:
            warning("symbol {} already exists".format(symbol))
        self.symbols[symbol] = value

    def add_children(self, parent, children):
        """
        Registers children to a parent

        :param parent: List of children to add to the node
        :param children: List of children to add to the parent
        """
        if parent in self.links:
            warning("symbol {} already linked".format(parent))
        self.links[parent] = children

    def exists(self, symbol):
        return symbol in self.symbols
    
    def check(self):
        if not self.root:
            error("tree has no root set")
    
    def get_children(self, parents):
        line = []
        for parent in parents:
            if parent in self.links:  # if parent has children
                line += self.links[parent]
        return line
    
    def get_values(self, symbols):
        return [self.symbols[s] for s in symbols]

    def print_levels(self):
        print(self.symbols[self.root])
        next_line = self.get_children([self.root])
        print(' '.join(self.get_values(next_line)))
        while next_line:
            next_line = self.get_children(next_line)
            print(' '.join(self.get_values(next_line)))
