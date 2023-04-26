import re
import os
from antlr4 import *
from gen.JavaScriptLexer import JavaScriptLexer

def main():
    file = os.path.join(os.path.dirname(__file__), 'example.js')
    lexer = JavaScriptLexer(FileStream(file))    
    token = lexer.nextToken()
    while token.type != token.EOF:
        text = token.text
        if token.type in [lexer.MultiLineComment, lexer.SingleLineComment, lexer.StringLiteral]:
            email = re.search(r'[\w\.-]+@[\w\.-]+', text)
            if email:
                print(email.group(0))
        token = lexer.nextToken()

if __name__ == '__main__':
    main()