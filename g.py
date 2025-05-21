import sys
from antlr4 import *
from grammar.gLexer import gLexer
from grammar.gParser import gParser
from classes.TreeVisitor import TreeVisitor
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error de sintaxis en línea {line}, columna {column}: {msg}")

def main():
    
    if len(sys.argv) != 2:
        print("Error: Debe proporcionar un archivo de código fuente.")
        print("Uso: python3 g.py archivo.j")
        sys.exit(1)
    
    try:
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
        
        lexer = gLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(CustomErrorListener())
        
        token_stream = CommonTokenStream(lexer)
        parser = gParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())
        
        tree = parser.program()
        
        visitor = TreeVisitor()
        visitor.visit(tree)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()