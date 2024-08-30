import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from CompiscriptLexer import CompiscriptLexer
from CompiscriptParser import CompiscriptParser
from antlr4.error.ErrorListener import ErrorListener


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CompiscriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiscriptParser(stream)

    # Custom error listener to capture syntax errors
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse the input code
    tree = parser.program()

    # Collecting lexer tokens
    tokens = []
    input_stream.seek(0)  # Reset input stream to start
    lexer = CompiscriptLexer(input_stream)
    lexer.removeErrorListeners()  # Remove default error listeners
    lexer.addErrorListener(error_listener)  # Add custom error listener

    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_type = token.type
        if token_type >= 0 and token_type < len(lexer.symbolicNames):
            token_name = lexer.symbolicNames[token_type]
        else:
            token_name = "UNKNOWN"
        tokens.append(f"Token: {token.text} (Type: {token_name})")
        token = lexer.nextToken()

    # Preparing the output
    output = ""

    # Add syntax errors to the output if any
    if error_listener.errors:
        output += "Syntax Errors:\n" + "\n".join(error_listener.errors)
    else:
        output += "No se encontraron"
        
    return output

if __name__ == '__main__':
    result = main(sys.argv)
    print(result)
