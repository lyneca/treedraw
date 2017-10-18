"""
Treedraw
"""
from .render import Renderer
from .parser import Parser


if __name__ == '__main__':
    parser = Parser('test.tree')
    rend = Renderer('test.png')
    rend.render_tree(parser.make_tree())
