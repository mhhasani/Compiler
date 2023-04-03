import sys
import os
# Add the path to the generated parser to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from antlr4 import *
from HW2.gen.CPP14Lexer import CPP14Lexer
from HW2.gen.CPP14Parser import CPP14Parser
from HW2.gen.CPP14ParserListener import CPP14ParserListener


# iterate statements by statement and remove braces from single statement blocks
class RemoveBracesListener(CPP14ParserListener):
    def __init__(self):
        self.braces_to_remove = []

    def enterCompoundStatement(self, ctx:CPP14Parser.CompoundStatementContext):
        if len(ctx.statementSeq().statement()) == 1:
            self.braces_to_remove.append(ctx.LeftBrace().symbol.tokenIndex)
            self.braces_to_remove.append(ctx.RightBrace().symbol.tokenIndex)
                
            
    
if __name__ == '__main__':
    input_stream = FileStream('input.cpp')
    lexer = CPP14Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationUnit()
    listener = RemoveBracesListener()
    # remove selected braces from file and save the new result in a new file
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.braces_to_remove)
    output_stream = open('output.cpp', 'w')
    for i in stream.tokens:
        if i.tokenIndex not in listener.braces_to_remove:
            output_stream.write(i.text)
    output_stream.close()




        


        


    

        
    
    
    
    