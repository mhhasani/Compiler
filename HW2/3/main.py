import sys
import os
# Add the path to the generated parser to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from antlr4 import *
from gen.CLexer import CLexer
from gen.CParser import CParser
from gen.CListener import CListener


class MyListener(CListener):
    def __init__(self):
        self.structs = []
        
    def enterStructOrUnionSpecifier(self, ctx):
        self.structs.append(ctx.Identifier().getText())

def main():
    input = FileStream("example.c")
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    printer = MyListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(printer.structs)
    print(len(printer.structs))
    

if __name__ == '__main__':
    main()
    
    


