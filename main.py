import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from CompiscriptLexer import CompiscriptLexer
from CompiscriptParser import CompiscriptParser
from anytree import Node, RenderTree, AsciiStyle
from anytree.exporter import DotExporter
from MyVisitor import MyVisitor
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    # Obtener el código fuente directamente desde el cuerpo de la solicitud
    code = request.get_json().get('code')
    
    # Crear un stream desde el código recibido
    input_stream = InputStream(code)
    lexer = CompiscriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiscriptParser(stream)
    tree = parser.program()

    # Usar el visitor para analizar el árbol sintáctico
    visitor = MyVisitor()
    visitor.visit(tree)
    
    result = visitor.getResult()

    # Devolver el resultado como JSON
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
