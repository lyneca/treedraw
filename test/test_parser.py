import os
from unittest import TestCase
from treedraw.parser import Parser

test_load_file = """
a:1
b :2;c: 3


::root a;;
a>b
b> c;
"""

test_load_file_output = [
    'a:1',
    'b :2',
    'c: 3',
    '::root a',
    'a>b',
    'b> c'
]

class TestParser(TestCase):
    def test_load(self):
        if not os.path.exists('test_parser_load.tree'):
            open('test_parser_load.tree', 'x').close()
        with open('test_parser_load.tree', 'w') as f:
            f.write(test_load_file)
        parser = Parser('test_parser_load.tree')
        loaded = parser.load(parser.file)
        for i, v in enumerate(loaded):
            self.assertTrue(v == test_load_file_output[i])

    def test_make_tree(self):
        pass

    def test_parse_line(self):
        pass
