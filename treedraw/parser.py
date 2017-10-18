from .tree import Tree
from .util import error, warning
import sys
import re

class Parser:
    """
    .tree file parser class
    """
    def __init__(self, f):
        """
        :param f: name of file to parse
        """

        self.file = f

        self.def_regex = re.compile(r'^\w+\s*:\s*.+$')
        self.child_regex = re.compile(r'^\w+\s*>\s*\w+(,\s*\w+)*$')

        self.tree = Tree()

    def load(self, f):
        with open(f, 'r') as f:
            file_lines = f.read().split('\n')

        # ; seperation
        lines = []
        for line in file_lines:
            if not line: continue  # blank lines
            for statement in line.split(';'):
                if statement.strip():
                    lines.append(statement.strip())
        return lines
    
    def make_tree(self):
        lines = self.load(self.file)
        for line in lines:
            self.parse_line(line)
        self.tree.check()
        return self.tree

    def parse_line(self, line):
        if line.startswith("::"):
            return self.parse_special(line[2:].strip())
        elif self.def_regex.match(line):
            return self.parse_definition(line)
        elif self.child_regex.match(line):
            return self.parse_child(line)
        else:
            self.syntax_error(line)

    def parse_special(self, line):
        if line.split()[0] == 'root':
            symbol = line.split()[1]
            if not self.tree.exists(symbol):
                warning("root symbol {} does not exist".format(symbol))
            self.tree.set_root(symbol)

    def parse_definition(self, line):
        symbol = line.split(':')[0].strip()

        # In case they want to put a : in their value
        value  = ':'.join(line.split(':')[1:]).strip()
        self.tree.add_symbol(symbol, value)

    def parse_child(self, line):
        parent = line.split('>')[0].strip()

        if not self.tree.exists(parent):
            return self.unknown_symbol(parent)

        children = line.split('>')[1].strip()
        children = [x.strip() for x in children.split(',')]

        for child in children:
            if not self.tree.exists(child):
                return self.unknown_symbol(child)

        self.tree.add_children(parent, children)       

    def syntax_error(self, string):
        error("syntax error in line \"{}\"".format(string))

    def unknown_symbol(self, symbol):
        error("unknown symbol \"{}\"".format(symbol))


if __name__ == '__main__':
    parser = Parser(sys.argv[1])
    tree = parser.make_tree()
    tree.print_levels()

