from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Almacena los errores en una lista
        error_message = f"Error sintáctico en línea {line}, columna {column}: {msg}"
        self.errors.append(error_message)
        print(error_message)
