"""Flake8 plugin checking for relative imports."""
import ast


__version__ = '0.0.1'

R100 = 'R100: Found relative import'


class RelativeImportFinder(ast.NodeVisitor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.relative_imports = []

    def visit_ImportFrom(self, node):
        if node.level > 0:
            self.relative_imports.append(node)


class RelativeImportChecker:
    name = 'flake8-relative'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        visitor = RelativeImportFinder()
        visitor.visit(self.tree)

        for import_node in visitor.relative_imports:
            yield (import_node.lineno, import_node.col_offset, R100, type(self))
