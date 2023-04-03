import sys
import os
# Add the path to the generated parser to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from antlr4 import *
from gen.CPP14Lexer import CPP14Lexer
from gen.CPP14Parser import CPP14Parser 
from gen.CPP14ParserListener import CPP14ParserListener


class ClassNameListener(CPP14ParserListener):
    def __init__(self):
        self.class_names = []
        
    # find class names
    def enterClassName(self, ctx:CPP14Parser.ClassSpecifierContext):
        class_name = ctx.Identifier().getText()
        self.class_names.append(class_name)

def find_class_names(file_path):
    with open(file_path, "r") as file:
        input_stream = InputStream(file.read())
        lexer = CPP14Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CPP14Parser(stream)
        tree = parser.translationUnit()
        printer = ClassNameListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        print(printer.class_names)
        print(len(printer.class_names))

if __name__ == '__main__':
    file_path = "example.cpp"
    find_class_names(file_path)



