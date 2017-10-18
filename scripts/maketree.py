from treemake import Parser, Renderer

parser = Parser(sys.argv[1])
renderer = Renderer(sys.argv[2])
renderer.render_tree(parser.make_tree())
