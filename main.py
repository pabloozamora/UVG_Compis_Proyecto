import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from CompiscriptLexer import CompiscriptLexer
from CompiscriptParser import CompiscriptParser
from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import DotExporter
from SemanticVisitor import SemanticVisitor
from TACVisitor import TACVisitor
from MyErrorListener import MyErrorListener

""" def create_tree(node, parser, parent=None):
    if node.getChildCount() == 0:  # Es una hoja
        return Node(node.getText(), parent=parent)
    
    rule_name = parser.ruleNames[node.getRuleIndex()]
    tree_node = Node(rule_name, parent=parent)
    for child in node.getChildren():
        create_tree(child, parser, tree_node)
    return tree_node """
    
def main():
    # Cargar archivo de entrada
    input_stream = FileStream("input.txt")
    
    # Crear lexer y parser
    lexer = CompiscriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiscriptParser(stream)
    
    # Crear error listener
    error_listener = MyErrorListener()
    
    # Agregar el error listener al lexer y parser
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    # Iniciar análisis sintáctico
    tree = parser.program()
    
    # Renderizar el árbol sintáctico
    # print("Árbol de análisis sintáctico:\n")
    print(tree.toStringTree(recog=parser), "\n")
    
    if error_listener.errors:
        print("El programa contiene errores sintácticos.")
        return
        
    semanticVisitor = SemanticVisitor()
    semanticVisitor.visit(tree)
    
    if semanticVisitor.hasErrors:
        print("El programa contiene errores semánticos.")
        for error in semanticVisitor.result:
            print(error)
        return
    
    print(semanticVisitor.code_generator)
    
if __name__ == '__main__':
    main()