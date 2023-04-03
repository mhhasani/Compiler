import sys
import os
# Add the path to the generated parser to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from antlr4 import *
from HW2.gen.CPP14Lexer import CPP14Lexer

def main():
    lexer = CPP14Lexer(FileStream(r"input.cpp"))
    output_stream = open(r"output.cpp", "w")
    token = lexer.nextToken()
    while token.type != token.EOF:
        text = token.text
        if token.type == lexer.BlockComment:
            text = "//" + text[2:-2]
            text = text.replace("\n", "\n//")
        output_stream.write(text)
        token = lexer.nextToken()


if __name__ == '__main__':
    main()