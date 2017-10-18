import sys
import argparse
from .render import Renderer
from .parser import Parser

def main():
    p = argparse.ArgumentParser(description='Render a tree image from a .tree file', add_help=False)
    p.add_argument('input', type=str, help='input .tree file')
    p.add_argument('output', type=str, help='output filename (.png only for now)')
    p.add_argument('-w', '--width', default=800, type=int, help='output file width in pixels')
    p.add_argument('-h', '--height', default=600, type=int, help='output file height in pixels')
    p.add_argument('-b', '--border', default=2, type=int, help='border width of nodes in tree')
    p.add_argument('--help', action='help', help='show this help message and exit')
    args = p.parse_args()

    parser = Parser(args.input)
    renderer = Renderer(args.output, args.width, args.height, args.border)
    print("Parsing...")
    tree = parser.make_tree()
    print("Rendering...")
    renderer.render_tree(tree)
    print("Done.")

if __name__ == '__main__':
    main()
