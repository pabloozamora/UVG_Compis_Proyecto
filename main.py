import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from CompiscriptLexer import CompiscriptLexer
from CompiscriptParser import CompiscriptParser
from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import DotExporter
from MyVisitor import MyVisitor


""" def create_tree(node, parser, parent=None):
    if node.getChildCount() == 0:  # Es una hoja
        return Node(node.getText(), parent=parent)
    
    rule_name = parser.ruleNames[node.getRuleIndex()]
    tree_node = Node(rule_name, parent=parent)
    for child in node.getChildren():
        create_tree(child, parser, tree_node)
    return tree_node """

def main():
    input_stream = FileStream("suma.txt")
    lexer = CompiscriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiscriptParser(stream)
    tree = parser.program()
    
    # Renderizar el árbol sintáctico

    # print("Árbol de análisis sintáctico:\n")
    print(tree.toStringTree(recog=parser), "\n")

    """ root = create_tree(tree, parser)

    for pre, fill, node in RenderTree(root, style=AsciiStyle()):
        print("%s%s" % (pre, node.name)) """
        
    visitor = MyVisitor()
    print(visitor.visit(tree))

if __name__ == '__main__':
    main()
