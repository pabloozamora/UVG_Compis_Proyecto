import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from CompiscriptLexer import CompiscriptLexer
from CompiscriptParser import CompiscriptParser
from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import DotExporter
from SemanticVisitor import SemanticVisitor
from MyErrorListener import MyErrorListener
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])   
def main():
    print('\n--- INICIA EJECUCIÓN ---\n')
    # Cargar archivo de entrada
    code = request.get_json().get('code')
    input_stream = InputStream(code)
    
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
    # print(tree.toStringTree(recog=parser), "\n")
    
    if error_listener.errors:
        print("El programa contiene errores sintácticos.")
        
        response = []
        response.append("El programa contiene errores sintácticos.")
        response.append(error_listener.errors)
        return jsonify(result=response)
        
    semanticVisitor = SemanticVisitor()
    semanticVisitor.visit(tree)
    
    if semanticVisitor.hasErrors:
        response = []
        response.append("El programa contiene errores semánticos.")
        
        print("El programa contiene errores semánticos.")
        for error in semanticVisitor.result:
            print(error)
            response.append(error)
            
        return jsonify(result=response)
    
    print(semanticVisitor.code_generator)
    
    response = [str(instruction) for instruction in semanticVisitor.code_generator.instructions]
    return jsonify(result=response)
    
    return 
    
if __name__ == '__main__':
    app.run(debug=True)